#!/usr/bin/env python
# encoding: utf-8
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
        self.backwardLength = 43
        self.forwardLength = 43
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
        pkFile = os.path.join(os.path.join(Resources.getStoragePath(Resources.Resources), 'plugins'), 'AdvertWord3C.pk')
        if os.path.exists(pkFile):

            try:
                _pkDat = pickle.load(open(pkFile, 'rb'))
            except:
                None
                None
                None
                _pkDat = None

            if isinstance(_pkDat, AdvertWordPara):
                i = self.__dict__
                for key in self.__dict__.keys():
                    if not isinstance(getattr(self, key), float) and isinstance(getattr(self, key), bool) and isinstance(getattr(self, key), str):
                        if isinstance(getattr(self, key), int) and key in _pkDat.__dict__.keys() and type(getattr(self, key)) == type(getattr(_pkDat, key)):
                            setattr(self, key, getattr(_pkDat, key))
                        return None



class AdvertWord3C(Script):
    __qualname__ = 'AdvertWord3C'

    def __init__(self):
        super().__init__()


    def getSettingDataString(self):
        if not hasattr(self, 'initDone'):
            self.initDone = True
            self.para = AdvertWordPara()
        print("SBS")
        rtDat = '{' \
                '            "name":"广告字专业三色插件",' \
                '            "key": "AdvertWord3C",' \
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
                '                    "label":"*换色进退料使能",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "SwitchFilamentHome":' \
                '                {' \
                '                    "label":"    换色时是否归零",' \
                '                    "description": "",' \
                '                    "type": "bool",' \
                '                    "default_value": %s,' \
                '                    "enabled": "SwitchFilamentBackward"' \
                '                },' \
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
                '                "Layer0":' \
                '                {' \
                '                    "label":"*初始层",' \
                '                    "description": "Set height ratio and select Extruder",' \
                '                    "type": "bool",' \
                '                    "default_value": %s' \
                '                },' \
                '                "Z_ratio0":' \
                '                {' \
                '                    "label": "    Z高度   ",' \
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
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
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
                '                    "label": "    Z高度   ",' \
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
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
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
                '                    "label": "    Z高度   ",' \
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
                '                    "type": "enum",' \
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
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
                '                    "label": "    Z高度   ",' \
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
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
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
                '                    "label": "    Z高度   ",' \
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
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
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
                '                    "label": "    Z高度   ",' \
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
                '                    "options": {"Extruder1":"挤出头1","Extruder2":"挤出头2","Extruder3":"挤出头3"},' \
                '                    "default_value": "%s",' \
                '                    "enabled": "Layer5"' \
                '                }' \
                '            }' \
                '        }' % (str(self.para.enableCutInfill).lower(), self.para.cutInfillHeight, self.para.cutInfillLayerNr, str(self.para.enableSwitchFilamentBackward).lower(), str(self.para.enableSwitchFilamentHome).lower(), self.para.backwardLength, self.para.forwardLength, str(self.para.layer0).lower(), self.para.z_ratio0, self.para.extrude_ratio0, str(self.para.layer1).lower(), self.para.z_ratio1, self.para.extrude_ratio1, str(self.para.layer2).lower(), self.para.z_ratio2, self.para.extrude_ratio2, str(self.para.layer3).lower(), self.para.z_ratio3, self.para.extrude_ratio3, str(self.para.layer4).lower(), self.para.z_ratio4, self.para.extrude_ratio4, str(self.para.layer5).lower(), self.para.z_ratio5, self.para.extrude_ratio5)
        return rtDat


    def getHeight(self, dat):
        try:
            global totalLayer
            totalLayer = -1 #总层数
            height = 0.0
            prepareEndFlag = False #准备结束的标志
            done = False #完成
            for layerDat in dat:
                lines = layerDat.split('\n')
                #print("layerDat:",lines)
                for line in lines:
                    if line:
                        code = self.getValue(line, 'G', None)
                        if code == 1 or code == 0:
                            height = self.getValue(line, 'Z', height)
                            #print("height:", height)
                            continue
                    if line.startswith(';LAYER_COUNT:'):
                        totalLayer = int(self.getValue(line, ';LAYER_COUNT:', totalLayer))
                        continue
                    if line.startswith(';End of Gcode'):
                        done = True
                        break
                        #continue
                    if line.startswith(';LAYER:') or int(self.getValue(line, ';LAYER:', 0)) == totalLayer - 1:
                        prepareEndFlag = True
                        continue
                    if prepareEndFlag:
                        done = True
                        break
                    if done:
                        break

            return float(height + 0.01)
        except Exception:
                    e = None
                    try:
                        print("e",e)
                        return 0
                    finally:
                        e = None
                        del e





    def getCurrentPara(self):
        self.para.enableCutInfill = self.getSettingValueByKey('CutInfill')
        self.para.cutInfillHeight = self.getSettingValueByKey('CutInfillHeight')
        self.para.cutInfillLayerNr = int(self.getSettingValueByKey('CutInfillLayerNr'))
        self.para.enableSwitchFilamentBackward = self.getSettingValueByKey('SwitchFilamentBackward')
        self.para.enableSwitchFilamentHome = self.getSettingValueByKey('SwitchFilamentHome')
        self.para.backwardLength = self.getSettingValueByKey('BackwardLength')
        self.para.forwardLength = self.getSettingValueByKey('ForwardLength')
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
        pkFile = os.path.join(os.path.join(Resources.getStoragePath(Resources.Resources), 'plugins'), 'AdvertWord3C.pk')
        print('pkFile:', pkFile)
        pickle.dump(self.para, open(pkFile, 'wb'))


    def _get_ratio(self, s):
        print("_get_ratio",s)
        if s == 'Extruder1':
            return (1, 0)
        if s == 'Extruder2':
            return (0, 1)
        if s == 'Extruder3':
            return (1, 1)
        return None


    def execute(self, data):
        paraList = []
        self.getCurrentPara()
        if self.para.layer0:
            paraList.append((self.para.z_ratio0 / 100, self._get_ratio(self.para.extrude_ratio0), 0))
        if self.para.layer1:
            paraList.append((self.para.z_ratio1 / 100, self._get_ratio(self.para.extrude_ratio1), 1))
        if self.para.layer2:
            paraList.append((self.para.z_ratio2 / 100, self._get_ratio(self.para.extrude_ratio2), 2))
        if self.para.layer3:
            paraList.append((self.para.z_ratio3 / 100, self._get_ratio(self.para.extrude_ratio3), 3))
        if self.para.layer4:
            paraList.append((self.para.z_ratio4 / 100, self._get_ratio(self.para.extrude_ratio4), 4))
        if self.para.layer5:
            paraList.append((self.para.z_ratio5 / 100, self._get_ratio(self.para.extrude_ratio5), 5))
        #print("paraList:",self.para)
        index = -1
        height = 0
        height_list = []
        ratio_list = []
        b_gradient_list = []
        if height == 0:
            height = self.getHeight(data)
        print("paraList",paraList)
        print("height:",height)
        print('-----------list start---------------------')

        def item_in_list(list, item):
            print("item:",item)

            try:
                return list.index(item) >= 0
            except:
                print("list.index:", list)
                return 0
        for (Z_ratio, extrude_ratio, b_gradient) in paraList:
            #print("item",height_list)
            #print("item", Z_ratio , height)
            if item_in_list(height_list, (Z_ratio * height)) == 0:
                height_list.append(Z_ratio * height)
                ratio_list.append(extrude_ratio)
                b_gradient_list.append(int(b_gradient))
                continue
            ratio_list[height_list.index(Z_ratio * height)] = extrude_ratio
            b_gradient_list[height_list.index(Z_ratio * height)] = int(b_gradient)

        if item_in_list(height_list, 0) == 0:
            height_list.append(0)
            ratio_list.append((1, 0))
            b_gradient_list.append(int(0))
        mapped_height_list = copy.deepcopy(height_list)
        mapped_height_list.sort()
        mapped_ratio_list = []
        mapped_gradient_list = []
        mapped_ratio_step = []
        RATIO_MIN = 0
        for h in mapped_height_list:
            print(ratio_list)
            t_ratio = ratio_list[height_list.index(h)]
            #print("TTTTT",t_ratio)
            mapped_ratio_list.append(t_ratio)
            mapped_gradient_list.append(b_gradient_list[height_list.index(h)])

        for h in mapped_height_list:
            index = mapped_height_list.index(h)
            if index != len(mapped_height_list) - 1 and mapped_height_list[index] != mapped_height_list[index + 1]:
                mapped_ratio_step.append((0, 0))
                continue
            mapped_ratio_step.append((0, 0))

        print('----------map list start----------------------')
        print("mapped_height_list",mapped_height_list)
        print("mapped_ratio_list",mapped_ratio_list)
        print("mapped_ratio_step",mapped_ratio_step)
        print("mapped_gradient_list",mapped_gradient_list)
        print('----------map list end----------------------')
        index = -1
        currE = 0
        currX = 0
        currY = 0
        #currF = 0
        currF = 0
        scriptCnt = 0
        layer_init = 0
        switchNote = ';extruder switch YY'
        cutFlag = False
        enableCutInfillStart = self.para.enableCutInfill
        keepLayer = 0
        ebackWard = 0
        lastEBackWard = 0
        mapped_ratio_index = 0
        lastValidLayerZ = 0
        lastZ = 0
        absolutely = True
        for layer in data:
            index += 1
            lines = layer.split('\n')
            gcodeChangeFlag = False
            for lineno in range(len(lines)):
                line = lines[lineno]
                #print("line:",line)
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
                        if item[0] == 'F':
                            currF = float(item[1:])
                        if cutFlag:
                            lines[lineno] = ''
                            gcodeChangeFlag = True
                        elif len(mapped_height_list) > 0 and Z:
                                print("ZZZZ:",Z)
                                if Z - lastZ >= 0.8:
                                    continue
                                if lastZ != Z:
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
                                    curr_ratio = mapped_ratio_list[mapped_ratio_index]
                                    _line = ''
                                    if scriptCnt > 0 and self.para.enableSwitchFilamentBackward:#启动选择材料回退
                                        _line = 'G0 E-%f F6000 I0' % (self.para.backwardLength - ebackWard) + switchNote + '\n' + _line
                                        _line = 'G92 E' + str(currE) + switchNote + '\n' + _line
                                    #print("SBS:", mapped_ratio_list)
                                    #print("SBB:",curr_ratio[0],curr_ratio[1])
                                    #print("BBS:", mapped_height_list[mapped_ratio_index],mapped_gradient_list[mapped_ratio_index])
                                    _s = 'M6050 S%f P0 D%f C0 Z%f;DUAL_IN_ONE_OUT:ratio:%f/%f height:%f gradient:%d\n' % (curr_ratio[0], curr_ratio[1], mapped_height_list[mapped_ratio_index], curr_ratio[0], curr_ratio[1], mapped_height_list[mapped_ratio_index], mapped_gradient_list[mapped_ratio_index])
                                    if scriptCnt == 0:
                                        _s = ';MAX_Z_HEIGHT:%f\n' % height + _s
                                    line = _line + _s + line + switchNote + '\n'
                                    if scriptCnt > 0 and self.para.enableSwitchFilamentBackward:
                                        if self.para.enableSwitchFilamentHome:
                                            line += 'G0 X5 Y5 F9000 I1' + switchNote + '\n'
                                        if not self.para.enableSwitchFilamentHome:
                                            pass
                                        trueLength = self.para.backwardLength
                                        line += 'G0 E%f F6000 I0' % (trueLength - ebackWard) + switchNote + '\n'
                                        if self.para.enableSwitchFilamentHome:
                                            if (self.para.forwardLength - self.para.backwardLength) + ebackWard > 0:
                                                line += 'G0 E%f F120 I0' % ((self.para.forwardLength - self.para.backwardLength) + ebackWard) + switchNote + '\n'
                                            if ebackWard > 0:
                                                line += 'G0 E-%f F6000 I0' % ebackWard + switchNote + '\n'
                                            line += 'G0 X%f Y%f F9000 T1' % (currX, currY) + switchNote + '\n'
                                        line += 'G92 E' + str(currE) + switchNote + '\n'
                                    line += 'G0 F%f' % currF + switchNote + '\n'
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
                    elif cutFlag:
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