import logging
import time
from PyQt5 import QtCore

from PyQt5.QtWidgets import QMessageBox, QApplication, QTableView

from sportorg.core.otime import OTime
from sportorg.gui.dialogs.about import AboutDialog
from sportorg.gui.dialogs.bib_report_dialog import BibReportDialog
from sportorg.gui.dialogs.cp_delete import CPDeleteDialog
from sportorg.gui.dialogs.entry_filter import DialogFilter
from sportorg.gui.dialogs.event_properties import EventPropertiesDialog
from sportorg.gui.dialogs.file_dialog import get_open_file_name, get_save_file_name
from sportorg.gui.dialogs.live_dialog import LiveDialog
from sportorg.gui.dialogs.not_start_dialog import NotStartDialog
from sportorg.gui.dialogs.number_change import NumberChangeDialog
from sportorg.gui.dialogs.print_properties import PrintPropertiesDialog
from sportorg.gui.dialogs.relay_number_dialog import RelayNumberDialog
from sportorg.gui.dialogs.report_dialog import ReportDialog
from sportorg.gui.dialogs.search_dialog import SearchDialog
from sportorg.gui.dialogs.settings import SettingsDialog
from sportorg.gui.dialogs.start_chess_dialog import StartChessDialog
from sportorg.gui.dialogs.start_preparation import StartPreparationDialog, guess_courses_for_groups
from sportorg.gui.dialogs.start_report_dialog import StartReportDialog
from sportorg.gui.dialogs.start_time_change_dialog import StartTimeChangeDialog
from sportorg.gui.dialogs.team_report_dialog import TeamReportDialog
from sportorg.gui.dialogs.team_results_report_dialog import TeamResultsReportDialog
from sportorg.gui.dialogs.text_io import TextExchangeDialog
from sportorg.gui.dialogs.timekeeping_properties import TimekeepingPropertiesDialog
from sportorg.gui.menu.action import Action
from sportorg.libs.winorient.wdb import write_wdb
from sportorg.models.memory import race, ResultStatus
from sportorg.models.result.result_calculation import ResultCalculation
from sportorg.models.result.result_checker import ResultChecker
from sportorg.models.start.start_preparation import guess_corridors_for_groups
from sportorg.modules import testing
from sportorg.modules.iof import iof_xml
from sportorg.modules.live.orgeo import OrgeoClient
from sportorg.modules.ocad import ocad
from sportorg.modules.ocad.ocad import OcadImportException
from sportorg.modules.sportident.sireader import SIReaderClient
from sportorg.modules.winorient import winorient
from sportorg.modules.winorient.wdb import WDBImportError, WinOrientBinary
from sportorg.language import _


class NewAction(Action):
    def execute(self):
        self.app.create_file()


class SaveAction(Action):
    def execute(self):
        self.app.save_file()


class OpenAction(Action):
    def execute(self):
        file_name = get_open_file_name(_('Open SportOrg file'), _("SportOrg file (*.sportorg)"))
        self.app.open_file(file_name)


class SaveAsAction(Action):
    def execute(self):
        self.app.save_file_as()


class OpenRecentAction(Action):
    def execute(self):
        pass


class SettingsAction(Action):
    def execute(self):
        SettingsDialog().exec()


class EventSettingsAction(Action):
    def execute(self):
        EventPropertiesDialog().exec()


class CSVWinorientImportAction(Action):
    def execute(self):
        file_name = get_open_file_name(_('Open CSV Winorient file'), _("CSV Winorient (*.csv)"))
        if file_name is not '':
            try:
                winorient.import_csv(file_name)
            except Exception as e:
                logging.exception(str(e))
                QMessageBox.warning(self.app, _('Error'), _('Import error') + ': ' + file_name)
            self.app.init_model()


class WDBWinorientImportAction(Action):
    def execute(self):
        file_name = get_open_file_name(_('Open WDB Winorient file'), _("WDB Winorient (*.wdb)"))
        if file_name is not '':
            try:
                winorient.import_wo_wdb(file_name)
            except WDBImportError as e:
                logging.exception(str(e))
                QMessageBox.warning(self.app, _('Error'), _('Import error') + ': ' + file_name)
            self.app.init_model()


