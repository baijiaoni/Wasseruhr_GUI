from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from org.eclipse.jface.dialogs import MessageDialog
from time import gmtime, strftime

a = PVUtil.getDouble(pvs[0])

if a > 30000:
    MessageDialog.openInformation(
            None, "Error message", "Maximum flow is 30000");

