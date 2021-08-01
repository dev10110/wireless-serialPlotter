import argparse
import glob
import csv
from cobs import cobs

read_buf = [None]*256
read_buf_pos = 0

motor_data = []

motor1_data = []
motor2_data = []
motor3_data = []
motor4_data = []


if __name__=="__main__":
  # load the filename
  parser = argparse.ArgumentParser("Converts the log file to a CSV");
  parser.add_argument("--file", type=str, default="", help="file name/path to process. If not provided, processes the last file available");
  
  args = parser.parse_args()

  if args.file == "":
    files = glob.glob("LOG*****.TXT")
    print("No file name provided - using the latest file.")
    try:
      args.file = files[-1]
    except Exception as e:
      print("NO FILE FOUND - ARE YOU SURE THERE ARE FILES OF THE FORMAT 'LOG*.TXT'?")
      print("These are the files I found:")
      print(files)
      print("Here is the error message from Python:")
      print(e)
      exit()


  print("Processing File: " + args.file)

  

  with open(args.file, "rb") as f:
    while True:
      c = f.read(1)

      if c == b'':
        break

      
      if c[0] == 0:
        data = [s[0] for s in read_buf[0:read_buf_pos]]
        read_buf = [None]*256
        read_buf_pos = 0
      
        try:
          decoded = cobs.decode(bytes(data))
        except Exception as e:
          print("Decoding failed: ", e)
          continue
      
        decoded_data = [d for d in decoded]

        motor_data.append(decoded_data)

        # print(decoded_data)
      
      else:
        read_buf[read_buf_pos] = c
        read_buf_pos += 1

      if read_buf_pos > 255:
        print("read buf > 255")
        read_buf_pos = 0
        read_buf = [None]*256
        print("SOMETHING WENT WRONG - file is probably corrupted!!")

  # now write all data to the csv file

  header = ["MotorID", "RPM", "RPM_COMMAND", "CURRENT", "CURRENT_COMMAND", "VOLTAGE", "TEMPERATURE"]

  save_file = args.file[:-4] + "_ALL.csv"
  print("SAVING ALL DATA TO " + save_file)

  with open(save_file, 'w') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for d in motor_data:
      writer.writerow(d)

  print("WROTE ALL DATA")

  for i in range(4):

    save_file = args.file[:-4] + "_MOTOR_" + str(i+1) + ".csv"
    print("SAVING MOTOR " + str(i+1) + " DATA TO " + save_file)

    with open(save_file, 'w') as f:
      writer = csv.writer(f)

      writer.writerow(["INDEX"] + header)

      index = 0

      for d in motor_data:
        if d[0] == i+1:
          writer.writerow([index] + d)
        index += 1

      print("WROTE MOTOR " + str(i+1) + " DATA")






    