class OcadTXTv8ImportAction(Action):
    def execute(self):
        file_name = get_open_file_name(_('Open Ocad txt v8 file'), _("Ocad classes v8 (*.txt)"))
        if file_name is not '':
            try:
                ocad.import_txt_v8(file_name)
            except OcadImportException as e:
                logging.exception(str(e))
                QMessageBox.warning(self.app, _('Error'), _('Import error') + ': ' + file_name)
            self.app.init_model()


class WDBWinorientExportAction(Action):
    def execute(self):
        file_name = get_save_file_name(_('Save As WDB file'), _("WDB file (*.wdb)"),
                                       '{}_sportorg_export'.format(time.strftime("%Y%m%d")))
        if file_name is not '':
            try:
                wb = WinOrientBinary()

                self.app.clear_filters(False)
                wdb_object = wb.export()
                self.app.apply_filters()

                write_wdb(wdb_object, file_name)
            except Exception as e:
                logging.exception(str(e))
                QMessageBox.warning(self.app, _('Error'), _('Export error') + ': ' + file_name)


class IOFResultListExportAction(Action):
    def execute(self):
        file_name = get_save_file_name(_('Save As IOF xml'), _("IOF xml (*.xml)"),
                                       '{}_resultList'.format(time.strftime("%Y%m%d")))
        if file_name is not '':
            try:
                iof_xml.export_result_list(file_name)
            except Exception as e:
                logging.exception(str(e))
                QMessageBox.warning(self.app, _('Error'), _('Export error') + ': ' + file_name)


class AddObjectAction(Action):
    def execute(self):
        self.app.add_object()


class DeleteAction(Action):
    def execute(self):
        self.app.delete_object()


class TextExchangeAction(Action):
    def execute(self):
        TextExchangeDialog().exec()
        self.app.refresh()


class RefreshAction(Action):
    def execute(self):
        self.app.refresh()


class FilterAction(Action):
    def execute(self):
        if self.app.current_tab not in range(2):
            return
        table = self.app.get_current_table()
        DialogFilter(table).exec()


class SearchAction(Action):
    def execute(self):
        if self.app.current_tab not in range(5):
            return
        table = self.app.get_current_table()
        SearchDialog(table).exec()


class ToStartPreparationAction(Action):
    def execute(self):
        self.app.select_tab(0)


class ToRaceResultsAction(Action):
    def execute(self):
        self.app.select_tab(1)


class ToGroupsAction(Action):
    def execute(self):
        self.app.select_tab(2)


class ToCoursesAction(Action):
    def execute(self):
        self.app.select_tab(3)


class ToTeamsAction(Action):
    def execute(self):
        self.app.select_tab(4)


class StartPreparationAction(Action):
    def execute(self):
        StartPreparationDialog().exec()


class GuessCoursesAction(Action):
    def execute(self):
        guess_courses_for_groups()
        self.app.refresh()


class GuessCorridorsAction(Action):
    def execute(self):
        guess_corridors_for_groups()
        self.app.refresh()


class RelayNumberAction(Action):
    def execute(self):
        obj = race()
        if obj.get_setting('relay_number_assign', False):
            obj.set_setting('relay_number_assign', False)
            QApplication.restoreOverrideCursor()
        else:
            obj.set_setting('relay_number_assign', True)
            QApplication.setOverrideCursor(QtCore.Qt.PointingHandCursor)
            RelayNumberDialog().exec()
        self.app.refresh()


class NumberChangeAction(Action):
    def execute(self):
        NumberChangeDialog().exec()


class StartTimeChangeAction(Action):
    def execute(self):
        StartTimeChangeDialog().exec()


class StartListAction(Action):
    def execute(self):
        StartReportDialog().exec()


class TeamListAction(Action):
    def execute(self):
        TeamReportDialog().exec()


