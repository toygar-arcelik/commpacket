from enum import Enum, auto, unique

@unique
class Headers(Enum):
    DateTime = 0
    elapsedTime = auto()
    remainingTime = auto()
    phaseTime = auto()
    motorTimer = auto()
    heaterTimer = auto()
    pumpTimer = auto()
    state = auto()
    selectedProgram = auto()
    conductivityValue = auto()
    conductivityCounterCupboard = auto()
    conductivityCounterMixed = auto()
    humidityDecision = auto()
    doorSwitch = auto()
    overflowSwitch = auto()
    airtouchReed = auto()
    steamReed = auto()
    heaterTemperature = auto()
    doorTemperature = auto()
    auxilaryHeaterTemperature = auto()
    heaterNTC = auto()
    doorNTC = auto()
    voltage = auto()
    motorState = auto()
    heaterState = auto()
    hybridState = auto()
    pumpState = auto()
    T2State = auto()
    voltageState = auto()
    ledState = auto()
    DCFanState = auto()
    doorReed1 = auto()
    doorReed2 = auto()
    DrynessLevel = auto()
    LowTemp = auto()
    AntiCreasing = auto()
    err0Id = auto()
    err0Cycle = auto()
    err0prId = auto()
    err1Id = auto()
    err1Cycle = auto()
    err1prId = auto()
    bldcRPM = auto()
    bldcCurrent = auto()
    bldcByteX = auto()
    bldcReady = auto()
    bldcStatus = auto()
    bldcDirection = auto()
    CombinedErrorCnt = auto()
    CombinedErrorFlag = auto()
    CCERCnt = auto()
    SensorControlAFT = auto()
    AutoControlAFT = auto()
    ReceivedVoltage0 = auto()
    ReceivedVoltage1 = auto()
    ReceivedVoltage2 = auto()
    TEW = auto()
    VEW = auto()
    SEW = auto()
    CommPackageControl = auto()
    ApolloError = auto()
    ApolloWdtReset = auto()
    SafirConnState = auto()
    SafirSubConnState = auto()
    wifiOpened = auto()
    wifiDeviceConnected = auto()
    remoteControl = auto()
    mainVersion = auto()
    mainRevision = auto()
    parModel = auto()
    parRevision = auto()
    serviceButtonState = auto()
    serviceButtonPrevState = auto()
    serviceButtonTimeout = auto()
    airtouchTemperature = auto()
    EcoSenseState = auto()
    EcoSenseCDDCCnt0 = auto()
    EcoSenseCDDCCnt1 = auto()
    ATTryCount = auto()
    ATMagnetCount = auto()
    dummy1 = auto()
    dummy2 = auto()
    dummy3 = auto()
    dummy4 = auto()
    dummy5 = auto()