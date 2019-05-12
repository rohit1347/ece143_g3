#%%
import xlrd

### need to be added

##from pandas import ExcelFile
##import pandas as pd

###end

####using panda
#excel_file = '2017-APTA-Fact-Book-Appendix-B.xlsx'
#movies = pd.read_excel('2017-APTA-Fact-Book-Appendix-B.xlsx')

####end

workbook = xlrd.open_workbook('2017-APTA-Fact-Book-Appendix-B.xlsx')

worksheet = workbook.sheet_by_name('Agency by Mode')#open a sheet

print(worksheet.cell(0, 0).value)#print the row(0,0)value of a particular sheet
#%%
#California
UZA_POP_AG_SD = []
UZA_POP_AG_SF = []
UZA_POP_AG_LA = []

UZA_POP_AR_SD = []
UZA_POP_AR_SF = []
UZA_POP_AR_LA = []

UZA_POP_CC_SD = []
UZA_POP_CC_SF = []
UZA_POP_CC_LA = []

UZA_POP_CR_SD = []
UZA_POP_CR_SF = []
UZA_POP_CR_LA = []

UZA_POP_DR_SD = []
UZA_POP_DR_SF = []
UZA_POP_DR_LA = []

UZA_POP_FB_SD = []
UZA_POP_FB_SF = []
UZA_POP_FB_LA = []

UZA_POP_HR_SD = []
UZA_POP_HR_SF = []
UZA_POP_HR_LA = []

UZA_POP_IP_SD = []
UZA_POP_IP_SF = []
UZA_POP_IP_LA = []

UZA_POP_LR_SD = []
UZA_POP_LR_SF = []
UZA_POP_LR_LA = []

UZA_POP_MB_SD = []
UZA_POP_MB_SF = []
UZA_POP_MB_LA = []

UZA_POP_MO_SD = []
UZA_POP_MO_SF = []
UZA_POP_MO_LA = []

UZA_POP_PB_SD = []
UZA_POP_PB_SF = []
UZA_POP_PB_LA = []

UZA_POP_TB_SD = []
UZA_POP_TB_SF = []
UZA_POP_TB_LA = []

UZA_POP_VP_SD = []
UZA_POP_VP_SF = []
UZA_POP_VP_LA = []
#Washiongton
UZA_POP_AG_SEA = []
UZA_POP_AR_SEA = []
UZA_POP_CC_SEA = []
UZA_POP_CR_SEA = []
UZA_POP_DR_SEA = []
UZA_POP_FB_SEA = []
UZA_POP_HR_SEA = []
UZA_POP_IP_SEA = []
UZA_POP_LR_SEA = []
UZA_POP_MB_SEA = []
UZA_POP_MO_SEA = []
UZA_POP_PB_SEA = []
UZA_POP_TB_SEA = []
UZA_POP_VP_SEA = []
#Taxas
UZA_POP_AG_AUS = []
UZA_POP_AG_HOU = []
UZA_POP_AG_DAL = []

UZA_POP_AR_AUS = []
UZA_POP_AR_HOU = []
UZA_POP_AR_DAL = []

UZA_POP_CC_AUS = []
UZA_POP_CC_HOU = []
UZA_POP_CC_DAL = []

UZA_POP_CR_AUS = []
UZA_POP_CR_HOU = []
UZA_POP_CR_DAL = []

UZA_POP_DR_AUS = []
UZA_POP_DR_HOU = []
UZA_POP_DR_DAL = []

UZA_POP_FB_AUS = []
UZA_POP_FB_HOU = []
UZA_POP_FB_DAL = []

UZA_POP_HR_AUS = []
UZA_POP_HR_HOU = []
UZA_POP_HR_DAL = []

UZA_POP_IP_AUS = []
UZA_POP_IP_HOU = []
UZA_POP_IP_DAL = []

UZA_POP_LR_AUS = []
UZA_POP_LR_HOU = []
UZA_POP_LR_DAL = []

UZA_POP_MB_AUS = []
UZA_POP_MB_HOU = []
UZA_POP_MB_DAL = []

UZA_POP_MO_AUS = []
UZA_POP_MO_HOU = []
UZA_POP_MO_DAL = []

UZA_POP_PB_AUS = []
UZA_POP_PB_HOU = []
UZA_POP_PB_DAL = []

UZA_POP_TB_AUS = []
UZA_POP_TB_HOU = []
UZA_POP_TB_DAL = []