class StartTimesAction(Action):
    def execute(self):
        StartChessDialog().exec()


class PrintBibAction(Action):
    def execute(self):
        BibReportDialog().exec()


class ManualFinishAction(Action):
    def execute(self):
        result = race().new_result()
        race().add_new_result(result)
        logging.info('Manual finish')
        self.app.get_result_table().model().init_cache()
        self.app.refresh()
        self.app.auto_save()


class SPORTidentReadoutAction(Action):
    def execute(self):
        SIReaderClient().set_call(self.app.add_sportident_result_from_sireader).start()


class CreateReportAction(Action):
    def execute(self):
        ReportDialog().exec()


class CreateTeamResultsReportAction(Action):
    def execute(self):
        TeamResultsReportDialog().exec()


class SplitPrintoutAction(Action):
    def execute(self):
        self.app.split_printout_selected()


class RecheckingAction(Action):
    def execute(self):
        logging.debug('Rechecking start')
        for result in race().results:
            if result.person is not None:
                ResultChecker.checking(result)
        logging.debug('Rechecking finish')
        ResultCalculation(race()).process_results()
        self.app.refresh()


class PenaltyCalculationAction(Action):
    def execute(self):
        logging.debug('Penalty calculation start')
        for result in race().results:
            if result.person is not None:
                ResultChecker.calculate_penalty(result)
        logging.debug('Penalty calculation finish')
        ResultCalculation(race()).process_results()
        self.app.refresh()


class PenaltyRemovingAction(Action):
    def execute(self):
        logging.debug('Penalty removing start')
        for result in race().results:
            result.penalty_time = OTime(msec=0)
            result.penalty_laps = 0
        logging.debug('Penalty removing finish')
        ResultCalculation(race()).process_results()
        self.app.refresh()


class ChangeStatusAction(Action):
    def execute(self):
        if self.app.current_tab != 1:
            logging.warning(_('No result selected'))
            return
        obj = race()

        status_dict = {
            ResultStatus.NONE: ResultStatus.OK,
            ResultStatus.OK: ResultStatus.DISQUALIFIED,
            ResultStatus.DISQUALIFIED: ResultStatus.DID_NOT_START,
            ResultStatus.DID_NOT_START: ResultStatus.DID_NOT_FINISH,
            ResultStatus.DID_NOT_FINISH: ResultStatus.OK,
        }

        table = self.app.get_result_table()
        assert isinstance(table, QTableView)
        index = table.currentIndex().row()
        if index < 0:
            index = 0
        if index >= len(obj.results):
            mes = QMessageBox()
            mes.setText(_('No results to change status'))
            mes.exec()
            return
        result = obj.results[index]
        result.status = status_dict[result.status]
        self.app.refresh()


class SetDNSNumbersAction(Action):
    def execute(self):
        NotStartDialog().exec()


class AddSPORTidentResultAction(Action):
    def execute(self):
        result = race().new_sportident_result()
        race().add_new_result(result)
        logging.info('SPORTident result')
        self.app.get_result_table().model().init_cache()
        self.app.refresh()
        self.app.auto_save()


class TimekeepingSettingsAction(Action):
    def execute(self):
        TimekeepingPropertiesDialog().exec()


class PrinterSettingsAction(Action):
    def execute(self):
        PrintPropertiesDialog().exec()


class LiveSettingsAction(Action):
    def execute(self):
        LiveDialog().exec()


class LiveSendStartListAction(Action):
    def execute(self):
        OrgeoClient().send_start_list()


class LiveSendResultsAction(Action):
    def execute(self):
        OrgeoClient().send_results()


class LiveResendResultsAction(Action):
    def execute(self):
        OrgeoClient().clear()
        OrgeoClient().send_results()


class AboutAction(Action):
    def execute(self):
        AboutDialog().exec()


class TestingAction(Action):
    def execute(self):
        testing.test()


class CPDeleteAction(Action):
    def execute(self):
        CPDeleteDialog().exec()
