
import copy
from ..Script import Script
from UM.Resources import Resources
import pickle
import os
from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog('cura')

class AdvertWordPara:
    __qualname__ = 'AdvertWordPara'
    
    def __init__(self):
        self.enableCutInfill = False
        self.cutInfillHeight = 20
        self.cutInfillLayerNr = 4
        self.enableSwitchFilamentBackward = True
        self.enableSwitchFilamentHome = False
        self.switchFilamentReduceSpeed = False
        self.reduceSpeedRatio = 50
        self.reduceSpeedELength = 20
        self.homeDelay = 0
        self.backwardLength = 43
        self.backwardSpeed = 80
        self.forwardLength = 43
        self.forwardSpeed = 100
        self.layer0 = True
        self.z_ratio0 = 0
        self.extrude_ratio0 = 'Extruder1'
        self.layer1 = False
        self.z_ratio1 = 20
        self.extrude_ratio1 = 'Extruder2'
        self.layer2 = False
        self.z_ratio2 = 30
        self.extrude_ratio2 = 'Extruder1'
        self.layer3 = False
        self.z_ratio3 = 40
        self.extrude_ratio3 = 'Extruder2'
        self.layer4 = False
        self.z_ratio4 = 60
        self.extrude_ratio4 = 'Extruder1'
        self.layer5 = False
        self.z_ratio5 = 80
        self.extrude_ratio5 = 'Extruder2'
        pkFile = os.path.join(os.path.join(Resources.getStoragePath(Resources.Resources), 'plugins'), 'AdvertWord')
        if os.path.exists(pkFile):
            
            try:
                _pkDat = pickle.load(open(pkFile, 'rb'))
            except:
                None
                _pkDat = None

            if isinstance(_pkDat, AdvertWordPara):
                i = self.__dict__
                for key in self.__dict__.keys():
                    if not isinstance(getattr(self, key), float) and isinstance(getattr(self, key), bool) and isinstance(getattr(self, key), str):
                        if isinstance(getattr(self, key), int) and key in _pkDat.__dict__.keys() and type(getattr(self, key)) == type(getattr(_pkDat, key)):
                            setattr(self, key, getattr(_pkDat, key))
                        return None



