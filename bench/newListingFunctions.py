from bench import app, db
from bench.models import User, Listing, Case, Memory, CPUCooler, Motherboard
from flask import render_template, request, flash, redirect
from forms import LoginForm, RegisterForm, newListingForm
from flask_login import current_user, login_user, logout_user

def processListing(request):
    print("Test")
    type = request.form.get('productType')
    price = request.form.get('productPrice')
    description = request.form.get('productDescription')
    name = request.form.get('productName')
    detailList = [type, price, description, name]

    if notNull(detailList) == False:
        return False
    if priceCheck == False:
        return False
    if(type == "Case"):
        if(processCase(detailList, request) == False):
            return False
    elif(type == "Memory"):
        if(processMemory(detailList,request) == False):
            return False
    elif(type == "CPU Cooler"):
            if(processCPUCooler(detailList,request) == False):
                return False
    elif(type == "Motherboard"):
                if(processMotherBoard(detailList,request) == False):
                    return False
    return True

def priceCheck(price):
    if(price.isdigit() == False or int(price) < 0):
        return False
    else:
        return True
def notNull(detailList):
     for detail in detailList:
        if detail == "":
            return False

def processCase(detailList, request):
    manufacturer = request.form.get('Manufacturer')
    print("Manufacturer: " + manufacturer)
    Colour = request.form.get('CaseColour')
    SidePanel = request.form.get('SidePanel')
    Bays25 = request.form.get('2.5Bays')
    Bays35 = request.form.get('3.5Bays')
    if(manufacturer == ""):
        return False
    if(Bays25.isdigit() == False or Bays35.isdigit() == False):
        return False
    Bays25 = int(Bays25)
    Bays35 = int(Bays35)
    
    listing = Listing(ListingName=detailList[3],ListingPrice=detailList[1],
    ListingType=detailList[0],ListingDescription=detailList[2],
    userId=current_user.id )
    db.session.add(listing)
    db.session.commit()
    listingID = listing.id
    
    case = Case(manufacturer=manufacturer,colour=Colour,sidePanel=SidePanel,
     internal25Bays=Bays25,internal35Bays=Bays35, caseListing=listingID)
    db.session.add(case)
    db.session.commit()

def processMemory(detailList,request):
    print("Memory")
    manufacturer = request.form.get('Manufacturer')
    memoryType = request.form.get('MemoryType')
    memorySpeed = request.form.get('RAMSpeed')
    modules = request.form.get('Modules')
    colour = request.form.get('RAMColour')

    if(manufacturer == ""):
        return False
    if(modules.isdigit() == False or memorySpeed.isdigit() == False):
        return False
    modules = int(modules)
    memorySpeed = int(memorySpeed)
    
    listing = Listing(ListingName=detailList[3],ListingPrice=detailList[1],
    ListingType=detailList[0],ListingDescription=detailList[2],
    userId=current_user.id)
    db.session.add(listing)
    db.session.commit()
    id_ = listing.id

    memory = Memory(manufacturer=manufacturer,colour=colour,memoryType=memoryType, speed=memorySpeed, modules=modules, memoryListing=id_)
    db.session.add(memory)
    db.session.commit()

def processCPUCooler(detailList,request):
    print("COol")
    manufacturer = request.form.get('Manufacturer')
    RPM = request.form.get('Fan RPM')
    Noise = request.form.get('Fan Noise Level')
    Height = request.form.get('Cooler Height')
    Socket = request.form.get('Socket')
    WaterCooled = request.form.get('WaterCooled')
    Fanless = request.form.get('Fanless')
    if(manufacturer == ""):
            return False
    if(Height.isdigit() == False or Noise.isdigit() == False or RPM.isdigit() == False):
            return False
    Height = int(Height)
    Noise = int(Noise)
    RPM = int(RPM)

    listing = Listing(ListingName=detailList[3],ListingPrice=detailList[1],
    ListingType=detailList[0],ListingDescription=detailList[2],
    userId=current_user.id)
    db.session.add(listing)
    db.session.commit()
    id_ = listing.id

    Cooler = CPUCooler(manufacturer=manufacturer,FanRPM=RPM, NoiseLevel=Noise, Height=Height, WaterCooled=WaterCooled, Fanless=Fanless, CPUCoolerListing=id_)
    db.session.add(Cooler)
    db.session.commit()

def processMotherBoard(detailList, request):
    print("Motherboard")
    manufacturer = request.form.get('Manufacturer')
    Socket = request.form.get('Socket')
    RamSlots = request.form.get('RAMSlots')
    MaxRam = request.form.get('RAMMax')
    colour = request.form.get('Colour')
    Chipset = request.form.get('Chipset')
    MemoryType = request.form.get('MemoryType')
    SLI = request.form.get('SLI')
    CrossFire = request.form.get('CrossFire')
    x16 = request.form.get('x16')
    x8 = request.form.get('x8')
    x4 = request.form.get('x4')
    x1 = request.form.get('x1')
    PCI = request.form.get('PCI')
    SATA = request.form.get('SATA')
    mSATA = request.form.get('mSATA')
    M2 = request.form.get('M.2')
    USB3 = request.form.get('USB3')
    WiFi = request.form.get('WiFi')
    RAID = request.form.get('RAID')
    IntegerDetailList = [RamSlots, MaxRam, x16, x8, x4, x1, PCI, SATA, mSATA, M2 ]
    OtherDetailList = [MemoryType,SLI, CrossFire,USB3,WiFi,RAID]
    if(manufacturer == ""):
            return False
    for i in range(len(IntegerDetailList)):
        if(IntegerDetailList[i] == "" or IntegerDetailList[i] == None):
            IntegerDetailList[i] = 0
        if(str(IntegerDetailList[i]).isdigit() == False):
            return False
        print(IntegerDetailList[i])
    for i in range(len(OtherDetailList)):
        if(OtherDetailList[i] == "Choose..."):
            OtherDetailList[i] = ""

    listing = Listing(ListingName=detailList[3],ListingPrice=detailList[1],
    ListingType=detailList[0],ListingDescription=detailList[2],
    userId=current_user.id)
    db.session.add(listing)
    db.session.commit()
    id_ = listing.id

    MotherBoard = Motherboard(manufacturer=manufacturer, Socket=Socket, RAMslots=IntegerDetailList[0],
     MaxRAM=IntegerDetailList[1], colour=colour, Chipset=Chipset, MemoryType=OtherDetailList[0],
     SLISupport=OtherDetailList[1], CrossFireSupport=OtherDetailList[2],PCIEx16Slots=IntegerDetailList[2],
     PCIEx8Slots=IntegerDetailList[3],PCIEx4Slots=IntegerDetailList[4],PCIEx1Slots=IntegerDetailList[5],
     PCISlots=IntegerDetailList[6], SATAPorts=IntegerDetailList[7], M2Slots=IntegerDetailList[9], mSata=IntegerDetailList[8],
     OnboardUSB3Headers=OtherDetailList[3],OnboardWifi=OtherDetailList[4],
     RAIDSupport=OtherDetailList[5],MotherboardListing=id_
     )
    db.session.add(MotherBoard)
    db.session.commit()