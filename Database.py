import csv, datetime

class Database:
    def __init__(self, pose_x, pose_y, pose_z, latitude, longitude):
        self.columns = ["pose_x" , "pose_y" , "pose_z", "latitude" , "longitude"]
        self.pose_x = pose_x
        self.pose_y = pose_y
        self.pose_z = pose_z
        self.latitude = latitude
        self.longitude = longitude
        self.pose_z = pose_z

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, lon):
        self.longitude = lon

    def set_lat_long(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def get_latitude(self, lat):
        return lat

    def get_longitude(self, lon):
        return lon

    def set_pose_x(self, x):
        self.pose_x = x

    def set_pose_y(self, y):
        self.pose_y = y

    def set_pose_z(self, z):
        self.pose_z = z

    def set_pose(self, x, y, z):
        self.pose_x = x
        self.pose_y = y
        self.pose_z = z

    def get_pose_x(self, x):
        return x

    def get_pose_y(self, y):
        return y

    def get_pose_z(self, z):
        return z


    def create_database(self):
        # Create new CSV when server is started
        data_filename = 'data/pose_data_' + str(datetime.datetime.now()) + '.csv'
        with open(data_filename, mode='w') as data_file:
            csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(self.columns)
        return data_filename

    def write_data(self, data_filename):
        with open(data_filename, mode='a') as data_file:
            csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([self.pose_x, self.pose_y, self.pose_z, self.latitude, self.longitude])