class AdvertWord(Script):
    __qualname__ = 'AdvertWord'
    
    def __init__(self):
        super().__init__()

    
    def getSettingDataString(self):
        if not hasattr(self, 'initDone'):
            self.initDone = True
            self.para = AdvertWordPara()
        rtDat = '{' \
                '            "name":"广告字双色换色V0.1",' \
                '            "key": "AdvertWord",' \
                '            "metadata": {},' \
                '            "version": 2,' \
                '            "settings":' \
                '            {' \
                '            ' \
                '                "CutInfill":' \
                '                {' \
                '                    "label":"*截留填充",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "CutInfillHeight":' \
                '                {' \
                '                    "label": "    截留高度   ",' \
                '                    "description": "",' \
                '                    "unit": "mm",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200000",' \
                '                    "enabled": "CutInfill"' \
                '                },' \
                '                "CutInfillLayerNr":' \
                '                {' \
                '                    "label": "    截留层数   ",' \
                '                    "description": "",' \
                '                    "unit": "层",' \
                '                    "type": "int",' \
                '                    "default_value": %d,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200000",' \
                '                    "enabled": "CutInfill"' \
                '                },' \
                '                ' \
                '                "SwitchFilamentBackward":' \
                '                {' \
                '                    "label":"*换色时进退料使能",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "SwitchFilamentHome":' \
                '                {' \
                '                    "label":"    换色后是否归零",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s,' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "HomeDelay":' \
                '                {' \
                '                    "label": "       归零后延时   ",' \
                '                    "description": "",' \
                '                    "unit": "s",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200",' \
                '                    "enabled": "SwitchFilamentHome and SwitchFilamentBackward"' \
                '                },' \
                '                ' \
                '                "SwitchFilamentReduceSpeed":' \
                '                {' \
                '                    "label":"    换色时是否减速",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s,' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "ReduceSpeedRatio":' \
                '                {' \
                '                    "label": "       减速至   ",' \
                '                    "description": "",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.5",' \
                '                    "maximum_value_warning": "110",' \
                '                    "enabled": "SwitchFilamentReduceSpeed and SwitchFilamentBackward"' \
                '                },' \
                '                "ReduceSpeedELength":' \
                '                {' \
                '                    "label": "       恢复速度当E挤出   ",' \
                '                    "description": "",' \
                '                    "unit": "mm",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "1000",' \
                '                    "enabled": "SwitchFilamentReduceSpeed and SwitchFilamentBackward"' \
                '                },' \
                '                ' \
                '                "BackwardLength":' \
                '                {' \
                '                    "label": "    退料长度   ",' \
                '                    "description": "",' \
                '                    "unit": "mm",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200",' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "BackwardSpeed":' \
                '                {' \
                '                    "label": "       退料速度   ",' \
                '                    "description": "",' \
                '                    "unit": "mm/s",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200",' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "ForwardLength":' \
                '                {' \
                '                    "label": "    进料长度   ",' \
                '                    "description": "",' \
                '                    "unit": "mm",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200",' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "ForwardSpeed":' \
                '                {' \
                '                    "label": "       进料速度   ",' \
                '                    "description": "",' \
                '                    "unit": "mm/s",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "200",' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
                '                "Layer0":' \
                '                {' \
                '                    "label":"*初始层",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio0":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer0"' \
                '                },' \
                '                "Extrude_ratio0":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer0"' \
                '                },' \
                '                "Layer1":' \
                '                {' \
                '                    "label": "换色层1",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio1":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer1"' \
                '                },' \
                '                "Extrude_ratio1":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer1"' \
                '                },' \
                '                "Layer2":' \
                '                {' \
                '                    "label": "换色层2",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio2":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer2"' \
                '                },' \
                '                "Extrude_ratio2":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                   "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer2"' \
                '                },' \
                '                ' \
                '                "Layer3":' \
                '                {' \
                '                    "label": "换色层3",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio3":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer3"' \
                '                },' \
                '                "Extrude_ratio3":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer3"' \
                '                },' \
                '                "Layer4":' \
                '                {' \
                '                    "label": "换色层4",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio4":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer4"' \
                '                },' \
                '                "Extrude_ratio4":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer4"' \
                '                },' \
                '                "Layer5":' \
                '                {' \
                '                    "label": "换色层5",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio5":' \
                '                {' \
                '                    "label": "    Z高度(该位置换喷头)   ",' \
                '                    "description": "height ratio (0 - 100)",' \
                '                    "unit": "%%",' \
                '                    "type": "float",' \
                '                    "default_value": %f,' \
                '                    "minimum_value": "0",' \
                '                    "minimum_value_warning": "0.0",' \
                '                    "maximum_value_warning": "100",' \
                '                    "enabled": "Layer5"' \
                '                },' \
                '                "Extrude_ratio5":' \
                '                {' \
                '                    "label": "    挤出头选择    ",' \
                '                    "description": "Select Extruder",' \
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer5"' \
                '                }' \
                '            }' \
                '        }' % (str(self.para.enableCutInfill).lower(), self.para.cutInfillHeight, self.para.cutInfillLayerNr, str(self.para.enableSwitchFilamentBackward).lower(), str(self.para.enableSwitchFilamentHome).lower(), self.para.homeDelay, str(self.para.switchFilamentReduceSpeed).lower(), self.para.reduceSpeedRatio, self.para.reduceSpeedELength, self.para.backwardLength, self.para.backwardSpeed, self.para.forwardLength, self.para.forwardSpeed, str(self.para.layer0).lower(), self.para.z_ratio0, self.para.extrude_ratio0, str(self.para.layer1).lower(), self.para.z_ratio1, self.para.extrude_ratio1, str(self.para.layer2).lower(), self.para.z_ratio2, self.para.extrude_ratio2, str(self.para.layer3).lower(), self.para.z_ratio3, self.para.extrude_ratio3, str(self.para.layer4).lower(), self.para.z_ratio4, self.para.extrude_ratio4, str(self.para.layer5).lower(), self.para.z_ratio5, self.para.extrude_ratio5)
        return rtDat

    
    def getHeight(self, dat):
        
        try:
            global totalLayer
            totalLayer = -1
            height = 0.0
            prepareEndFlag = False
            done = False
            for layerDat in dat:
                lines = layerDat.split('\n')
                for line in lines:
                    if line.endswith(';End of Gcode'):
                        done = True
                        break
                    if line:
                        code = self.getValue(line, 'G', None)
                        if code == 1 : #or code == 0 现在的切片G1 是一开始的移动，打印途中的换层用的G0 所以这里要把G1的排除掉
                            continue
                        height = self.getValue(line, 'Z', height)
                    if line.startswith(';LAYER_COUNT:'):
                        totalLayer = int(self.getValue(line, ';LAYER_COUNT:', totalLayer))
                    elif line.startswith(';End of Gcode'):
                        done = True
                        break
                    elif line.startswith(';LAYER:'):
                        if int(self.getValue(line, ';LAYER:', 0)) == totalLayer - 1:
                            prepareEndFlag = True
                    else:
                        if prepareEndFlag:
                            done = True
                            break

                if done:
                    break
            return round(float(height),2)
        except Exception as e:
            print(e)
            return 0.0




                


    
    def getCurrentPara(self):
        self.para.enableCutInfill = self.getSettingValueByKey('CutInfill')
        self.para.cutInfillHeight = self.getSettingValueByKey('CutInfillHeight')
        self.para.cutInfillLayerNr = int(self.getSettingValueByKey('CutInfillLayerNr'))
        self.para.enableSwitchFilamentBackward = self.getSettingValueByKey('SwitchFilamentBackward')
        self.para.enableSwitchFilamentHome = self.getSettingValueByKey('SwitchFilamentHome')
        self.para.homeDelay = self.getSettingValueByKey('HomeDelay')
        self.para.switchFilamentReduceSpeed = self.getSettingValueByKey('SwitchFilamentReduceSpeed')
        self.para.reduceSpeedRatio = self.getSettingValueByKey('ReduceSpeedRatio')
        self.para.reduceSpeedELength = self.getSettingValueByKey('ReduceSpeedELength')
        self.para.backwardLength = self.getSettingValueByKey('BackwardLength')
        self.para.backwardSpeed = self.getSettingValueByKey('BackwardSpeed')
        self.para.forwardLength = self.getSettingValueByKey('ForwardLength')
        self.para.forwardSpeed = self.getSettingValueByKey('ForwardSpeed')
        self.para.layer0 = self.getSettingValueByKey('Layer0')
        self.para.z_ratio0 = self.getSettingValueByKey('Z_ratio0')
        self.para.extrude_ratio0 = self.getSettingValueByKey('Extrude_ratio0')
        self.para.layer1 = self.getSettingValueByKey('Layer1')
        self.para.z_ratio1 = self.getSettingValueByKey('Z_ratio1')
        self.para.extrude_ratio1 = self.getSettingValueByKey('Extrude_ratio1')
        self.para.layer2 = self.getSettingValueByKey('Layer2')
        self.para.z_ratio2 = self.getSettingValueByKey('Z_ratio2')
        self.para.extrude_ratio2 = self.getSettingValueByKey('Extrude_ratio2')
        self.para.layer3 = self.getSettingValueByKey('Layer3')
        self.para.z_ratio3 = self.getSettingValueByKey('Z_ratio3')
        self.para.extrude_ratio3 = self.getSettingValueByKey('Extrude_ratio3')
        self.para.layer4 = self.getSettingValueByKey('Layer4')
        self.para.z_ratio4 = self.getSettingValueByKey('Z_ratio4')
        self.para.extrude_ratio4 = self.getSettingValueByKey('Extrude_ratio4')
        self.para.layer5 = self.getSettingValueByKey('Layer5')
        self.para.z_ratio5 = self.getSettingValueByKey('Z_ratio5')
        self.para.extrude_ratio5 = self.getSettingValueByKey('Extrude_ratio5')

    
    def savePara(self):
        self.getCurrentPara()
        pkFile = os.path.join(os.path.join(Resources.getStoragePath(Resources.Resources), 'plugins'), 'AdvertWord.pk')
        print('pkFile:', pkFile)
        pickle.dump(self.para, open(pkFile, 'wb'))

    
    def _get_ratio(self, s):
        if s == 'Extruder1':
            return 0
        if s == 'Extruder2':
            return 1
        return None

    
    def execute(self, data):
        paraList = []
        self.getCurrentPara()
        if self.para.layer0:
            paraList.append((self.para.z_ratio0 / 100, self._get_ratio(self.para.extrude_ratio0), 0))
        if self.para.layer1:
            paraList.append((self.para.z_ratio1 / 100, self._get_ratio(self.para.extrude_ratio1), 0))
        if self.para.layer2:
            paraList.append((self.para.z_ratio2 / 100, self._get_ratio(self.para.extrude_ratio2), 0))
        if self.para.layer3:
            paraList.append((self.para.z_ratio3 / 100, self._get_ratio(self.para.extrude_ratio3), 0))
        if self.para.layer4:
            paraList.append((self.para.z_ratio4 / 100, self._get_ratio(self.para.extrude_ratio4), 0))
        if self.para.layer5:
            paraList.append((self.para.z_ratio5 / 100, self._get_ratio(self.para.extrude_ratio5), 0))
        index = -1
        height = 0
        height_list = []
        ratio_list = []
        b_gradient_list = []
        if height == 0:
            height = self.getHeight(data)
        print("paraList:",paraList)
        print("height:",height)
        print('-----------list start---------------------')
        
        def item_in_list(list, item):
            try:
                return list.index(item) >= 0
            except:
                return 0
        for (Z_ratio, extrude_ratio, b_gradient) in paraList:
            if item_in_list(height_list, Z_ratio * height) == 0:
                height_list.append(Z_ratio * height)
                ratio_list.append(extrude_ratio)
                b_gradient_list.append(int(b_gradient))
                continue
            ratio_list[height_list.index(Z_ratio * height)] = extrude_ratio
            b_gradient_list[height_list.index(Z_ratio * height)] = int(b_gradient)
        
        if item_in_list(height_list, 0) == 0:#最底层是否有记录
            height_list.append(0)
            ratio_list.append(1)
            b_gradient_list.append(int(0))
        if item_in_list(height_list, height) == 0:#最高层是否有记录
            height_list.append(height)
            ratio_list.append(1)
            b_gradient_list.append(int(0))
        mapped_height_list = copy.deepcopy(height_list)
        mapped_height_list.sort()
        mapped_ratio_list = []
        mapped_gradient_list = []
        mapped_ratio_step = []
        RATIO_MIN = 0 #比例最小值
        for h in mapped_height_list:
            t_ratio = ratio_list[height_list.index(h)]
            if t_ratio < RATIO_MIN:
                t_ratio = RATIO_MIN
            if t_ratio > 1 - RATIO_MIN:
                t_ratio = 1 - RATIO_MIN
            mapped_ratio_list.append(t_ratio)
            mapped_gradient_list.append(b_gradient_list[height_list.index(h)])
        
        for h in mapped_height_list:
            index = mapped_height_list.index(h)
            if index != len(mapped_height_list) - 1 and mapped_height_list[index] != mapped_height_list[index + 1]:
                mapped_ratio_step.append((mapped_ratio_list[index + 1] - mapped_ratio_list[index]) / (mapped_height_list[index + 1] - mapped_height_list[index]))
                continue
            mapped_ratio_step.append(0)
        
        print('----------map list start----------------------')
        print(mapped_height_list)
        print(mapped_ratio_list)
        print(mapped_ratio_step)
        print(mapped_gradient_list)
        print('----------map list end----------------------')
        index = -1
        currE = 0
        currX = 0
        currY = 0
        currF = 3600
        scriptCnt = 0
        layer_init = 0
        switchNote = ';extruder switch YY'
        cutFlag = False
        enableCutInfillStart = self.para.enableCutInfill
        keepLayer = 0#保留层
        ebackWard = 0
        lastEBackWard = 0
        mapped_ratio_index = 0
        lastValidLayerZ = 0
        lastZ = 0
        absolutely = True
        reduceSpeedAppending = False
        reduceSpeedLastE = 0
        filamentPrepareAppending = True #耗材准备挤出
        for layer in data:
            index += 1
            lines = layer.split('\n')
            gcodeChangeFlag = False
            for lineno in range(len(lines)):
                line = lines[lineno]
                if line.startswith('G1 ') or line.startswith('G0 '):
                    s = line.split(' ')
                    (Z, E) = (None, None)
                    for item in s[1:]:
                        if len(item) <= 1:
                            continue
                        if item.startswith(';'):
                            continue
                        if item[0] == 'X':
                            if absolutely:
                                pass
                            currX = currX + float(item[1:])
                        if item[0] == 'Y':
                            if absolutely:
                                pass
                            currY = currY + float(item[1:])
                        if item[0] == 'Z':
                            if absolutely:
                                pass
                            Z = lastZ + float(item[1:])
                        if item[0] == 'E':
                            if absolutely:
                                pass
                            E = currE + float(item[1:])
                            if currE > E:
                                ebackWard = currE - E
                            else:
                                ebackWard = 0
                            currE = E
                            # M220 设置进给百分比，该百分比适用于所有（X，Y，Z和E）轴上的所有基于G代码的移动。
                            if reduceSpeedAppending and currE - reduceSpeedLastE > self.para.reduceSpeedELength:
                                reduceSpeedAppending = False
                                lines[lineno] = line + '\n' + '11M220 S100' + switchNote + '\n'
                                gcodeChangeFlag = True
                        if item[0] == 'F':
                            currF = float(item[1:])
                    if cutFlag:
                        lines[lineno] = ''
                        gcodeChangeFlag = True
                    elif len(mapped_height_list) > 0 and Z:
                        # if Z - lastZ >= 0.8:
                        #     continue
                        # lastZ = Z
                        if lastZ != Z: #TODO：截留填充
                            if self.para.enableCutInfill and Z >= self.para.cutInfillHeight:
                                enableCutInfillStart = keepLayer >= self.para.cutInfillLayerNr
                                if not enableCutInfillStart:
                                    keepLayer += 1
                                lastZ = Z
                        if lastValidLayerZ > Z:
                            mapped_ratio_index = 0
                            keepLayer = 0
                            enableCutInfillStart = self.para.enableCutInfill
                            scriptCnt = 0
                            lastValidLayerZ = 0
                            lastZ = 0
                        if Z >= mapped_height_list[mapped_ratio_index]:
                            curr_step = 0
                            curr_ratio = mapped_ratio_list[mapped_ratio_index]
                            _line = ''
                            if filamentPrepareAppending:#进退料使能
                                filamentPrepareAppending = False
                                if curr_ratio == 1:
                                    currEName = 'A'
                                    alterEName = 'B'
                                else:
                                    currEName = 'B'
                                    alterEName = 'A'
                                _line += 'G0 %s-%f F%f I0' % (currEName, self.para.backwardLength, self.para.backwardSpeed * 60) + switchNote + ' prepare\n'
                                _line += 'G0 %s%f F%f I0' % (alterEName, self.para.forwardLength, self.para.forwardSpeed * 60) + switchNote + ' prepare\n'
                                _line += 'G0 %s15 F300 I0' % alterEName + switchNote + ' prepare\n'
                                _line += 'G0 %s-%f F%f I0' % (alterEName, self.para.backwardLength, self.para.backwardSpeed * 60) + switchNote + ' prepare\n'
                                _line += 'G0 %s%f F%f I0' % (currEName, self.para.forwardLength, self.para.forwardSpeed * 60) + switchNote + ' prepare\n'
                                _line += 'G92 A0 B0' + switchNote + ' prepare\n'
                        if scriptCnt > 0 and self.para.enableSwitchFilamentBackward: #换料时进退料使能
                            _line = 'G0 E-%f F%f' % (self.para.backwardLength - ebackWard, self.para.backwardSpeed * 60) + switchNote + '\n' + _line
                        #创客主板没有使能开关
                        #TODO：_s = 'M6050 S%f P%f Z%f;DUAL_IN_ONE_OUT:ratio:%f height:%f gradient:%d\n' % (curr_ratio, curr_step, mapped_height_list[mapped_ratio_index], curr_ratio, mapped_height_list[mapped_ratio_index], mapped_gradient_list[mapped_ratio_index])
                        if scriptCnt == 0:
                            _s = ';MAX_Z_HEIGHT:%f\n' % height + _s
                        line = _line + _s + line + switchNote + '\n'
                        if scriptCnt > 0 and self.para.enableSwitchFilamentBackward:
                            if self.para.enableSwitchFilamentHome:
                                line += 'G0 X5 Y5 F9000' + switchNote + '\n'
                            if not self.para.enableSwitchFilamentHome:
                                pass
                            trueLength = self.para.backwardLength
                            line += 'G0 E%f F%f ' % (trueLength - ebackWard, self.para.forwardSpeed * 60) + switchNote + '\n'
                            if self.para.enableSwitchFilamentHome:
                                if (self.para.forwardLength - self.para.backwardLength) + ebackWard > 0:
                                    line += 'G0 E%f F120 ' % ((self.para.forwardLength - self.para.backwardLength) + ebackWard) + switchNote + '\n'
                                if self.para.homeDelay > 0:
                                    line += 'G4 P%f' % self.para.homeDelay * 1000 + switchNote + '\n'
                                if ebackWard > 0:
                                    line += 'G0 E-%f F%f ' % (ebackWard, self.para.backwardSpeed * 60) + switchNote + '\n'
                                line += 'G0 X%f Y%f F9000' % (currX, currY) + switchNote + '\n'
                            line += 'G92 E' + str(currE) + switchNote + '\n'
                        line += 'G0 F%f' % currF + switchNote + '\n'
                        if self.para.switchFilamentReduceSpeed:#TODO M220 设置进给百分比，该百分比适用于所有（X，Y，Z和E）轴上的所有基于G代码的移动。
                            line += 'M220 S%f' % self.para.reduceSpeedRatio + switchNote + '\n'
                            reduceSpeedAppending = True
                            reduceSpeedLastE = currE
                        scriptCnt = scriptCnt + 1
                        lastValidLayerZ = Z
                        if mapped_ratio_index < len(mapped_height_list) - 1:
                            mapped_ratio_index += 1
                        lines[lineno] = line
                        gcodeChangeFlag = True
                        print('generate extrude switch code')
                        continue
                if line.startswith('M6050'):
                    continue

                if layer_init == 0 or line.startswith(';LAYER_COUNT:'):
                    layer_init = 1
                    continue
                if switchNote in line:
                    continue

                if line.startswith(';MAX_Z_HEIGHT:'):
                    continue

                if line.startswith('G92'):
                    E = self.getValue(line, 'E', currE)
                    if E != currE:
                        currE = E
                        ebackWard = 0
                    lastZ = self.getValue(line, 'Z', lastZ)
                    continue
                if enableCutInfillStart and line.startswith(';TYPE:'):
                    if line.startswith(';TYPE:FILL'):
                        cutFlag = True
                        gcodeChangeFlag = True
                        lastEBackWard = ebackWard
                    if cutFlag:
                        lines[lineno] = 'G0 X%f Y%f F%f\nG92 E%f\n' % (currX, currY, currF, (currE - lastEBackWard) + ebackWard) + line
                        cutFlag = False
                        gcodeChangeFlag = True
                        continue
                if line.startswith('G91'):
                    absolutely = False
                    continue
                if line.startswith('G90'):
                    absolutely = True
                if gcodeChangeFlag:
                    data[index] = '\n' + '\n'.join(filter((lambda x: len(x) > 0), lines)) + '\n'
        return data

        return (None,)