min_apr = 0

def APR_filter(data, min_apr):
    return [item for item in data if item.get('effectiveApr', 0) > min_apr]

def APR(data):
    return data

def ltv_calculator(principleAmount, collateralAmount):
    ltv = (principleAmount / collateralAmount) * 100
    if collateralAmount == 0:
        return 0
    return ltv

def ltv_filter(datos):
    return sorted(datos,  key=lambda x: ltv_calculator(x.get('principleAmount', 0), x.get('collateralAmount', 0)))

def name(names):
    if names == '0x1B6382DBDEa11d97f24495C9A90b7c88469134a4':
        names = 'axlUSDC'
    elif names == '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83':
        names = 'WFTM'
    elif names == '0x3Fd3A0c85B70754eFc07aC9Ac0cbBDCe664865A6':
        names = 'EQUAL'
    elif names == '0xE53aFA646d48E9EF68fCd559F2a598880a3f1370':
        names = 'TOMB+'
    else:
        names = 'Uknown'
    return names





