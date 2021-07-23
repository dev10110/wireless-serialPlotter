# brief:
# creates a dashboard for live plotting of uppercuts telemetry data

# installation: 
#   python3 -m pip install pyqtgraph
#   python3 -m pip install numpy

# usage:
#   python3 plotter.py

import pyqtgraph as pg
import signal

# import the dashboard class
from dashboard import Dashboard


if __name__ == '__main__':
    # change behaviour, such that if Ctrl+c is pressed, it will execute a kill command
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    # create the dashboard
    dash = Dashboard()

    # data should be inserted by calling
    #   dash.insertMotorData(self, motor_id, t, rpm, rpm_cmd, current, current_cmd, voltage, temperature)
    # where motor_id is "DL", "DR", "WL" or "WR"
    
    # calling update will update the plot and the text
    dash.test_getData()
    dash.update()
    
    
    # it can either be called in a loop:

    # for i in range(100):
    #   start = timer()
    #   dash.testUpdate()
    #   end = timer()
    #   print(1.0/(end - start))

    # or from a timer
    timer = pg.Qt.QtCore.QTimer()
    timer.timeout.connect(dash.testUpdate)
    timer.start(0) 
    
    # needed, but not sure why
    pg.exec()
    
    

