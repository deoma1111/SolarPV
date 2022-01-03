
create table Location(
locationID int auto_increment primary key,
address1 varchar(255),
address2 varchar(50),
city varchar(50),
state varchar (50),
country varchar(50),
phone varchar(10),
fax varchar(10),
clientID int,
foreign key(clientID) references Client(clientID)
);

create table TestStandard(
standardID int auto_increment primary key,
standardName varchar(50),
description varchar(255),
publishedDate date
);

create table TestSequence(
sequenceID int auto_increment primary key,
sequenceName varchar(50)
);
create table Service(
serviceID int auto_increment primary key,
serviceName varchar(50),
description varchar(255),
isF1Required varchar(3),
F1Frequency float,
standardID int,
foreign key(standardID) references TestStandard(standardID)
);

create table Product(
modelNumber varchar(10) primary key,
productName varchar (20),
cellTechnology varchar(10),
cellManufacturer varchar(10),
numberofCells int,
numberofCellsinSeries int,
numberofSeriesStrings int,
numberofDiode int,
productLength float,
productWidth float,
productWeight float,
superStateType varchar(20),
superStateManufacturer varchar(20),
substrateType varchar(20),
substrateManufacturer varchar(20),
frameType varchar(20),
frameAdhesive varchar(20),
encapsulateType varchar(20),
encapsulantManufacturer varchar(20),
junctionBoxType varchar(20),
junctionBoxManufacturer varchar(20)
);

create table PerformanceData(
modelNumber varchar(10),
sequenceID int,
maxSystemVoltage float,
voc float,
isc float,
vmp float,
imp float,
pmp float,
ff float,
foreign key(modelNumber) references Product(modelNumber),
foreign key(sequenceID) references TestSequence(sequenceID),
primary key(modelNumber, sequenceID)
);

create table Certificate(
certNumber int auto_increment primary key,
certID int,
userID int,
reportNumber int,
issueDate date,
standardID int,
locationID int,
modelNumber varchar(10),
foreign key(userID) references User(userID),
foreign key(standardID) references TestStandard(standardID),
foreign key(locationID) references Location(locationID),
foreign key(modelNumber) references Product(modelNumber)
);