UZA_POP_VP_AUS = []
UZA_POP_VP_HOU = []
UZA_POP_VP_DAL = []
#NewYork
UZA_POP_AG_NY = []
UZA_POP_AR_NY = []
UZA_POP_CC_NY = []
UZA_POP_CR_NY = []
UZA_POP_DR_NY = []
UZA_POP_FB_NY = []
UZA_POP_HR_NY = []
UZA_POP_IP_NY = []
UZA_POP_LR_NY = []
UZA_POP_MB_NY = []
UZA_POP_MO_NY = []
UZA_POP_PB_NY = []
UZA_POP_TB_NY = []
UZA_POP_VP_NY = []
#illinois
UZA_POP_AG_CHI = []
UZA_POP_AR_CHI = []
UZA_POP_CC_CHI = []
UZA_POP_CR_CHI = []
UZA_POP_DR_CHI = []
UZA_POP_FB_CHI = []
UZA_POP_HR_CHI = []
UZA_POP_IP_CHI = []
UZA_POP_LR_CHI = []
UZA_POP_MB_CHI = []
UZA_POP_MO_CHI = []
UZA_POP_PB_CHI = []
UZA_POP_TB_CHI = []
UZA_POP_VP_CHI = []
#Michigan
UZA_POP_AG_DET = []
UZA_POP_AR_DET = []
UZA_POP_CC_DET = []
UZA_POP_CR_DET = []
UZA_POP_DR_DET = []
UZA_POP_FB_DET = []
UZA_POP_HR_DET = []
UZA_POP_IP_DET = []
UZA_POP_LR_DET = []
UZA_POP_MB_DET = []
UZA_POP_MO_DET = []
UZA_POP_PB_DET = []
UZA_POP_TB_DET = []
UZA_POP_VP_DET = []

#Geogia
UZA_POP_AG_ATL = []
UZA_POP_AR_ATL = []
UZA_POP_CC_ATL = []
UZA_POP_CR_ATL = []
UZA_POP_DR_ATL = []
UZA_POP_FB_ATL = []
UZA_POP_HR_ATL = []
UZA_POP_IP_ATL = []
UZA_POP_LR_ATL = []
UZA_POP_MB_ATL = []
UZA_POP_MO_ATL = []
UZA_POP_PB_ATL = []
UZA_POP_TB_ATL = []
UZA_POP_VP_ATL = []

#Florida
UZA_POP_AG_MIA = []
UZA_POP_AG_ORL = []

UZA_POP_AR_MIA = []
UZA_POP_AR_ORL = []

UZA_POP_CC_MIA = []
UZA_POP_CC_ORL = []

UZA_POP_CR_MIA = []
UZA_POP_CR_ORL = []

UZA_POP_DR_MIA = []
UZA_POP_DR_ORL = []

UZA_POP_FB_MIA = []
UZA_POP_FB_ORL = []

UZA_POP_HR_MIA = []
UZA_POP_HR_ORL = []

UZA_POP_IP_MIA = []
UZA_POP_IP_ORL = []

UZA_POP_LR_MIA = []
UZA_POP_LR_ORL = []

UZA_POP_MB_MIA = []
UZA_POP_MB_ORL = []

UZA_POP_MO_MIA = []
UZA_POP_MO_ORL = []

UZA_POP_PB_MIA = []
UZA_POP_PB_ORL = []

UZA_POP_TB_MIA = []
UZA_POP_TB_ORL = []

UZA_POP_VP_MIA = []
UZA_POP_VP_ORL = []
#Arizonia
UZA_POP_AG_PHX = []
UZA_POP_AR_PHX = []
UZA_POP_CC_PHX = []
UZA_POP_CR_PHX = []
UZA_POP_DR_PHX = []
UZA_POP_FB_PHX = []
UZA_POP_HR_PHX = []
UZA_POP_IP_PHX = []
UZA_POP_LR_PHX = []
UZA_POP_MB_PHX = []
UZA_POP_MO_PHX = []
UZA_POP_PB_PHX = []
UZA_POP_TB_PHX = []
UZA_POP_VP_PHX = []
#PENN
UZA_POP_AG_PHI = []
UZA_POP_AG_PIT = []

UZA_POP_AR_PHI = []
UZA_POP_AR_PIT = []

UZA_POP_CC_PHI = []
UZA_POP_CC_PIT = []

UZA_POP_CR_PHI = []
UZA_POP_CR_PIT = []

UZA_POP_DR_PHI = []
UZA_POP_DR_PIT = []

UZA_POP_FB_PHI = []
UZA_POP_FB_PIT = []

UZA_POP_HR_PHI = []
UZA_POP_HR_PIT = []

UZA_POP_IP_PHI = []
UZA_POP_IP_PIT = []

UZA_POP_LR_PHI = []
UZA_POP_LR_PIT = []

UZA_POP_MB_PHI = []
UZA_POP_MB_PIT = []

UZA_POP_MO_PHI = []
UZA_POP_MO_PIT = []

UZA_POP_PB_PHI = []
UZA_POP_PB_PIT = []

UZA_POP_TB_PHI = []
UZA_POP_TB_PIT = []

