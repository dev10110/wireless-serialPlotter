import numpy as np
from pyqtgraph.Qt import QtCore
import pyqtgraph as pg

class Dashboard:

  def __init__(self):

    pg.setConfigOptions(antialias=True, background='w', foreground='k')

    self.app = pg.mkQApp("Uppercut Telemetry")

    self.win = pg.GraphicsLayoutWidget(show=True, title="Uppecut Telemetry")
    self.win.resize(1000,600)
    self.win.setWindowTitle('Uppecut Telemetry')

    self.penRedSolid = pg.mkPen(color="#F00", width=3)
    self.penRedDashed = pg.mkPen(color="#F00000", width=2, style=QtCore.Qt.DashLine)
    self.penBlueSolid = pg.mkPen(color="#00F", width=3)
    self.penBlueDashed = pg.mkPen(color="#0000F0", width=2, style=QtCore.Qt.DashLine)

    self.labelStyle = {"bold":True,  "size": "18pt"}
    self.textStyle = {"size": "18pt"}

    self.warnTemp = 29.0

    self.drawCanvas()
    self.firstPlot()

    self.index = 0

  # this function draws the canvas, does not initialize plots
  def drawCanvas(self):

    # create the three RPM plots
    self.plot_rpm_L = self.win.addPlot(title="Left RPM")
    self.plot_rpm_L.setTitle("Left RPM", **self.labelStyle)
    self.plot_rpm_W = self.win.addPlot(title="Weapon RPM")
    self.plot_rpm_W.setTitle("Weapon RPM",**self.labelStyle)
    self.plot_rpm_R = self.win.addPlot(title="Right RPM")
    self.plot_rpm_R.setTitle("Right RPM", **self.labelStyle)

    # create the three current plots
    self.win.nextRow()

    self.plot_current_L = self.win.addPlot(title="Left Current")
    self.plot_current_L.setTitle("Left Current", **self.labelStyle)
    self.plot_current_W = self.win.addPlot(title="Weapon Current")
    self.plot_current_W.setTitle("Weapon Current", **self.labelStyle)
    self.plot_current_R = self.win.addPlot(title="Right Current")
    self.plot_current_R.setTitle("Right Current", **self.labelStyle)

    self.win.nextRow()

    # create the text area
    self.textArea = self.win.addLayout(rowspan=1, colspan=3)

    self.textArea.addLabel("")
    self.textArea.addLabel("Drive Left", **self.labelStyle)
    self.textArea.addLabel("Weapon Left", **self.labelStyle)
    self.textArea.addLabel("Weapon Right", **self.labelStyle)
    self.textArea.addLabel("Drive Right ", **self.labelStyle)
    self.textArea.nextRow()

    self.textArea.addLabel("Temp:", **self.labelStyle)
    self.label_temp_DL = self.textArea.addLabel("Temp", **self.textStyle)
    self.label_temp_WL = self.textArea.addLabel("Temp", **self.textStyle)
    self.label_temp_WR = self.textArea.addLabel("Temp", **self.textStyle)
    self.label_temp_DR = self.textArea.addLabel("Temp", **self.textStyle)
    self.textArea.nextRow()

    self.textArea.addLabel("Voltage:", **self.labelStyle)
    self.label_volt_DL = self.textArea.addLabel("Volt", **self.textStyle)
    self.label_volt_WL = self.textArea.addLabel("Volt", **self.textStyle)
    self.label_volt_WR = self.textArea.addLabel("Volt", **self.textStyle)
    self.label_volt_DR = self.textArea.addLabel("Volt", **self.textStyle)
    self.textArea.nextRow()

    self.textArea.addLabel("RPM (CMD):", **self.labelStyle)
    self.label_rpm_DL = self.textArea.addLabel("RPM (CMD)", **self.textStyle)
    self.label_rpm_WL = self.textArea.addLabel("RPM (CMD)", **self.textStyle)
    self.label_rpm_WR = self.textArea.addLabel("RPM (CMD)", **self.textStyle)
    self.label_rpm_DR = self.textArea.addLabel("RPM (CMD)", **self.textStyle)
    self.textArea.nextRow()

    self.textArea.addLabel("Current (CMD):", **self.labelStyle)
    self.label_current_DL = self.textArea.addLabel("Current (CMD)", **self.textStyle)
    self.label_current_WL = self.textArea.addLabel("Current (CMD)", **self.textStyle)
    self.label_current_WR = self.textArea.addLabel("Current (CMD)", **self.textStyle)
    self.label_current_DR = self.textArea.addLabel("Current (CMD)", **self.textStyle)


  # this function inserts lines into each plot, and allocates the necessary memory
  def firstPlot(self):
    # dummy data
    t = np.array([0])

    
    # create the data arrays
    self.DL_t = t
    self.DL_rpm_val = np.sin(t)
    self.DL_rpm_cmd = 2*np.sin(t)
    self.DL_current_val = np.cos(t)
    self.DL_current_cmd = 2*np.cos(t)
    self.DL_voltage = 25.0 * np.ones_like(t)
    self.DL_temp = 28.0 * np.ones_like(t)

    self.DR_t = t
    self.DR_rpm_val = np.sin(t)
    self.DR_rpm_cmd = 2*np.sin(t)
    self.DR_current_val = np.cos(t)
    self.DR_current_cmd = 2*np.cos(t)
    self.DR_voltage = 25.0 * np.ones_like(t)
    self.DR_temp = 28.0 * np.ones_like(t)

    self.WL_t = t
    self.WL_rpm_val = np.sin(t)
    self.WL_rpm_cmd = 2*np.sin(t)
    self.WL_current_val = np.cos(t)
    self.WL_current_cmd = 2*np.cos(t)
    self.WL_voltage = 25.0 * np.ones_like(t)
    self.WL_temp = 28.0 * np.ones_like(t)

    self.WR_t = t
    self.WR_rpm_val = np.sin(t)
    self.WR_rpm_cmd = 2*np.sin(t)
    self.WR_current_val = np.cos(t)
    self.WR_current_cmd = 2*np.cos(t)
    self.WR_voltage = 25.0 * np.ones_like(t)
    self.WR_temp = 28.0 * np.ones_like(t)

    
    
    # # create the plots
    self.plot_rpm_DL_val = self.plot_rpm_L.plot(self.DL_t, self.DL_rpm_val, pen=self.penRedSolid)
    self.plot_rpm_DL_cmd = self.plot_rpm_L.plot(self.DL_t, self.DL_rpm_cmd, pen=self.penRedDashed)
    
    self.plot_rpm_WL_val = self.plot_rpm_W.plot(self.WL_t, self.WL_rpm_val, pen=self.penRedSolid)
    self.plot_rpm_WL_cmd = self.plot_rpm_W.plot(self.WL_t, self.WL_rpm_cmd, pen=self.penRedDashed)
    self.plot_rpm_WR_val = self.plot_rpm_W.plot(self.WR_t, self.WR_rpm_val, pen=self.penBlueSolid)
    self.plot_rpm_WR_cmd = self.plot_rpm_W.plot(self.WR_t, self.WR_rpm_cmd, pen=self.penBlueDashed)

    self.plot_rpm_DR_val = self.plot_rpm_R.plot(self.DR_t, self.DR_rpm_val, pen=self.penBlueSolid)
    self.plot_rpm_DR_cmd = self.plot_rpm_R.plot(self.DR_t, self.DR_rpm_cmd, pen=self.penBlueDashed)

    
    self.plot_current_DL_val = self.plot_current_L.plot(self.DL_t, self.DL_rpm_val, pen=self.penRedSolid)
    self.plot_current_DL_cmd = self.plot_current_L.plot(self.DL_t, self.DL_rpm_cmd, pen=self.penRedDashed)

    self.plot_current_WL_val = self.plot_current_W.plot(self.WL_t, self.WL_current_val,pen=self.penRedSolid)
    self.plot_current_WL_cmd = self.plot_current_W.plot(self.WL_t, self.WL_current_cmd,pen=self.penRedDashed)
    self.plot_current_WR_val = self.plot_current_W.plot(self.WR_t, self.WR_current_val ,pen=self.penBlueSolid)
    self.plot_current_WR_cmd = self.plot_current_W.plot(self.WR_t, self.WR_current_cmd, pen=self.penBlueDashed)

    self.plot_current_DR_val = self.plot_current_R.plot(self.DR_t, self.DR_current_val,pen=self.penBlueSolid)
    self.plot_current_DR_cmd = self.plot_current_R.plot(self.DR_t, self.DR_current_cmd, pen=self.penBlueDashed)

    # RESET to not have data

    self.DL_t = np.array([])
    self.DL_rpm_val =np.array([])
    self.DL_rpm_cmd = np.array([])
    self.DL_current_val =np.array([])
    self.DL_current_cmd = np.array([])
    self.DL_voltage = np.array([])
    self.DL_temp =np.array([])

    self.DR_t = np.array([])
    self.DR_rpm_val =np.array([])
    self.DR_rpm_cmd = np.array([])
    self.DR_current_val =np.array([])
    self.DR_current_cmd = np.array([])
    self.DR_voltage = np.array([])
    self.DR_temp =np.array([])

    self.WL_t = np.array([])
    self.WL_rpm_val =np.array([])
    self.WL_rpm_cmd = np.array([])
    self.WL_current_val =np.array([])
    self.WL_current_cmd = np.array([])
    self.WL_voltage = np.array([])
    self.WL_temp =np.array([])

    self.WR_t = np.array([])
    self.WR_rpm_val =np.array([])
    self.WR_rpm_cmd = np.array([])
    self.WR_current_val =np.array([])
    self.WR_current_cmd = np.array([])
    self.WR_voltage = np.array([])
    self.WR_temp =np.array([])


  def testUpdate(self):

    self.test_getData()
    self.update()

  def update(self):
    self.index += 1 

    # update plots
    self.plot_rpm_DL_val.setData(x=self.DL_t, y= self.DL_rpm_val)
    self.plot_rpm_DL_cmd.setData(x=self.DL_t, y= self.DL_rpm_cmd)
    self.plot_rpm_DR_val.setData(x=self.DR_t, y= self.DR_rpm_val)
    self.plot_rpm_DR_cmd.setData(x=self.DR_t, y= self.DR_rpm_cmd)
    self.plot_rpm_WL_val.setData(x=self.WL_t, y= self.WL_rpm_val)
    self.plot_rpm_WL_cmd.setData(x=self.WL_t, y= self.WL_rpm_cmd)
    self.plot_rpm_WR_val.setData(x=self.WR_t, y= self.WR_rpm_val)
    self.plot_rpm_WR_cmd.setData(x=self.WR_t, y= self.WR_rpm_cmd)

    self.plot_current_DL_val.setData(x=self.DL_t, y= self.DL_current_val)
    self.plot_current_DL_cmd.setData(x=self.DL_t, y= self.DL_current_cmd)
    self.plot_current_DR_val.setData(x=self.DR_t, y= self.DR_current_val)
    self.plot_current_DR_cmd.setData(x=self.DR_t, y= self.DR_current_cmd)
    self.plot_current_WL_val.setData(x=self.WL_t, y= self.WL_current_val)
    self.plot_current_WL_cmd.setData(x=self.WL_t, y= self.WL_current_cmd)
    self.plot_current_WR_val.setData(x=self.WR_t, y= self.WR_current_val)
    self.plot_current_WR_cmd.setData(x=self.WR_t, y= self.WR_current_cmd)

    # update text

    if len(self.DL_t) > 0:
        self.label_rpm_DL.setText(f"{self.DL_rpm_val[-1]: .1f} ({self.DL_rpm_cmd[-1]: .1f})")
        self.label_current_DL.setText(f"{self.DL_current_val[-1]: .1f} ({self.DL_current_cmd[-1]: .1f})")
        self.label_volt_DL.setText(f"{self.DL_voltage[-1]: .1f}")
        self.label_temp_DL.setText(f"{self.DL_temp[-1]: .1f}", color=("#000" if self.DL_temp[-1] < self.warnTemp else "#F00"))

    if len(self.DR_t) > 0:


        self.label_rpm_DR.setText(f"{self.DR_rpm_val[-1]: .1f} ({self.DR_rpm_cmd[-1]: .1f})")
        self.label_current_DR.setText(f"{self.DR_current_val[-1]: .1f} ({self.DR_current_cmd[-1]: .1f})")
        self.label_volt_DR.setText(f"{self.DR_voltage[-1]: .1f}")
        self.label_temp_DR.setText(f"{self.DR_temp[-1]: .1f}", color=("#000" if self.DR_temp[-1] < self.warnTemp else "#F00"))

    if len(self.WL_t) > 0:
        self.label_rpm_WL.setText(f"{self.WL_rpm_val[-1]: .1f} ({self.WL_rpm_cmd[-1]: .1f})")
        self.label_current_WL.setText(f"{self.WL_current_val[-1]: .1f} ({self.WL_current_cmd[-1]: .1f})")
        self.label_volt_WL.setText(f"{self.WL_voltage[-1]: .1f}")
        self.label_temp_WL.setText(f"{self.WL_temp[-1]: .1f}", color=("#000" if self.WL_temp[-1] < self.warnTemp else "#F00"))
   
    if len(self.WR_t) > 0:
        self.label_rpm_WR.setText(f"{self.WR_rpm_val[-1]: .1f} ({self.WR_rpm_cmd[-1]: .1f})")
        self.label_current_WR.setText(f"{self.WR_current_val[-1]: .1f} ({self.WR_current_cmd[-1]: .1f})")
        self.label_volt_WR.setText(f"{self.WR_voltage[-1]: .1f}")
        self.label_temp_WR.setText(f"{self.WR_temp[-1]: .1f}", color=("#000" if self.WR_temp[-1] < self.warnTemp else "#F00"))

    # this is what actually updates the plot
    self.app.processEvents()

  # insert a data point into an array
  def insertData(self, arr, d):
    
    if len(arr) < 50:
      return np.append(arr, d)
      
    arr = np.roll(arr, -1)
    arr[-1] = d
    return arr

  def insertMotorData(self, motor_id, t, rpm, rpm_cmd, current, current_cmd, voltage, temperature):

    if motor_id == "DL":
      self.DL_t           = self.insertData(self.DL_t,           t)
      self.DL_rpm_val     = self.insertData(self.DL_rpm_val,     rpm)
      self.DL_rpm_cmd     = self.insertData(self.DL_rpm_cmd,     rpm_cmd)
      self.DL_current_val = self.insertData(self.DL_current_val, current)
      self.DL_current_cmd = self.insertData(self.DL_current_cmd, current_cmd)
      self.DL_voltage     = self.insertData(self.DL_voltage,     voltage)
      self.DL_temp        = self.insertData(self.DL_temp,        temperature)

    if motor_id == "DR":
      self.DR_t           = self.insertData(self.DR_t,           t)
      self.DR_rpm_val     = self.insertData(self.DR_rpm_val,     rpm)
      self.DR_rpm_cmd     = self.insertData(self.DR_rpm_cmd,     rpm_cmd)
      self.DR_current_val = self.insertData(self.DR_current_val, current)
      self.DR_current_cmd = self.insertData(self.DR_current_cmd, current_cmd)
      self.DR_voltage     = self.insertData(self.DR_voltage,     voltage)
      self.DR_temp        = self.insertData(self.DR_temp,        temperature)

    if motor_id == "WL":
      self.WL_t           = self.insertData(self.WL_t,           t)
      self.WL_rpm_val     = self.insertData(self.WL_rpm_val,     rpm)
      self.WL_rpm_cmd     = self.insertData(self.WL_rpm_cmd,     rpm_cmd)
      self.WL_current_val = self.insertData(self.WL_current_val, current)
      self.WL_current_cmd = self.insertData(self.WL_current_cmd, current_cmd)
      self.WL_voltage     = self.insertData(self.WL_voltage,     voltage)
      self.WL_temp        = self.insertData(self.WL_temp,        temperature)

    if motor_id == "WR":
      self.WR_t           = self.insertData(self.WR_t,           t)
      self.WR_rpm_val     = self.insertData(self.WR_rpm_val,     rpm)
      self.WR_rpm_cmd     = self.insertData(self.WR_rpm_cmd,     rpm_cmd)
      self.WR_current_val = self.insertData(self.WR_current_val, current)
      self.WR_current_cmd = self.insertData(self.WR_current_cmd, current_cmd)
      self.WR_voltage     = self.insertData(self.WR_voltage,     voltage)
      self.WR_temp        = self.insertData(self.WR_temp,        temperature)


  def test_getData(self):
    
    # store data here

    t = 2*self.index*np.pi/100
    self.DL_t           = self.insertData(self.DL_t,           t)
    self.DL_rpm_val     = self.insertData(self.DL_rpm_val,     np.sin(t))
    self.DL_rpm_cmd     = self.insertData(self.DL_rpm_cmd,     2*np.sin(t))
    self.DL_current_val = self.insertData(self.DL_current_val, np.cos(t))
    self.DL_current_cmd = self.insertData(self.DL_current_cmd, 2*np.cos(t))
    self.DL_voltage     = self.insertData(self.DL_voltage,     self.DL_voltage[-1] + 0.2*np.random.randn())
    self.DL_temp        = self.insertData(self.DL_temp   ,     self.DL_temp[-1]    + 0.3*np.random.randn())

    self.DR_t           = self.insertData(self.DR_t,           t)
    self.DR_rpm_val     = self.insertData(self.DR_rpm_val,     np.cos(t))
    self.DR_rpm_cmd     = self.insertData(self.DR_rpm_cmd,     2*np.cos(t))
    self.DR_current_val = self.insertData(self.DR_current_val, np.sin(t))
    self.DR_current_cmd = self.insertData(self.DR_current_cmd, 2*np.sin(t))
    self.DR_voltage     = self.insertData(self.DR_voltage,     self.DR_voltage[-1] + 0.2*np.random.randn())
    self.DR_temp        = self.insertData(self.DR_temp   ,     self.DR_temp[-1]    + 0.3*np.random.randn())

    self.WL_t           = self.insertData(self.WL_t,           t)
    self.WL_rpm_val     = self.insertData(self.WL_rpm_val,     np.sin(t))
    self.WL_rpm_cmd     = self.insertData(self.WL_rpm_cmd,     2*np.sin(t))
    self.WL_current_val = self.insertData(self.WL_current_val, np.cos(t))
    self.WL_current_cmd = self.insertData(self.WL_current_cmd, 2*np.cos(t))
    self.WL_voltage     = self.insertData(self.WL_voltage,     self.WL_voltage[-1] + 0.2*np.random.randn())
    self.WL_temp        = self.insertData(self.WL_temp   ,     self.WL_temp[-1]    + 0.3*np.random.randn())

    self.WR_t           = self.insertData(self.WR_t,           t)
    self.WR_rpm_val     = self.insertData(self.WR_rpm_val,     np.cos(t))
    self.WR_rpm_cmd     = self.insertData(self.WR_rpm_cmd,     2*np.cos(t))
    self.WR_current_val = self.insertData(self.WR_current_val, np.sin(t))
    self.WR_current_cmd = self.insertData(self.WR_current_cmd, 2*np.sin(t))
    self.WR_voltage     = self.insertData(self.WR_voltage,     self.WR_voltage[-1] + 0.2*np.random.randn())
    self.WR_temp        = self.insertData(self.WR_temp   ,     self.WR_temp[-1]    + 0.3*np.random.randn())