UZA_POP_VP_PHI = []
UZA_POP_VP_PIT = []
#WISCONSIN
UZA_POP_AG_MAD = []
UZA_POP_AG_MIL = []

UZA_POP_AR_MAD = []
UZA_POP_AR_MIL = []

UZA_POP_CC_MAD = []
UZA_POP_CC_MIL = []

UZA_POP_CR_MAD = []
UZA_POP_CR_MIL = []

UZA_POP_DR_MAD = []
UZA_POP_DR_MIL = []

UZA_POP_FB_MAD = []
UZA_POP_FB_MIL = []

UZA_POP_HR_MAD = []
UZA_POP_HR_MIL = []

UZA_POP_IP_MAD = []
UZA_POP_IP_MIL = []

UZA_POP_LR_MAD = []
UZA_POP_LR_MIL = []

UZA_POP_MB_MAD = []
UZA_POP_MB_MIL = []

UZA_POP_MO_MAD = []
UZA_POP_MO_MIL = []

UZA_POP_PB_MAD = []
UZA_POP_PB_MIL = []

UZA_POP_TB_MAD = []
UZA_POP_TB_MIL = []

UZA_POP_VP_MAD = []
UZA_POP_VP_MIL = []
#CORONADO
UZA_POP_AG_DEN = []
UZA_POP_AR_DEN = []
UZA_POP_CC_DEN = []
UZA_POP_CR_DEN = []
UZA_POP_DR_DEN = []
UZA_POP_FB_DEN = []
UZA_POP_HR_DEN = []
UZA_POP_IP_DEN = []
UZA_POP_LR_DEN = []
UZA_POP_MB_DEN = []
UZA_POP_MO_DEN = []
UZA_POP_PB_DEN = []
UZA_POP_TB_DEN = []
UZA_POP_VP_DEN = []
#NEVADA
UZA_POP_AG_LV = []
UZA_POP_AR_LV = []
UZA_POP_CC_LV = []
UZA_POP_CR_LV = []
UZA_POP_DR_LV = []
UZA_POP_FB_LV = []
UZA_POP_HR_LV = []
UZA_POP_IP_LV = []
UZA_POP_LR_LV = []
UZA_POP_MB_LV = []
UZA_POP_MO_LV = []
UZA_POP_PB_LV = []
UZA_POP_TB_LV = []
UZA_POP_VP_LV = []

#utah
UZA_POP_AG_SALT = []
UZA_POP_AR_SALT = []
UZA_POP_CC_SALT = []
UZA_POP_CR_SALT = []
UZA_POP_DR_SALT = []
UZA_POP_FB_SALT = []
UZA_POP_HR_SALT = []
UZA_POP_IP_SALT = []
UZA_POP_LR_SALT = []
UZA_POP_MB_SALT = []
UZA_POP_MO_SALT = []
UZA_POP_PB_SALT = []
UZA_POP_TB_SALT = []
UZA_POP_VP_SALT = []



for i in range(1845):
    if worksheet.cell(i,2).value == 'San Diego':
        SD = (worksheet.cell(i, 4).value)        
    elif worksheet.cell(i,2).value == 'San Francisco':
        SF = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Los Angeles':
        LA = (worksheet.cell(i, 4).value)
    
    elif worksheet.cell(i,2).value == 'Seattle':
        SEA = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Austin':
        AUS = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Houston':
        HOU = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Dallas':
        DAL = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'New York':
        NY = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Chicago':
        CHI = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Detroit':
        DET = (worksheet.cell(i, 4).value)
        
    elif worksheet.cell(i,2).value == 'Atlanta':
        ATL = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Miami':
        MIA = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Orlando':
        ORL = (worksheet.cell(i, 4).value)

    elif worksheet.cell(i,2).value == 'Phoenix':
        PHX = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Philadelphia':
        PHI = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Pittsburgh':
        PIT = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Madison':
        MAD = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Milwaukee':
        MIL = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Denver':
        DEN = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Las Vegas':
        LV = (worksheet.cell(i, 4).value)
    elif worksheet.cell(i,2).value == 'Salt Lake City':
        SALT = (worksheet.cell(i, 4).value)

dict_POP = {
    "San Diego":SD,
    "San Francisco":SF,
    "Los Angeles":LA,
    "Seattle":SEA,
    "Austin":AUS,
    "Houston":HOU,
    "Dallas":DAL,
    "New York":NY,
    "Chicaco":CHI,
    "Detroit":DET,
    "Atlanta":ATL,
    "Miami":MIA,
    "Orlando":ORL,
    "Phoenix":PHX,
    "Philadelphia":PHI,
    "Pittsburgh":PIT,
    "Madison":MAD,
    "Milwaukee":MIL,
    "Denver":DEN,
    "Las Vegas":LV,
    "Salt Lake City":SALT
}

CityName = list(dict_POP.keys())
print(dict_POP)
print(CityName)

    


