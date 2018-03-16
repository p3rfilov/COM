# -*- coding: mbcs -*-
typelib_path = 'C:\\Program Files\\Adobe\\Adobe Photoshop CC 2015.5\\Required\\Plug-Ins\\Extensions\\ScriptingSupport.8li'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes.wintypes import VARIANT_BOOL
from comtypes import BSTR
from comtypes import dispid
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring
from comtypes.automation import VARIANT
from comtypes.automation import IDispatch
from comtypes import IUnknown
from comtypes import CoClass



# values for enumeration 'PsJavaScriptExecutionMode'
psNeverShowDebugger = 1
psDebuggerOnError = 2
psBeforeRunning = 3
PsJavaScriptExecutionMode = c_int # enum

# values for enumeration 'PsChannelType'
psComponentChannel = 1
psMaskedAreaAlphaChannel = 2
psSelectedAreaAlphaChannel = 3
psSpotColorChannel = 4
PsChannelType = c_int # enum

# values for enumeration 'PsColorBlendMode'
psNormalBlendColor = 2
psDissolveBlend = 3
psBehindBlend = 24
psClearBlend = 25
psDarkenBlend = 4
psMultiplyBlend = 5
psColorBurnBlend = 6
psLinearBurnBlend = 7
psLightenBlend = 8
psScreenBlend = 9
psColorDodgeBlend = 10
psLinearDodgeBlend = 11
psOverlayBlend = 12
psSoftLightBlend = 13
psHardLightBlend = 14
psVividLightBlend = 15
psLinearLightBlend = 16
psPinLightBlend = 17
psDifferenceBlend = 18
psExclusionBlend = 19
psSubtractBlend = 29
psDivideBlend = 30
psHueBlend = 20
psSaturationBlendColor = 21
PsColorBlendMode = 22
psLuminosityBlend = 23
psHardMixBlend = 26
psLighterColorBlend = 27
psDarkerColorBlend = 28
PsColorBlendMode = c_int # enum
class _PNGSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a PNG document'
    _iid_ = GUID('{478BF855-E42A-4D63-8C9D-F562DE5FF7A8}')
    _idlflags_ = ['hidden']
    _methods_ = []
class _Application(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The Adobe Photoshop application'
    _iid_ = GUID('{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}')
    _idlflags_ = ['hidden', 'nonextensible']
    _methods_ = []
class Document(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A document'
    _iid_ = GUID('{B1ADEFB6-C536-42D6-8A83-397354A769F8}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
class ArtLayer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'any layer that can contain data'
    _iid_ = GUID('{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsLayerKind'
psNormalLayer = 1
psTextLayer = 2
psSolidFillLayer = 3
psGradientFillLayer = 4
psPatternFillLayer = 5
psLevelsLayer = 6
psCurvesLayer = 7
psColorBalanceLayer = 8
psBrightnessContrastLayer = 9
psHueSaturationLayer = 10
psSelectiveColorLayer = 11
psChannelMixerLayer = 12
psGradientMapLayer = 13
psInversionLayer = 14
psThresholdLayer = 15
psPosterizeLayer = 16
psSmartObjectLayer = 17
psPhotoFilterLayer = 18
psExposureLayer = 19
psLayer3D = 20
psVideoLayer = 21
psBlackAndWhiteLayer = 22
psVibrance = 23
psColorLookup = 24
PsLayerKind = c_int # enum
class TextItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Text object contained in an art layer'
    _iid_ = GUID('{E7A940CD-9AC7-4D76-975D-24D6BA0FDD16}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsAntiAlias'
psNoAntialias = 1
psSharp = 2
psCrisp = 3
psStrong = 4
psSmooth = 5
PsAntiAlias = c_int # enum

# values for enumeration 'PsAutoKernType'
psManual = 1
psMetrics = 2
psOptical = 3
PsAutoKernType = c_int # enum
class _SolidColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A color value'
    _iid_ = GUID('{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsColorModel'
psGrayscaleModel = 1
psRGBModel = 2
psCMYKModel = 3
psLabModel = 4
psHSBModel = 5
psNoModel = 50
PsColorModel = c_int # enum
class _RGBColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An RGB color specification'
    _iid_ = GUID('{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}')
    _idlflags_ = ['hidden']
    _methods_ = []
_RGBColor._disp_methods_ = [
    DISPMETHOD([dispid(1884443254), helpstring('the red color value ( 0.0 - 255.0; default: 255.0 )'), 'propget'], c_double, 'Red'),
    DISPMETHOD([dispid(1884443254), helpstring('the red color value ( 0.0 - 255.0; default: 255.0 )'), 'propput'], None, 'Red',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884440438), helpstring('the green color value ( 0.0 - 255.0; default: 255.0 )'), 'propget'], c_double, 'Green'),
    DISPMETHOD([dispid(1884440438), helpstring('the green color value ( 0.0 - 255.0; default: 255.0 )'), 'propput'], None, 'Green',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884439158), helpstring('the blue color value ( 0.0 - 255.0; default: 255.0 )'), 'propget'], c_double, 'Blue'),
    DISPMETHOD([dispid(1884439158), helpstring('the blue color value ( 0.0 - 255.0; default: 255.0 )'), 'propput'], None, 'Blue',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884440696), helpstring('Hex representation of this color'), 'propget'], BSTR, 'HexValue'),
    DISPMETHOD([dispid(1884440696), helpstring('Hex representation of this color'), 'propput'], None, 'HexValue',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_RGBColor), 'rhs' )),
]
class _GrayColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A gray color specification'
    _iid_ = GUID('{1B28B8CD-7578-415F-AC67-DC22A69F4C07}')
    _idlflags_ = ['hidden']
    _methods_ = []
_GrayColor._disp_methods_ = [
    DISPMETHOD([dispid(1883730550), helpstring('the gray value ( 0.0 - 100.0; default: 0.0 )'), 'propget'], c_double, 'Gray'),
    DISPMETHOD([dispid(1883730550), helpstring('the gray value ( 0.0 - 100.0; default: 0.0 )'), 'propput'], None, 'Gray',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GrayColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GrayColor), 'rhs' )),
]
class _CMYKColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A CMYK color specification'
    _iid_ = GUID('{29C13F49-BCEF-4FE2-BFC7-6F03B82B726F}')
    _idlflags_ = ['hidden']
    _methods_ = []
_CMYKColor._disp_methods_ = [
    DISPMETHOD([dispid(1883456374), helpstring('the cyan color value (between 0.0 and 100.0)'), 'propget'], c_double, 'Cyan'),
    DISPMETHOD([dispid(1883456374), helpstring('the cyan color value (between 0.0 and 100.0)'), 'propput'], None, 'Cyan',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1883458934), helpstring('the magenta color value (between 0.0 and 100.0)'), 'propget'], c_double, 'Magenta'),
    DISPMETHOD([dispid(1883458934), helpstring('the magenta color value (between 0.0 and 100.0)'), 'propput'], None, 'Magenta',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1883462006), helpstring('the yellow color value (between 0.0 and 100.0)'), 'propget'], c_double, 'Yellow'),
    DISPMETHOD([dispid(1883462006), helpstring('the yellow color value (between 0.0 and 100.0)'), 'propput'], None, 'Yellow',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1883458422), helpstring('the black color value (between 0.0 and 100.0)'), 'propget'], c_double, 'Black'),
    DISPMETHOD([dispid(1883458422), helpstring('the black color value (between 0.0 and 100.0)'), 'propput'], None, 'Black',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_CMYKColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_CMYKColor), 'rhs' )),
]
class _LabColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An Lab color specification'
    _iid_ = GUID('{F4D7F5C2-37DB-4DF7-8A7D-528902056596}')
    _idlflags_ = ['hidden']
    _methods_ = []
_LabColor._disp_methods_ = [
    DISPMETHOD([dispid(1884054092), helpstring('the L-value (between 0.0 and 100.0)'), 'propget'], c_double, 'L'),
    DISPMETHOD([dispid(1884054092), helpstring('the L-value (between 0.0 and 100.0)'), 'propput'], None, 'L',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884054113), helpstring('the a-value (between -128.0 and 127.0)'), 'propget'], c_double, 'A'),
    DISPMETHOD([dispid(1884054113), helpstring('the a-value (between -128.0 and 127.0)'), 'propput'], None, 'A',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884054114), helpstring('the b-value (between -128.0 and 127.0)'), 'propget'], c_double, 'B'),
    DISPMETHOD([dispid(1884054114), helpstring('the b-value (between -128.0 and 127.0)'), 'propput'], None, 'B',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_LabColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_LabColor), 'rhs' )),
]
class _HSBColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An HSB color specification'
    _iid_ = GUID('{F91F9C5B-AC34-45B7-AFF2-871D9DD2E8EC}')
    _idlflags_ = ['hidden']
    _methods_ = []
_HSBColor._disp_methods_ = [
    DISPMETHOD([dispid(1883796837), helpstring('the hue value (between 0.0 and 360.0)'), 'propget'], c_double, 'Hue'),
    DISPMETHOD([dispid(1883796837), helpstring('the hue value (between 0.0 and 360.0)'), 'propput'], None, 'Hue',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884512628), helpstring('the saturation value (between 0.0 and 100.0)'), 'propget'], c_double, 'Saturation'),
    DISPMETHOD([dispid(1884512628), helpstring('the saturation value (between 0.0 and 100.0)'), 'propput'], None, 'Saturation',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1114141806), helpstring('the brightness value (between 0.0 and 100.0)'), 'propget'], c_double, 'Brightness'),
    DISPMETHOD([dispid(1114141806), helpstring('the brightness value (between 0.0 and 100.0)'), 'propput'], None, 'Brightness',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_HSBColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_HSBColor), 'rhs' )),
]
_SolidColor._disp_methods_ = [
    DISPMETHOD([dispid(1883458916), helpstring('color model'), 'propget'], PsColorModel, 'Model'),
    DISPMETHOD([dispid(1883458916), helpstring('color model'), 'propput'], None, 'Model',
               ( [], PsColorModel, 'rhs' )),
    DISPMETHOD([dispid(1666336630), helpstring('return an rgb representation of the color'), 'propget'], POINTER(_RGBColor), 'RGB'),
    DISPMETHOD([dispid(1666336630), helpstring('return an rgb representation of the color'), 'propput'], None, 'RGB',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1666336630), helpstring('return an rgb representation of the color'), 'propputref'], None, 'RGB',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1665626742), helpstring('return a grayscale representation of the color'), 'propget'], POINTER(_GrayColor), 'Gray'),
    DISPMETHOD([dispid(1665626742), helpstring('return a grayscale representation of the color'), 'propput'], None, 'Gray',
               ( [], POINTER(_GrayColor), 'rhs' )),
    DISPMETHOD([dispid(1665626742), helpstring('return a grayscale representation of the color'), 'propputref'], None, 'Gray',
               ( [], POINTER(_GrayColor), 'rhs' )),
    DISPMETHOD([dispid(1665355126), helpstring('return a grayscale representation of the color'), 'propget'], POINTER(_CMYKColor), 'CMYK'),
    DISPMETHOD([dispid(1665355126), helpstring('return a grayscale representation of the color'), 'propput'], None, 'CMYK',
               ( [], POINTER(_CMYKColor), 'rhs' )),
    DISPMETHOD([dispid(1665355126), helpstring('return a grayscale representation of the color'), 'propputref'], None, 'CMYK',
               ( [], POINTER(_CMYKColor), 'rhs' )),
    DISPMETHOD([dispid(1665950326), helpstring('return a grayscale representation of the color'), 'propget'], POINTER(_LabColor), 'Lab'),
    DISPMETHOD([dispid(1665950326), helpstring('return a grayscale representation of the color'), 'propput'], None, 'Lab',
               ( [], POINTER(_LabColor), 'rhs' )),
    DISPMETHOD([dispid(1665950326), helpstring('return a grayscale representation of the color'), 'propputref'], None, 'Lab',
               ( [], POINTER(_LabColor), 'rhs' )),
    DISPMETHOD([dispid(1665679990), helpstring('return a grayscale representation of the color'), 'propget'], POINTER(_HSBColor), 'HSB'),
    DISPMETHOD([dispid(1665679990), helpstring('return a grayscale representation of the color'), 'propput'], None, 'HSB',
               ( [], POINTER(_HSBColor), 'rhs' )),
    DISPMETHOD([dispid(1665679990), helpstring('return a grayscale representation of the color'), 'propputref'], None, 'HSB',
               ( [], POINTER(_HSBColor), 'rhs' )),
    DISPMETHOD([dispid(1466057580), helpstring('The nearest web color to the current color'), 'propget'], POINTER(_RGBColor), 'NearestWebColor'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1129406828), helpstring('return true if the provided color is visually equal to this color')], VARIANT_BOOL, 'IsEqual',
               ( ['in'], POINTER(_SolidColor), 'Color' )),
]

# values for enumeration 'PsDirection'
psHorizontal = 1
psVertical = 2
PsDirection = c_int # enum

# values for enumeration 'PsCase'
psNormalCase = 1
psAllCaps = 2
psSmallCaps = 3
PsCase = c_int # enum

# values for enumeration 'PsStrikeThruType'
psStrikeOff = 1
psStrikeHeight = 2
psStrikeBox = 3
PsStrikeThruType = c_int # enum

# values for enumeration 'PsUnderlineType'
psUnderlineOff = 1
psUnderlineRight = 2
psUnderlineLeft = 3
PsUnderlineType = c_int # enum

# values for enumeration 'PsLanguage'
psEnglishUSA = 1
psEnglishUK = 2
psFrench = 3
psCanadianFrench = 4
psFinnish = 5
psGerman = 6
psOldGerman = 7
psSwissGerman = 8
psItalian = 9
psNorwegian = 10
psNynorskNorwegian = 11
psPortuguese = 12
psBrazillianPortuguese = 13
psSpanish = 14
psSwedish = 15
psDutch = 16
psDanish = 17
PsLanguage = c_int # enum

# values for enumeration 'PsTextType'
psPointText = 1
psParagraphText = 2
PsTextType = c_int # enum

# values for enumeration 'PsJustification'
psLeft = 1
psCenter = 2
psRight = 3
psLeftJustified = 4
psCenterJustified = 5
psRightJustified = 6
psFullyJustified = 7
PsJustification = c_int # enum

# values for enumeration 'PsTextComposer'
psAdobeSingleLine = 1
psAdobeEveryLine = 2
PsTextComposer = c_int # enum

# values for enumeration 'PsWarpStyle'
psNoWarp = 1
psArc = 2
psArcLower = 3
psArcUpper = 4
psArch = 5
psBulge = 6
psShellLower = 7
psShellUpper = 8
psFlag = 9
psWave = 10
psFish = 11
psRise = 12
psFishEye = 13
psInflate = 14
psSqueeze = 15
psTwist = 16
PsWarpStyle = c_int # enum
TextItem._disp_methods_ = [
    DISPMETHOD([dispid(1094808688), 'propget'], PsAntiAlias, 'AntiAliasMethod'),
    DISPMETHOD([dispid(1094808688), 'propput'], None, 'AntiAliasMethod',
               ( [], PsAntiAlias, 'rhs' )),
    DISPMETHOD([dispid(1097560686), helpstring('options for auto kerning'), 'propget'], PsAutoKernType, 'AutoKerning'),
    DISPMETHOD([dispid(1097560686), helpstring('options for auto kerning'), 'propput'], None, 'AutoKerning',
               ( [], PsAutoKernType, 'rhs' )),
    DISPMETHOD([dispid(1413704771), helpstring('color of text'), 'propget'], POINTER(_SolidColor), 'Color'),
    DISPMETHOD([dispid(1413704771), helpstring('color of text'), 'propput'], None, 'Color',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1413704771), helpstring('color of text'), 'propputref'], None, 'Color',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1097622631), helpstring("whether to use a font's built-in leading information"), 'propget'], VARIANT_BOOL, 'UseAutoLeading'),
    DISPMETHOD([dispid(1097622631), helpstring("whether to use a font's built-in leading information"), 'propput'], None, 'UseAutoLeading',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416784750), helpstring('controls uniform spacing between multiple characters'), 'propget'], c_double, 'Tracking'),
    DISPMETHOD([dispid(1416784750), helpstring('controls uniform spacing between multiple characters'), 'propput'], None, 'Tracking',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1450464099), helpstring('vertical scaling of characters (in percent)'), 'propget'], c_int, 'VerticalScale'),
    DISPMETHOD([dispid(1450464099), helpstring('vertical scaling of characters (in percent)'), 'propput'], None, 'VerticalScale',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1215452003), helpstring('horizontal scaling of characters (in percent)'), 'propget'], c_int, 'HorizontalScale'),
    DISPMETHOD([dispid(1215452003), helpstring('horizontal scaling of characters (in percent)'), 'propput'], None, 'HorizontalScale',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1114403688), helpstring('baseline offset of text (unit value)'), 'propget'], c_double, 'BaselineShift'),
    DISPMETHOD([dispid(1114403688), helpstring('baseline offset of text (unit value)'), 'propput'], None, 'BaselineShift',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1885564532), helpstring('the text in the layer'), 'propget'], BSTR, 'Contents'),
    DISPMETHOD([dispid(1885564532), helpstring('the text in the layer'), 'propput'], None, 'Contents',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('text face of the character'), 'propget'], BSTR, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('text face of the character'), 'propput'], None, 'Font',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1414292583), helpstring('leading (unit value)'), 'propget'], c_double, 'Leading'),
    DISPMETHOD([dispid(1414292583), helpstring('leading (unit value)'), 'propput'], None, 'Leading',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1282699891), helpstring('use ligatures?'), 'propget'], VARIANT_BOOL, 'Ligatures'),
    DISPMETHOD([dispid(1282699891), helpstring('use ligatures?'), 'propput'], None, 'Ligatures',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1095529587), helpstring('use alternate ligatures?'), 'propget'], VARIANT_BOOL, 'AlternateLigatures'),
    DISPMETHOD([dispid(1095529587), helpstring('use alternate ligatures?'), 'propput'], None, 'AlternateLigatures',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1331975028), helpstring('use old style?'), 'propget'], VARIANT_BOOL, 'OldStyle'),
    DISPMETHOD([dispid(1331975028), helpstring('use old style?'), 'propput'], None, 'OldStyle',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1332897646), helpstring('position of origin (unit value)'), 'propget'], VARIANT, 'Position'),
    DISPMETHOD([dispid(1332897646), helpstring('position of origin (unit value)'), 'propput'], None, 'Position',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1413769586), helpstring('text orientation'), 'propget'], PsDirection, 'Direction'),
    DISPMETHOD([dispid(1413769586), helpstring('text orientation'), 'propput'], None, 'Direction',
               ( [], PsDirection, 'rhs' )),
    DISPMETHOD([dispid(1886679930), helpstring('font size in points'), 'propget'], c_double, 'Size'),
    DISPMETHOD([dispid(1886679930), helpstring('font size in points'), 'propput'], None, 'Size',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1182286444), helpstring('use faux bold?'), 'propget'], VARIANT_BOOL, 'FauxBold'),
    DISPMETHOD([dispid(1182286444), helpstring('use faux bold?'), 'propput'], None, 'FauxBold',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1182288244), helpstring('use faux italic?'), 'propget'], VARIANT_BOOL, 'FauxItalic'),
    DISPMETHOD([dispid(1182288244), helpstring('use faux italic?'), 'propput'], None, 'FauxItalic',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1130459251), helpstring('the case of the text'), 'propget'], PsCase, 'Capitalization'),
    DISPMETHOD([dispid(1130459251), helpstring('the case of the text'), 'propput'], None, 'Capitalization',
               ( [], PsCase, 'rhs' )),
    DISPMETHOD([dispid(1347711605), helpstring('options for strik thru of the text'), 'propget'], PsStrikeThruType, 'StrikeThru'),
    DISPMETHOD([dispid(1347711605), helpstring('options for strik thru of the text'), 'propput'], None, 'StrikeThru',
               ( [], PsStrikeThruType, 'rhs' )),
    DISPMETHOD([dispid(1433168238), helpstring('options for underlining of the text'), 'propget'], PsUnderlineType, 'Underline'),
    DISPMETHOD([dispid(1433168238), helpstring('options for underlining of the text'), 'propput'], None, 'Underline',
               ( [], PsUnderlineType, 'rhs' )),
    DISPMETHOD([dispid(1281453671), 'propget'], PsLanguage, 'Language'),
    DISPMETHOD([dispid(1281453671), 'propput'], None, 'Language',
               ( [], PsLanguage, 'rhs' )),
    DISPMETHOD([dispid(1315922539), 'propget'], VARIANT_BOOL, 'NoBreak'),
    DISPMETHOD([dispid(1315922539), 'propput'], None, 'NoBreak',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1265200740), helpstring('the type of the text'), 'propget'], PsTextType, 'Kind'),
    DISPMETHOD([dispid(1265200740), helpstring('the type of the text'), 'propput'], None, 'Kind',
               ( [], PsTextType, 'rhs' )),
    DISPMETHOD([dispid(1886024564), helpstring('paragraph justification'), 'propget'], PsJustification, 'Justification'),
    DISPMETHOD([dispid(1886024564), helpstring('paragraph justification'), 'propput'], None, 'Justification',
               ( [], PsJustification, 'rhs' )),
    DISPMETHOD([dispid(1414293860), helpstring('(unit value)'), 'propget'], c_double, 'LeftIndent'),
    DISPMETHOD([dispid(1414293860), helpstring('(unit value)'), 'propput'], None, 'LeftIndent',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1413900644), helpstring('(unit value)'), 'propget'], c_double, 'FirstLineIndent'),
    DISPMETHOD([dispid(1413900644), helpstring('(unit value)'), 'propput'], None, 'FirstLineIndent',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1414687076), helpstring('(unit value)'), 'propget'], c_double, 'RightIndent'),
    DISPMETHOD([dispid(1414687076), helpstring('(unit value)'), 'propput'], None, 'RightIndent',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1414742630), helpstring('(unit value)'), 'propget'], c_double, 'SpaceBefore'),
    DISPMETHOD([dispid(1414742630), helpstring('(unit value)'), 'propput'], None, 'SpaceBefore',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1414750566), helpstring('(unit value)'), 'propget'], c_double, 'SpaceAfter'),
    DISPMETHOD([dispid(1414750566), helpstring('(unit value)'), 'propput'], None, 'SpaceAfter',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1213227892), helpstring('use Roman Hanging Punctuation?'), 'propget'], VARIANT_BOOL, 'HangingPuntuation'),
    DISPMETHOD([dispid(1213227892), helpstring('use Roman Hanging Punctuation?'), 'propput'], None, 'HangingPuntuation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1213227875), helpstring('use Roman Hanging Punctuation?'), 'propget'], VARIANT_BOOL, 'HangingPunctuation'),
    DISPMETHOD([dispid(1213227875), helpstring('use Roman Hanging Punctuation?'), 'propput'], None, 'HangingPunctuation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1413705843), helpstring('type of text composing engine to use'), 'propget'], PsTextComposer, 'TextComposer'),
    DISPMETHOD([dispid(1413705843), helpstring('type of text composing engine to use'), 'propput'], None, 'TextComposer',
               ( [], PsTextComposer, 'rhs' )),
    DISPMETHOD([dispid(1430810728), helpstring('use hyphenation?'), 'propget'], VARIANT_BOOL, 'Hyphenation'),
    DISPMETHOD([dispid(1430810728), helpstring('use hyphenation?'), 'propput'], None, 'Hyphenation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1298745203), 'propget'], c_double, 'MinimumGlyphScaling'),
    DISPMETHOD([dispid(1298745203), 'propput'], None, 'MinimumGlyphScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1148405619), 'propget'], c_double, 'DesiredGlyphScaling'),
    DISPMETHOD([dispid(1148405619), 'propput'], None, 'DesiredGlyphScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1299400563), 'propget'], c_double, 'MaximumGlyphScaling'),
    DISPMETHOD([dispid(1299400563), 'propput'], None, 'MaximumGlyphScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1298746483), 'propget'], c_double, 'MinimumLetterScaling'),
    DISPMETHOD([dispid(1298746483), 'propput'], None, 'MinimumLetterScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1148406899), 'propget'], c_double, 'DesiredLetterScaling'),
    DISPMETHOD([dispid(1148406899), 'propput'], None, 'DesiredLetterScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1298222195), 'propget'], c_double, 'MaximumLetterScaling'),
    DISPMETHOD([dispid(1298222195), 'propput'], None, 'MaximumLetterScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1298749299), 'propget'], c_double, 'MinimumWordScaling'),
    DISPMETHOD([dispid(1298749299), 'propput'], None, 'MinimumWordScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1148409715), 'propget'], c_double, 'DesiredWordScaling'),
    DISPMETHOD([dispid(1148409715), 'propput'], None, 'DesiredWordScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1298225011), 'propget'], c_double, 'MaximumWordScaling'),
    DISPMETHOD([dispid(1298225011), 'propput'], None, 'MaximumWordScaling',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1097621837), helpstring('percentage to use for auto leading'), 'propget'], c_double, 'AutoLeadingAmount'),
    DISPMETHOD([dispid(1097621837), helpstring('percentage to use for auto leading'), 'propput'], None, 'AutoLeadingAmount',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1212970094), helpstring('hyphenate words that have more than this number of letters ( minimum 0 )'), 'propget'], c_int, 'HyphenateWordsLongerThan'),
    DISPMETHOD([dispid(1212970094), helpstring('hyphenate words that have more than this number of letters ( minimum 0 )'), 'propput'], None, 'HyphenateWordsLongerThan',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1212245620), helpstring('hyphenate after this many letters'), 'propget'], c_int, 'HyphenateAfterFirst'),
    DISPMETHOD([dispid(1212245620), helpstring('hyphenate after this many letters'), 'propput'], None, 'HyphenateAfterFirst',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1212311154), helpstring('hyphenate before this many letters'), 'propget'], c_int, 'HyphenateBeforeLast'),
    DISPMETHOD([dispid(1212311154), helpstring('hyphenate before this many letters'), 'propput'], None, 'HyphenateBeforeLast',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1212968308), helpstring('maximum number of consecutive hyphens'), 'propget'], c_int, 'HyphenLimit'),
    DISPMETHOD([dispid(1212968308), helpstring('maximum number of consecutive hyphens'), 'propput'], None, 'HyphenLimit',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1213886053), helpstring('the hyphenation zone (unit value)'), 'propget'], c_double, 'HyphenationZone'),
    DISPMETHOD([dispid(1213886053), helpstring('the hyphenation zone (unit value)'), 'propput'], None, 'HyphenationZone',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1212379251), helpstring('wheter to hyphenate capitalized words'), 'propget'], VARIANT_BOOL, 'HyphenateCapitalWords'),
    DISPMETHOD([dispid(1212379251), helpstring('wheter to hyphenate capitalized words'), 'propput'], None, 'HyphenateCapitalWords',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1466201192), helpstring('the width of paragraph text (unit value)'), 'propget'], c_double, 'Width'),
    DISPMETHOD([dispid(1466201192), helpstring('the width of paragraph text (unit value)'), 'propput'], None, 'Width',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1214736500), helpstring('the height of paragraph text (unit value)'), 'propget'], c_double, 'Height'),
    DISPMETHOD([dispid(1214736500), helpstring('the height of paragraph text (unit value)'), 'propput'], None, 'Height',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1465087084), 'propget'], PsWarpStyle, 'WarpStyle'),
    DISPMETHOD([dispid(1465087084), 'propput'], None, 'WarpStyle',
               ( [], PsWarpStyle, 'rhs' )),
    DISPMETHOD([dispid(1464101234), 'propget'], PsDirection, 'WarpDirection'),
    DISPMETHOD([dispid(1464101234), 'propput'], None, 'WarpDirection',
               ( [], PsDirection, 'rhs' )),
    DISPMETHOD([dispid(1463971428), helpstring('percentage from -100 to 100'), 'propget'], c_double, 'WarpBend'),
    DISPMETHOD([dispid(1463971428), helpstring('percentage from -100 to 100'), 'propput'], None, 'WarpBend',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1464353907), helpstring('percentage from -100 to 100'), 'propget'], c_double, 'WarpHorizontalDistortion'),
    DISPMETHOD([dispid(1464353907), helpstring('percentage from -100 to 100'), 'propput'], None, 'WarpHorizontalDistortion',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1465271411), helpstring('percentage from -100 to 100'), 'propget'], c_double, 'WarpVerticalDistortion'),
    DISPMETHOD([dispid(1465271411), helpstring('percentage from -100 to 100'), 'propput'], None, 'WarpVerticalDistortion',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1129803892), helpstring('creates a work path based on the text object')], None, 'CreatePath'),
    DISPMETHOD([dispid(1131819635), helpstring('converts the text object and its containing layer to a fill layer with the text changed to a clipping path')], None, 'ConvertToShape'),
]

# values for enumeration 'PsBlendMode'
psPassThrough = 1
psNormalBlend = 2
psDissolve = 3
psDarken = 4
psMultiply = 5
psColorBurn = 6
psLinearBurn = 7
psLighten = 8
psScreen = 9
psColorDodge = 10
psLinearDodge = 11
psOverlay = 12
psSoftLight = 13
psHardLight = 14
psVividLight = 15
psLinearLight = 16
psPinLight = 17
psDifference = 18
psExclusion = 19
psSubtract = 29
psDivide = 30
psHue = 20
psSaturationBlend = 21
psColorBlend = 22
psLuminosity = 23
psHardMix = 26
psLighterColor = 27
psDarkerColor = 28
PsBlendMode = c_int # enum

# values for enumeration 'PsLayerType'
psArtLayer = 1
psLayerSet = 2
PsLayerType = c_int # enum
class LayerSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Layer set'
    _iid_ = GUID('{C1C35524-2AA4-4630-80B9-011EFE3D5779}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
class Layers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}')
    _idlflags_ = []
    _methods_ = []
Layers._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1684368495), helpstring('Delete an element from the collection'), 'hidden'], None, 'Remove',
               ( ['in'], POINTER(IDispatch), 'Item' )),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(IDispatch), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(IDispatch), 'ItemPtr' )),
]
class LayerSets(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}')
    _idlflags_ = []
    _methods_ = []
LayerSets._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1684368495), helpstring('Delete an element from the collection'), 'hidden'], None, 'Remove',
               ( ['in'], POINTER(LayerSet), 'Item' )),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(LayerSet), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(LayerSet), 'ItemPtr' )),
    DISPMETHOD([dispid(1665948266), helpstring('create a new object')], POINTER(LayerSet), 'Add'),
]
class ArtLayers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}')
    _idlflags_ = []
    _methods_ = []
ArtLayers._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1684368495), helpstring('Delete an element from the collection'), 'hidden'], None, 'Remove',
               ( ['in'], POINTER(ArtLayer), 'Item' )),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(ArtLayer), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(ArtLayer), 'ItemPtr' )),
    DISPMETHOD([dispid(1665354858), helpstring('create a new object')], POINTER(ArtLayer), 'Add'),
]

# values for enumeration 'PsElementPlacement'
psPlaceInside = 0
psPlaceAtBeginning = 1
psPlaceAtEnd = 2
psPlaceBefore = 3
psPlaceAfter = 4
PsElementPlacement = c_int # enum
LayerSet._disp_methods_ = [
    DISPMETHOD([dispid(1164854120), helpstring('channels that are enabled for the layer set. Must be a list of component channels'), 'propget'], VARIANT, 'EnabledChannels'),
    DISPMETHOD([dispid(1164854120), helpstring('channels that are enabled for the layer set. Must be a list of component channels'), 'propput'], None, 'EnabledChannels',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1665956210), helpstring('the layers in this layer set'), 'propget'], POINTER(Layers), 'Layers'),
    DISPMETHOD([dispid(1665948276), helpstring('the top level layer sets in this document'), 'propget'], POINTER(LayerSets), 'LayerSets'),
    DISPMETHOD([dispid(1665354866), helpstring('the art layers in this layer set'), 'propget'], POINTER(ArtLayers), 'ArtLayers'),
    DISPMETHOD([dispid(1396927603), helpstring('The Layer corresponding to the LayerSet'), 'hidden', 'propget'], POINTER(IDispatch), 'Layer'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1097616483), 'propget'], VARIANT_BOOL, 'AllLocked'),
    DISPMETHOD([dispid(1097616483), 'propput'], None, 'AllLocked',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1114393956), 'propget'], PsBlendMode, 'BlendMode'),
    DISPMETHOD([dispid(1114393956), 'propput'], None, 'BlendMode',
               ( [], PsBlendMode, 'rhs' )),
    DISPMETHOD([dispid(1282106724), 'propget'], VARIANT, 'LinkedLayers'),
    DISPMETHOD([dispid(1332765556), helpstring('master opacity of layer ( 0.0 - 100.0 )'), 'propget'], c_double, 'Opacity'),
    DISPMETHOD([dispid(1332765556), helpstring('master opacity of layer ( 0.0 - 100.0 )'), 'propput'], None, 'Opacity',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884705634), 'propget'], VARIANT_BOOL, 'Visible'),
    DISPMETHOD([dispid(1884705634), 'propput'], None, 'Visible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1229201440), helpstring('the unique ID of this layer'), 'propget'], c_int, 'id'),
    DISPMETHOD([dispid(1886603640), helpstring('the layer index sans layer groups, how Photoshop would index them'), 'propget'], c_int, 'ItemIndex'),
    DISPMETHOD([dispid(1954115685), helpstring('Type of the Layer'), 'hidden', 'propget'], PsLayerType, 'LayerType'),
    DISPMETHOD([dispid(1279358028), helpstring('If the Layer is a ArtLayer then this property will return a reference to the corresponding ArtLayer object'), 'hidden', 'propget'], POINTER(ArtLayer), 'ArtLayer'),
    DISPMETHOD([dispid(1279358042), helpstring('If the Layer is a LayerSet then this property will return a reference to the corresponding LayerSet object'), 'hidden', 'propget'], POINTER(LayerSet), 'LayerSet'),
    DISPMETHOD([dispid(1114530931), helpstring('Bounding rectangle of the Layer'), 'propget'], VARIANT, 'Bounds'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1298615386), helpstring('merge layerset. Returns a reference to the art layer that is created by this method')], POINTER(ArtLayer), 'Merge'),
    DISPMETHOD([dispid(1433169515), helpstring('unlink the layer')], None, 'Unlink'),
    DISPMETHOD([dispid(1818973295), helpstring('link the layer with another layer')], None, 'Link',
               ( ['in'], POINTER(IDispatch), 'With' )),
    DISPMETHOD([dispid(1299599475), helpstring('moves the position relative to its current position')], None, 'Translate',
               ( ['in', 'optional'], VARIANT, 'DeltaX' ),
               ( ['in', 'optional'], VARIANT, 'DeltaY' )),
    DISPMETHOD([dispid(1383036001)], None, 'Rotate',
               ( ['in'], c_double, 'Angle' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1399024741)], None, 'Resize',
               ( ['in', 'optional'], VARIANT, 'Horizontal' ),
               ( ['in', 'optional'], VARIANT, 'Vertical' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1299596646), helpstring('Move the PageItem to beginning of container'), 'hidden'], None, 'MoveToBeginning',
               ( ['in'], POINTER(IDispatch), 'Container' )),
    DISPMETHOD([dispid(1299596645), helpstring('Move the PageItem to end of container'), 'hidden'], None, 'MoveToEnd',
               ( ['in'], POINTER(IDispatch), 'Container' )),
    DISPMETHOD([dispid(1299596642), helpstring('Move the PageItem in front of object'), 'hidden'], None, 'MoveBefore',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' )),
    DISPMETHOD([dispid(1299596641), helpstring('Move the PageItem in behind object'), 'hidden'], None, 'MoveAfter',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' )),
    DISPMETHOD([dispid(1668050798), helpstring('create a duplicate of the object')], POINTER(IDispatch), 'Duplicate',
               ( ['in', 'optional'], VARIANT, 'RelativeObject' ),
               ( ['in', 'optional'], VARIANT, 'InsertionLocation' )),
    DISPMETHOD([dispid(1836021349), helpstring('move the object')], None, 'Move',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' ),
               ( ['in'], PsElementPlacement, 'InsertionLocation' )),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]

# values for enumeration 'PsRasterizeType'
psTextContents = 1
psShape = 2
psFillContent = 3
psLayerClippingPath = 4
psEntireLayer = 5
psLinkedLayers = 6
PsRasterizeType = c_int # enum

# values for enumeration 'PsRadialBlurMethod'
psSpin = 1
psZoom = 2
PsRadialBlurMethod = c_int # enum

# values for enumeration 'PsRadialBlurQuality'
psRadialBlurDraft = 1
psRadialBlurGood = 2
psRadialBlurBest = 3
PsRadialBlurQuality = c_int # enum

# values for enumeration 'PsSmartBlurQuality'
psSmartBlurLow = 1
psSmartBlurMedium = 2
psSmartBlurHigh = 3
PsSmartBlurQuality = c_int # enum

# values for enumeration 'PsSmartBlurMode'
psSmartBlurNormal = 1
psSmartBlurEdgeOnly = 2
psSmartBlurOverlayEdge = 3
PsSmartBlurMode = c_int # enum

# values for enumeration 'PsDisplacementMapType'
psStretchToFit = 1
psTile = 2
PsDisplacementMapType = c_int # enum

# values for enumeration 'PsUndefinedAreas'
psWrapAround = 1
psRepeatEdgePixels = 2
PsUndefinedAreas = c_int # enum

# values for enumeration 'PsPolarConversionType'
psRectangularToPolar = 1
psPolarToRectangular = 2
PsPolarConversionType = c_int # enum

# values for enumeration 'PsRippleSize'
psSmallRipple = 1
psMediumRipple = 2
psLargeRipple = 3
PsRippleSize = c_int # enum

# values for enumeration 'PsSpherizeMode'
psNormalSpherize = 1
psHorizontalSpherize = 2
psVerticalSpherize = 3
PsSpherizeMode = c_int # enum

# values for enumeration 'PsWaveType'
psSine = 1
psTriangular = 2
psSquare = 3
PsWaveType = c_int # enum

# values for enumeration 'PsZigZagType'
psAroundCenter = 1
psOutFromCenter = 2
psPondRipples = 3
PsZigZagType = c_int # enum

# values for enumeration 'PsNoiseDistribution'
psUniformNoise = 1
psGaussianNoise = 2
PsNoiseDistribution = c_int # enum

# values for enumeration 'PsLensType'
psZoomLens = 1
psPrime35 = 2
psPrime105 = 3
psMoviePrime = 5
PsLensType = c_int # enum

# values for enumeration 'PsEliminateFields'
psOddFields = 1
psEvenFields = 2
PsEliminateFields = c_int # enum

# values for enumeration 'PsCreateFields'
psDuplication = 1
psInterpolation = 2
PsCreateFields = c_int # enum

# values for enumeration 'PsOffsetUndefinedAreas'
psOffsetSetToLayerFill = 1
psOffsetWrapAround = 2
psOffsetRepeatEdgePixels = 3
PsOffsetUndefinedAreas = c_int # enum

# values for enumeration 'PsAdjustmentReference'
psRelative = 1
psAbsolute = 2
PsAdjustmentReference = c_int # enum
ArtLayer._disp_methods_ = [
    DISPMETHOD([dispid(1179611235), helpstring('the interior opacity of the layer (between 0.0 and 100.0)'), 'propget'], c_double, 'FillOpacity'),
    DISPMETHOD([dispid(1179611235), helpstring('the interior opacity of the layer (between 0.0 and 100.0)'), 'propput'], None, 'FillOpacity',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1883731792), helpstring('is the layer grouped with the layer below?. Photoshop CS changed the menu name to Create/Release Clipping Mask'), 'propget'], VARIANT_BOOL, 'Grouped'),
    DISPMETHOD([dispid(1883731792), helpstring('is the layer grouped with the layer below?. Photoshop CS changed the menu name to Create/Release Clipping Mask'), 'propput'], None, 'Grouped',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1147292786), helpstring('is the layer a background layer?'), 'propget'], VARIANT_BOOL, 'IsBackgroundLayer'),
    DISPMETHOD([dispid(1147292786), helpstring('is the layer a background layer?'), 'propput'], None, 'IsBackgroundLayer',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1350061155), 'propget'], VARIANT_BOOL, 'PixelsLocked'),
    DISPMETHOD([dispid(1350061155), 'propput'], None, 'PixelsLocked',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349799011), 'propget'], VARIANT_BOOL, 'PositionLocked'),
    DISPMETHOD([dispid(1349799011), 'propput'], None, 'PositionLocked',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416645731), 'propget'], VARIANT_BOOL, 'TransparentPixelsLocked'),
    DISPMETHOD([dispid(1416645731), 'propput'], None, 'TransparentPixelsLocked',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1265200740), helpstring("to create a text layer set this property to 'text layer' on an empty art layer of type 'normal'"), 'propget'], PsLayerKind, 'Kind'),
    DISPMETHOD([dispid(1265200740), helpstring("to create a text layer set this property to 'text layer' on an empty art layer of type 'normal'"), 'propput'], None, 'Kind',
               ( [], PsLayerKind, 'rhs' )),
    DISPMETHOD([dispid(1884058196), helpstring("the text that is associated with the art layer. Only valid for art layers whose 'kind' is a text layer"), 'propget'], POINTER(TextItem), 'TextItem'),
    DISPMETHOD([dispid(1396927603), helpstring('The Layer corresponding to the ArtLayer'), 'hidden', 'propget'], POINTER(IDispatch), 'Layer'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1097616483), 'propget'], VARIANT_BOOL, 'AllLocked'),
    DISPMETHOD([dispid(1097616483), 'propput'], None, 'AllLocked',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1114393956), 'propget'], PsBlendMode, 'BlendMode'),
    DISPMETHOD([dispid(1114393956), 'propput'], None, 'BlendMode',
               ( [], PsBlendMode, 'rhs' )),
    DISPMETHOD([dispid(1282106724), 'propget'], VARIANT, 'LinkedLayers'),
    DISPMETHOD([dispid(1332765556), helpstring('master opacity of layer ( 0.0 - 100.0 )'), 'propget'], c_double, 'Opacity'),
    DISPMETHOD([dispid(1332765556), helpstring('master opacity of layer ( 0.0 - 100.0 )'), 'propput'], None, 'Opacity',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884705634), 'propget'], VARIANT_BOOL, 'Visible'),
    DISPMETHOD([dispid(1884705634), 'propput'], None, 'Visible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1229201440), helpstring('the unique ID of this layer'), 'propget'], c_int, 'id'),
    DISPMETHOD([dispid(1886603640), helpstring('the layer index sans layer groups, how Photoshop would index them'), 'propget'], c_int, 'ItemIndex'),
    DISPMETHOD([dispid(1954115685), helpstring('Type of the Layer'), 'hidden', 'propget'], PsLayerType, 'LayerType'),
    DISPMETHOD([dispid(1279358028), helpstring('If the Layer is a ArtLayer then this property will return a reference to the corresponding ArtLayer object'), 'hidden', 'propget'], POINTER(ArtLayer), 'ArtLayer'),
    DISPMETHOD([dispid(1279358042), helpstring('If the Layer is a LayerSet then this property will return a reference to the corresponding LayerSet object'), 'hidden', 'propget'], POINTER(LayerSet), 'LayerSet'),
    DISPMETHOD([dispid(1114530931), helpstring('Bounding rectangle of the Layer'), 'propget'], VARIANT, 'Bounds'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1097878643)], None, 'ApplyStyle',
               ( ['in'], BSTR, 'StyleName' )),
    DISPMETHOD([dispid(1296117809)], None, 'Clear'),
    DISPMETHOD([dispid(1668247673)], None, 'Copy',
               ( ['in', 'optional'], VARIANT, 'Merge' )),
    DISPMETHOD([dispid(1668641824)], None, 'Cut'),
    DISPMETHOD([dispid(1298615386), helpstring('merges the layer down. This will remove the layer from the document. The method returns a reference to the art layer that this layer is merged into')], POINTER(ArtLayer), 'Merge'),
    DISPMETHOD([dispid(1383298162)], None, 'Rasterize',
               ( ['in'], PsRasterizeType, 'Target' )),
    DISPMETHOD([dispid(1177563959), helpstring('apply the average filter')], None, 'ApplyAverage'),
    DISPMETHOD([dispid(1195535474), helpstring('apply the gaussian blur filter')], None, 'ApplyGaussianBlur',
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1282294380), helpstring('apply the lens blur filter')], None, 'ApplyLensBlur',
               ( ['in', 'optional'], VARIANT, 'Source' ),
               ( ['in', 'optional'], VARIANT, 'FocalDistance' ),
               ( ['in', 'optional'], VARIANT, 'InvertDepthMap' ),
               ( ['in', 'optional'], VARIANT, 'Shape' ),
               ( ['in', 'optional'], VARIANT, 'Radius' ),
               ( ['in', 'optional'], VARIANT, 'BladeCurvature' ),
               ( ['in', 'optional'], VARIANT, 'Rotation' ),
               ( ['in', 'optional'], VARIANT, 'Brightness' ),
               ( ['in', 'optional'], VARIANT, 'Threshold' ),
               ( ['in', 'optional'], VARIANT, 'Amount' ),
               ( ['in', 'optional'], VARIANT, 'Distribution' ),
               ( ['in', 'optional'], VARIANT, 'Monochromatic' )),
    DISPMETHOD([dispid(1177563185), helpstring('apply the blur filter')], None, 'ApplyBlur'),
    DISPMETHOD([dispid(1177563186), helpstring('apply the blur more filter')], None, 'ApplyBlurMore'),
    DISPMETHOD([dispid(1177563187), helpstring('apply the motion blur filter')], None, 'ApplyMotionBlur',
               ( ['in'], c_int, 'Angle' ),
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1177563188), helpstring('apply the radial blur filter')], None, 'ApplyRadialBlur',
               ( ['in'], c_int, 'Amount' ),
               ( ['in'], PsRadialBlurMethod, 'BlurMethod' ),
               ( ['in'], PsRadialBlurQuality, 'BlurQuality' ),
               ( ['in', 'optional'], VARIANT, 'BlurCenter' )),
    DISPMETHOD([dispid(1177563189), helpstring('apply the smart blur filter')], None, 'ApplySmartBlur',
               ( ['in'], c_double, 'Radius' ),
               ( ['in'], c_double, 'Threshold' ),
               ( ['in'], PsSmartBlurQuality, 'BlurQuality' ),
               ( ['in'], PsSmartBlurMode, 'Mode' )),
    DISPMETHOD([dispid(1177563190), helpstring('apply the diffuse glow filter')], None, 'ApplyDiffuseGlow',
               ( ['in'], c_int, 'Graininess' ),
               ( ['in'], c_int, 'GlowAmount' ),
               ( ['in'], c_int, 'ClearAmount' )),
    DISPMETHOD([dispid(1177563445), helpstring('apply the displace filter')], None, 'ApplyDisplace',
               ( ['in'], c_int, 'HorizontalScale' ),
               ( ['in'], c_int, 'VerticalScale' ),
               ( ['in'], PsDisplacementMapType, 'DisplacementType' ),
               ( ['in'], PsUndefinedAreas, 'UndefinedAreas' ),
               ( ['in'], BSTR, 'DisplacementMapFile' )),
    DISPMETHOD([dispid(1177563191), helpstring('apply the glass filter')], None, 'ApplyGlassEffect',
               ( ['in'], c_int, 'Distortion' ),
               ( ['in'], c_int, 'Smoothness' ),
               ( ['in'], c_int, 'Scaling' ),
               ( ['in', 'optional'], VARIANT, 'Invert' ),
               ( ['in', 'optional'], VARIANT, 'Texture' ),
               ( ['in', 'optional'], VARIANT, 'TextureFile' )),
    DISPMETHOD([dispid(1177563192), helpstring('apply the ocean ripple filter')], None, 'ApplyOceanRipple',
               ( ['in'], c_int, 'Size' ),
               ( ['in'], c_int, 'Magnitude' )),
    DISPMETHOD([dispid(1177563193), helpstring('apply the pinch filter')], None, 'ApplyPinch',
               ( ['in'], c_int, 'Amount' )),
    DISPMETHOD([dispid(1177563440), helpstring('apply the polar coordinates filter')], None, 'ApplyPolarCoordinates',
               ( ['in'], PsPolarConversionType, 'Conversion' )),
    DISPMETHOD([dispid(1177563441), helpstring('apply the ripple filter')], None, 'ApplyRipple',
               ( ['in'], c_int, 'Amount' ),
               ( ['in'], PsRippleSize, 'Size' )),
    DISPMETHOD([dispid(1177563442), helpstring('apply the shear filter')], None, 'ApplyShear',
               ( ['in'], VARIANT, 'Curve' ),
               ( ['in'], PsUndefinedAreas, 'UndefinedAreas' )),
    DISPMETHOD([dispid(1177563443), helpstring('apply the spherize filter')], None, 'ApplySpherize',
               ( ['in'], c_int, 'Amount' ),
               ( ['in'], PsSpherizeMode, 'Mode' )),
    DISPMETHOD([dispid(1177563444), helpstring('apply the twirl filter')], None, 'ApplyTwirl',
               ( ['in'], c_int, 'Angle' )),
    DISPMETHOD([dispid(1177563446), helpstring('apply the wave filter')], None, 'ApplyWave',
               ( ['in'], c_int, 'GeneratorNumber' ),
               ( ['in'], c_int, 'MinimumWavelength' ),
               ( ['in'], c_int, 'MaximumWavelength' ),
               ( ['in'], c_int, 'MinimumAmplitude' ),
               ( ['in'], c_int, 'MaximumAmplitude' ),
               ( ['in'], c_int, 'HorizontalScale' ),
               ( ['in'], c_int, 'VerticalScale' ),
               ( ['in'], PsWaveType, 'WaveType' ),
               ( ['in'], PsUndefinedAreas, 'UndefinedAreas' ),
               ( ['in'], c_int, 'RandomSeed' )),
    DISPMETHOD([dispid(1177563447), helpstring('apply the zigzag filter')], None, 'ApplyZigZag',
               ( ['in'], c_int, 'Amount' ),
               ( ['in'], c_int, 'Ridges' ),
               ( ['in'], PsZigZagType, 'Style' )),
    DISPMETHOD([dispid(1177563448), helpstring('apply the add noise filter')], None, 'ApplyAddNoise',
               ( ['in'], c_double, 'Amount' ),
               ( ['in'], PsNoiseDistribution, 'Distribution' ),
               ( ['in'], VARIANT_BOOL, 'Monochromatic' )),
    DISPMETHOD([dispid(1177563449), helpstring('apply the despeckle filter')], None, 'ApplyDespeckle'),
    DISPMETHOD([dispid(1177563696), helpstring('apply the dust and scratches filter')], None, 'ApplyDustAndScratches',
               ( ['in'], c_int, 'Radius' ),
               ( ['in'], c_int, 'Threshold' )),
    DISPMETHOD([dispid(1177563697), helpstring('apply the median noise filter')], None, 'ApplyMedianNoise',
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1177563953), helpstring('apply the clouds filter')], None, 'ApplyClouds'),
    DISPMETHOD([dispid(1177563954), helpstring('apply the difference clouds filter')], None, 'ApplyDifferenceClouds'),
    DISPMETHOD([dispid(1177563955), helpstring('apply the lens flare filter')], None, 'ApplyLensFlare',
               ( ['in'], c_int, 'Brightness' ),
               ( ['in'], VARIANT, 'FlareCenter' ),
               ( ['in'], PsLensType, 'LensType' )),
    DISPMETHOD([dispid(1177563956), helpstring('apply the texture fill filter')], None, 'ApplyTextureFill',
               ( ['in'], BSTR, 'TextureFile' )),
    DISPMETHOD([dispid(1177563698), helpstring('apply the sharpen filter')], None, 'ApplySharpen'),
    DISPMETHOD([dispid(1177563699), helpstring('apply the sharpen edges filter')], None, 'ApplySharpenEdges'),
    DISPMETHOD([dispid(1177563700), helpstring('apply the sharpen more filter')], None, 'ApplySharpenMore'),
    DISPMETHOD([dispid(1177563701), helpstring('apply the unsharp mask filter')], None, 'ApplyUnSharpMask',
               ( ['in'], c_double, 'Amount' ),
               ( ['in'], c_double, 'Radius' ),
               ( ['in'], c_int, 'Threshold' )),
    DISPMETHOD([dispid(1177563957), helpstring('apply the de-interlace filter')], None, 'ApplyDeInterlace',
               ( ['in'], PsEliminateFields, 'EliminateFields' ),
               ( ['in'], PsCreateFields, 'CreateFields' )),
    DISPMETHOD([dispid(1177563958), helpstring('apply the NTSC colors filter')], None, 'ApplyNTSC'),
    DISPMETHOD([dispid(1177563702), helpstring('apply the custom filter')], None, 'ApplyCustomFilter',
               ( ['in'], VARIANT, 'Characteristics' ),
               ( ['in'], c_int, 'Scale' ),
               ( ['in'], c_int, 'Offset' )),
    DISPMETHOD([dispid(1177563952), helpstring('apply the high pass filter')], None, 'ApplyHighPass',
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1177563703), helpstring('apply the maximum filter')], None, 'ApplyMaximum',
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1177563704), helpstring('apply the minimum filter')], None, 'ApplyMinimum',
               ( ['in'], c_double, 'Radius' )),
    DISPMETHOD([dispid(1177563705), helpstring('apply the offset filter')], None, 'ApplyOffset',
               ( ['in'], c_double, 'Horizontal' ),
               ( ['in'], c_double, 'Vertical' ),
               ( ['in'], PsOffsetUndefinedAreas, 'UndefinedAreas' )),
    DISPMETHOD([dispid(1097084977), helpstring('adjust levels of the selected channels')], None, 'AdjustLevels',
               ( ['in'], c_int, 'InputRangeStart' ),
               ( ['in'], c_int, 'InputRangeEnd' ),
               ( ['in'], c_double, 'InputRangeGamma' ),
               ( ['in'], c_int, 'OutputRangeStart' ),
               ( ['in'], c_int, 'OutputRangeEnd' )),
    DISPMETHOD([dispid(1094856753), helpstring('adjust levels of the selected channels using auto levels option')], None, 'AutoLevels'),
    DISPMETHOD([dispid(1097084978), helpstring('adjust contrast of the selected channels automatically')], None, 'AutoContrast'),
    DISPMETHOD([dispid(1097084979), helpstring('adjust curves of the selected channels')], None, 'AdjustCurves',
               ( ['in'], VARIANT, 'CurveShape' )),
    DISPMETHOD([dispid(1097084980), helpstring('adjust brightness and constrast')], None, 'AdjustBrightnessContrast',
               ( ['in'], c_int, 'Brightness' ),
               ( ['in'], c_int, 'Contrast' )),
    DISPMETHOD([dispid(1097084981)], None, 'AdjustColorBalance',
               ( ['in', 'optional'], VARIANT, 'Shadows' ),
               ( ['in', 'optional'], VARIANT, 'Midtones' ),
               ( ['in', 'optional'], VARIANT, 'Highlights' ),
               ( ['in', 'optional'], VARIANT, 'PreserveLuminosity' )),
    DISPMETHOD([dispid(1097084982)], None, 'Desaturate'),
    DISPMETHOD([dispid(1097084983)], None, 'SelectiveColor',
               ( ['in'], PsAdjustmentReference, 'SelectionMethod' ),
               ( ['in', 'optional'], VARIANT, 'Reds' ),
               ( ['in', 'optional'], VARIANT, 'Yellows' ),
               ( ['in', 'optional'], VARIANT, 'Greens' ),
               ( ['in', 'optional'], VARIANT, 'Cyans' ),
               ( ['in', 'optional'], VARIANT, 'Blues' ),
               ( ['in', 'optional'], VARIANT, 'Magentas' ),
               ( ['in', 'optional'], VARIANT, 'Whites' ),
               ( ['in', 'optional'], VARIANT, 'Neutrals' ),
               ( ['in', 'optional'], VARIANT, 'Blacks' )),
    DISPMETHOD([dispid(1097084984), helpstring('only valid for RGB or CMYK documents')], None, 'MixChannels',
               ( ['in'], VARIANT, 'OutputChannels' ),
               ( ['in', 'optional'], VARIANT, 'Monochrome' )),
    DISPMETHOD([dispid(1767272302), helpstring('inverts the currently selected layer or channels')], None, 'Invert'),
    DISPMETHOD([dispid(1097084985), helpstring('equalize the levels')], None, 'Equalize'),
    DISPMETHOD([dispid(1097085233)], None, 'Threshold',
               ( ['in'], c_int, 'Level' )),
    DISPMETHOD([dispid(1097085232)], None, 'Posterize',
               ( ['in'], c_int, 'Levels' )),
    DISPMETHOD([dispid(1097085234)], None, 'PhotoFilter',
               ( ['in', 'optional'], VARIANT, 'FillColor' ),
               ( ['in', 'optional'], VARIANT, 'Density' ),
               ( ['in', 'optional'], VARIANT, 'PreserveLuminosity' )),
    DISPMETHOD([dispid(1397239857)], None, 'ShadowHighlight',
               ( ['in', 'optional'], VARIANT, 'ShadowAmount' ),
               ( ['in', 'optional'], VARIANT, 'ShadowWidth' ),
               ( ['in', 'optional'], VARIANT, 'ShadowRaduis' ),
               ( ['in', 'optional'], VARIANT, 'HighlightAmount' ),
               ( ['in', 'optional'], VARIANT, 'HighlightWidth' ),
               ( ['in', 'optional'], VARIANT, 'HighlightRaduis' ),
               ( ['in', 'optional'], VARIANT, 'ColorCorrection' ),
               ( ['in', 'optional'], VARIANT, 'MidtoneContrast' ),
               ( ['in', 'optional'], VARIANT, 'BlackClip' ),
               ( ['in', 'optional'], VARIANT, 'WhiteClip' )),
    DISPMETHOD([dispid(1433169515), helpstring('unlink the layer')], None, 'Unlink'),
    DISPMETHOD([dispid(1818973295), helpstring('link the layer with another layer')], None, 'Link',
               ( ['in'], POINTER(IDispatch), 'With' )),
    DISPMETHOD([dispid(1299599475), helpstring('moves the position relative to its current position')], None, 'Translate',
               ( ['in', 'optional'], VARIANT, 'DeltaX' ),
               ( ['in', 'optional'], VARIANT, 'DeltaY' )),
    DISPMETHOD([dispid(1383036001)], None, 'Rotate',
               ( ['in'], c_double, 'Angle' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1399024741)], None, 'Resize',
               ( ['in', 'optional'], VARIANT, 'Horizontal' ),
               ( ['in', 'optional'], VARIANT, 'Vertical' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1299596646), helpstring('Move the PageItem to beginning of container'), 'hidden'], None, 'MoveToBeginning',
               ( ['in'], POINTER(IDispatch), 'Container' )),
    DISPMETHOD([dispid(1299596645), helpstring('Move the PageItem to end of container'), 'hidden'], None, 'MoveToEnd',
               ( ['in'], POINTER(IDispatch), 'Container' )),
    DISPMETHOD([dispid(1299596642), helpstring('Move the PageItem in front of object'), 'hidden'], None, 'MoveBefore',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' )),
    DISPMETHOD([dispid(1299596641), helpstring('Move the PageItem in behind object'), 'hidden'], None, 'MoveAfter',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' )),
    DISPMETHOD([dispid(1668050798), helpstring('create a duplicate of the object')], POINTER(IDispatch), 'Duplicate',
               ( ['in', 'optional'], VARIANT, 'RelativeObject' ),
               ( ['in', 'optional'], VARIANT, 'InsertionLocation' )),
    DISPMETHOD([dispid(1836021349), helpstring('move the object')], None, 'Move',
               ( ['in'], POINTER(IDispatch), 'RelativeObject' ),
               ( ['in'], PsElementPlacement, 'InsertionLocation' )),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]

# values for enumeration 'PsBitsPerChannelType'
psDocument1Bit = 1
psDocument8Bits = 8
psDocument16Bits = 16
psDocument32Bits = 32
PsBitsPerChannelType = c_int # enum

# values for enumeration 'PsColorProfileType'
psNo = 1
psWorking = 2
psCustom = 3
PsColorProfileType = c_int # enum

# values for enumeration 'PsDocumentMode'
psGrayscale = 1
psRGB = 2
psCMYK = 3
psLab = 4
psBitmap = 5
psIndexedColor = 6
psMultiChannel = 7
psDuotone = 8
PsDocumentMode = c_int # enum
class HistoryState(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A history state for the document'
    _iid_ = GUID('{EDC373C3-FE30-40BA-A31C-0251CA7456F1}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
HistoryState._disp_methods_ = [
    DISPMETHOD([dispid(1886282093), helpstring("the history state's name"), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1213425780), helpstring('is the history state a snapshot?'), 'propget'], VARIANT_BOOL, 'Snapshot'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
class DocumentInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Document information'
    _iid_ = GUID('{746FEF90-A182-4BD0-A4F6-BB6BBAE87A78}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsCopyrightedType'
psCopyrightedWork = 1
psPublicDomain = 2
psUnmarked = 3
PsCopyrightedType = c_int # enum

# values for enumeration 'PsUrgency'
psNone = 0
psLow = 1
psTwo = 2
psThree = 3
psFour = 4
psNormal = 5
psSix = 6
psSeven = 7
psHigh = 8
PsUrgency = c_int # enum
DocumentInfo._disp_methods_ = [
    DISPMETHOD([dispid(1147744818), 'propget'], BSTR, 'Title'),
    DISPMETHOD([dispid(1147744818), 'propput'], None, 'Title',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744817), 'propget'], BSTR, 'Author'),
    DISPMETHOD([dispid(1147744817), 'propput'], None, 'Author',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744819), 'propget'], BSTR, 'AuthorPosition'),
    DISPMETHOD([dispid(1147744819), 'propput'], None, 'AuthorPosition',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744305), 'propget'], BSTR, 'Caption'),
    DISPMETHOD([dispid(1147744305), 'propput'], None, 'Caption',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744306), 'propget'], BSTR, 'CaptionWriter'),
    DISPMETHOD([dispid(1147744306), 'propput'], None, 'CaptionWriter',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744820), 'propget'], BSTR, 'JobName'),
    DISPMETHOD([dispid(1147744820), 'propput'], None, 'JobName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744569), 'propget'], PsCopyrightedType, 'Copyrighted'),
    DISPMETHOD([dispid(1147744569), 'propput'], None, 'Copyrighted',
               ( [], PsCopyrightedType, 'rhs' )),
    DISPMETHOD([dispid(1147744816), 'propget'], BSTR, 'CopyrightNotice'),
    DISPMETHOD([dispid(1147744816), 'propput'], None, 'CopyrightNotice',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1884648044), 'propget'], BSTR, 'OwnerUrl'),
    DISPMETHOD([dispid(1884648044), 'propput'], None, 'OwnerUrl',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744309), helpstring('list of keywords'), 'propget'], VARIANT, 'Keywords'),
    DISPMETHOD([dispid(1147744309), helpstring('list of keywords'), 'propput'], None, 'Keywords',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1147744310), 'propget'], BSTR, 'Category'),
    DISPMETHOD([dispid(1147744310), 'propput'], None, 'Category',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744311), 'propget'], VARIANT, 'SupplementalCategories'),
    DISPMETHOD([dispid(1147744311), 'propput'], None, 'SupplementalCategories',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1147744564), 'propget'], BSTR, 'CreationDate'),
    DISPMETHOD([dispid(1147744564), 'propput'], None, 'CreationDate',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744565), 'propget'], BSTR, 'City'),
    DISPMETHOD([dispid(1147744565), 'propput'], None, 'City',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744566), 'propget'], BSTR, 'ProvinceState'),
    DISPMETHOD([dispid(1147744566), 'propput'], None, 'ProvinceState',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744567), 'propget'], BSTR, 'Country'),
    DISPMETHOD([dispid(1147744567), 'propput'], None, 'Country',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744561), 'propget'], BSTR, 'Credit'),
    DISPMETHOD([dispid(1147744561), 'propput'], None, 'Credit',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744562), 'propget'], BSTR, 'Source'),
    DISPMETHOD([dispid(1147744562), 'propput'], None, 'Source',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744307), 'propget'], BSTR, 'Headline'),
    DISPMETHOD([dispid(1147744307), 'propput'], None, 'Headline',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744308), 'propget'], BSTR, 'Instructions'),
    DISPMETHOD([dispid(1147744308), 'propput'], None, 'Instructions',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744568), 'propget'], BSTR, 'TransmissionReference'),
    DISPMETHOD([dispid(1147744568), 'propput'], None, 'TransmissionReference',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1147744312), 'propget'], PsUrgency, 'Urgency'),
    DISPMETHOD([dispid(1147744312), 'propput'], None, 'Urgency',
               ( [], PsUrgency, 'rhs' )),
    DISPMETHOD([dispid(1147744821), 'propget'], VARIANT, 'EXIF'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
class Selection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The selection of the document'
    _iid_ = GUID('{09DA6B10-9684-44EE-A575-01F54660BDDC}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
class Channel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A channel in a document. Can be either a component channel representing a color of the document color model or an alpha channel'
    _iid_ = GUID('{4B9E6B85-0613-4873-8AB7-575CD2226768}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
Channel._disp_methods_ = [
    DISPMETHOD([dispid(1214870388), helpstring('a histogram of values for the channel'), 'propget'], VARIANT, 'Histogram'),
    DISPMETHOD([dispid(1886282093), helpstring("the channel's name"), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring("the channel's name"), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1265200740), helpstring('type of the channel'), 'propget'], PsChannelType, 'Kind'),
    DISPMETHOD([dispid(1265200740), helpstring('type of the channel'), 'propput'], None, 'Kind',
               ( [], PsChannelType, 'rhs' )),
    DISPMETHOD([dispid(1332765556), helpstring('opacity of alpha channels (called solidity for spot channels)'), 'propget'], c_double, 'Opacity'),
    DISPMETHOD([dispid(1332765556), helpstring('opacity of alpha channels (called solidity for spot channels)'), 'propput'], None, 'Opacity',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884705634), 'propget'], VARIANT_BOOL, 'Visible'),
    DISPMETHOD([dispid(1884705634), 'propput'], None, 'Visible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1883456323), helpstring('color of the channel (not valid for component channels)'), 'propget'], POINTER(_SolidColor), 'Color'),
    DISPMETHOD([dispid(1883456323), helpstring('color of the channel (not valid for component channels)'), 'propput'], None, 'Color',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1883456323), helpstring('color of the channel (not valid for component channels)'), 'propputref'], None, 'Color',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1296849475), helpstring('merge a spot channel into the component channels')], None, 'Merge'),
    DISPMETHOD([dispid(1148207976), helpstring('duplicate the channel')], POINTER(Channel), 'Duplicate',
               ( ['in', 'optional'], VARIANT, 'TargetDocument' )),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
Selection._disp_methods_ = [
    DISPMETHOD([dispid(1114530931), helpstring('bounding rectangle of the entire selection'), 'propget'], VARIANT, 'Bounds'),
    DISPMETHOD([dispid(1399613796), helpstring('is the bounding rectangle a solid rectangle'), 'propget'], VARIANT_BOOL, 'Solid'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1296117809), helpstring('clear selection')], None, 'Clear'),
    DISPMETHOD([dispid(1668247673), helpstring('copy selection to the clipboard')], None, 'Copy',
               ( ['in', 'optional'], VARIANT, 'Merge' )),
    DISPMETHOD([dispid(1668641824), helpstring('cut current selection to the clipboard')], None, 'Cut'),
    DISPMETHOD([dispid(1114793074), helpstring('select the border of the selection')], None, 'SelectBorder',
               ( ['in'], c_double, 'Width' )),
    DISPMETHOD([dispid(1396929650), helpstring('contracts the selection')], None, 'Contract',
               ( ['in'], c_double, 'By' )),
    DISPMETHOD([dispid(1181314156), helpstring('fills the selection')], None, 'Fill',
               ( ['in'], VARIANT, 'FillType' ),
               ( ['in', 'optional'], VARIANT, 'Mode' ),
               ( ['in', 'optional'], VARIANT, 'Opacity' ),
               ( ['in', 'optional'], VARIANT, 'PreserveTransparency' )),
    DISPMETHOD([dispid(1400138597), helpstring('strokes the selection')], None, 'Stroke',
               ( ['in'], VARIANT, 'StrokeColor' ),
               ( ['in'], c_int, 'Width' ),
               ( ['in', 'optional'], VARIANT, 'Location' ),
               ( ['in', 'optional'], VARIANT, 'Mode' ),
               ( ['in', 'optional'], VARIANT, 'Opacity' ),
               ( ['in', 'optional'], VARIANT, 'PreserveTransparency' )),
    DISPMETHOD([dispid(1399013740)], None, 'SelectAll'),
    DISPMETHOD([dispid(1148415092)], None, 'Deselect'),
    DISPMETHOD([dispid(1936483188)], None, 'Select',
               ( ['in'], VARIANT, 'Region' ),
               ( ['in', 'optional'], VARIANT, 'Type' ),
               ( ['in', 'optional'], VARIANT, 'Feather' ),
               ( ['in', 'optional'], VARIANT, 'AntiAlias' )),
    DISPMETHOD([dispid(1483763300), helpstring('expand selection')], None, 'Expand',
               ( ['in'], c_double, 'By' )),
    DISPMETHOD([dispid(1182034034), helpstring('feather edges of selection')], None, 'Feather',
               ( ['in'], c_double, 'By' )),
    DISPMETHOD([dispid(1198681975), helpstring('grow selection to include all adjacent pixels falling within the specified tolerance range')], None, 'Grow',
               ( ['in'], c_int, 'Tolerance' ),
               ( ['in'], VARIANT_BOOL, 'AntiAlias' )),
    DISPMETHOD([dispid(1232491372), helpstring('invert the selection')], None, 'Invert'),
    DISPMETHOD([dispid(1399680114), helpstring('grow selection to include pixels throughout the image falling within the tolerance range')], None, 'Similar',
               ( ['in'], c_int, 'Tolerance' ),
               ( ['in'], VARIANT_BOOL, 'AntiAlias' )),
    DISPMETHOD([dispid(1347646568)], None, 'Smooth',
               ( ['in'], c_int, 'Radius' )),
    DISPMETHOD([dispid(1400263532), helpstring('save the selection as a channel')], None, 'Store',
               ( ['in'], POINTER(Channel), 'Into' ),
               ( ['in', 'optional'], VARIANT, 'Combination' )),
    DISPMETHOD([dispid(1281643372), helpstring('load the selection from a channel')], None, 'Load',
               ( ['in'], POINTER(Channel), 'From' ),
               ( ['in', 'optional'], VARIANT, 'Combination' ),
               ( ['in', 'optional'], VARIANT, 'Inverting' )),
    DISPMETHOD([dispid(1299599475), helpstring('moves the position relative to its current position')], None, 'Translate',
               ( ['in', 'optional'], VARIANT, 'DeltaX' ),
               ( ['in', 'optional'], VARIANT, 'DeltaY' )),
    DISPMETHOD([dispid(1299595876), helpstring('moves the boundary of selection relative to its current position')], None, 'TranslateBoundary',
               ( ['in', 'optional'], VARIANT, 'DeltaX' ),
               ( ['in', 'optional'], VARIANT, 'DeltaY' )),
    DISPMETHOD([dispid(1383036001)], None, 'Rotate',
               ( ['in'], c_double, 'Angle' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1383035970), helpstring('rotates the boundary of selection')], None, 'RotateBoundary',
               ( ['in'], c_double, 'Angle' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1399024741)], None, 'Resize',
               ( ['in', 'optional'], VARIANT, 'Horizontal' ),
               ( ['in', 'optional'], VARIANT, 'Vertical' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1399013988), helpstring('scale the boundary of selection')], None, 'ResizeBoundary',
               ( ['in', 'optional'], VARIANT, 'Horizontal' ),
               ( ['in', 'optional'], VARIANT, 'Vertical' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1347694902), helpstring('make this selection item the work path for this document')], None, 'MakeWorkPath',
               ( ['in', 'optional'], VARIANT, 'Tolerance' )),
]
class XMPMetadata(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DC865034-A587-4CC4-8A5A-453032562BE4}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
XMPMetadata._disp_methods_ = [
    DISPMETHOD([dispid(1884441956), helpstring('raw XML form of file information'), 'propget'], BSTR, 'RawData'),
    DISPMETHOD([dispid(1884441956), helpstring('raw XML form of file information'), 'propput'], None, 'RawData',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
class MeasurementScale(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Document Measurement Scale'
    _iid_ = GUID('{632F36B3-1D76-48BE-ADC3-D7FB62A0C2FB}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
MeasurementScale._disp_methods_ = [
    DISPMETHOD([dispid(1886282093), helpstring('the name of this scale'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of this scale'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1836281964), helpstring('the length in pixels this scale equates to'), 'propget'], c_int, 'PixelLength'),
    DISPMETHOD([dispid(1836281964), helpstring('the length in pixels this scale equates to'), 'propput'], None, 'PixelLength',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1836280940), helpstring('the logical length this scale equates to'), 'propget'], c_double, 'LogicalLength'),
    DISPMETHOD([dispid(1836280940), helpstring('the logical length this scale equates to'), 'propput'], None, 'LogicalLength',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1836280949), helpstring('the logical units for this scale'), 'propget'], BSTR, 'LogicalUnits'),
    DISPMETHOD([dispid(1836280949), helpstring('the logical units for this scale'), 'propput'], None, 'LogicalUnits',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
class Channels(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Channels of the document'
    _iid_ = GUID('{2DC64F97-8C69-4016-A8EB-89A00217291F}')
    _idlflags_ = []
    _methods_ = []
Channels._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1684368495), helpstring('Delete an element from the collection'), 'hidden'], None, 'Remove',
               ( ['in'], POINTER(Channel), 'Item' )),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(Channel), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(Channel), 'ItemPtr' )),
    DISPMETHOD([dispid(1665353838), helpstring('create a new object')], POINTER(Channel), 'Add'),
]
class HistoryStates(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'History states associated with the document'
    _iid_ = GUID('{69172A3F-E06E-42E6-B733-4DC36E2AC948}')
    _idlflags_ = []
    _methods_ = []
HistoryStates._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(HistoryState), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(HistoryState), 'ItemPtr' )),
]
class LayerComps(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Layer compositions associated with the document'
    _iid_ = GUID('{726B458C-74B0-47AE-B390-99753B55DF2E}')
    _idlflags_ = []
    _methods_ = []
class LayerComp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A layer composition in a document'
    _iid_ = GUID('{9A37A0AC-E951-4B16-A548-886B77338DE0}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
LayerComp._disp_methods_ = [
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer comp'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the layer comp'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1279471666), helpstring('the description of the layer comp'), 'propget'], VARIANT, 'Comment'),
    DISPMETHOD([dispid(1279471666), helpstring('the description of the layer comp'), 'propput'], None, 'Comment',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1279471667), helpstring('use layer appearance'), 'propget'], VARIANT_BOOL, 'Appearance'),
    DISPMETHOD([dispid(1279471667), helpstring('use layer appearance'), 'propput'], None, 'Appearance',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1332897646), helpstring('use layer position'), 'propget'], VARIANT_BOOL, 'Position'),
    DISPMETHOD([dispid(1332897646), helpstring('use layer position'), 'propput'], None, 'Position',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1279471669), helpstring('use layer visibility'), 'propget'], VARIANT_BOOL, 'Visibility'),
    DISPMETHOD([dispid(1279471669), helpstring('use layer visibility'), 'propput'], None, 'Visibility',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1279471670), helpstring('the layer comp is currently selected'), 'propget'], VARIANT_BOOL, 'Selected'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1346842673), helpstring('apply the layer comp to the document')], None, 'Apply'),
    DISPMETHOD([dispid(1346842674), helpstring('recapture the current layer state(s) for this layer comp')], None, 'Recapture'),
    DISPMETHOD([dispid(1346844210), helpstring('reset the layer comp state to the document state')], None, 'ResetFromComp'),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
LayerComps._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(LayerComp), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(LayerComp), 'ItemPtr' )),
    DISPMETHOD([dispid(1279471665), helpstring('a layer comp')], POINTER(LayerComp), 'Add',
               ( ['in'], BSTR, 'Name' ),
               ( ['in', 'optional'], VARIANT, 'Comment' ),
               ( ['in', 'optional'], VARIANT, 'Appearance' ),
               ( ['in', 'optional'], VARIANT, 'Position' ),
               ( ['in', 'optional'], VARIANT, 'Visibility' )),
]
class PathItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'art paths associated with this document'
    _iid_ = GUID('{91B5F8AE-3CC5-4775-BCD3-FF1E0724BB01}')
    _idlflags_ = []
    _methods_ = []
class PathItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An artwork path item'
    _iid_ = GUID('{8B0CB532-4ACC-4BF3-9E42-0949B679D120}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
class SubPathItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'art sub paths associated with the path item'
    _iid_ = GUID('{B7283EEC-23B1-49A6-B151-0E97E4AF353C}')
    _idlflags_ = []
    _methods_ = []
class SubPathItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An artwork sub path item'
    _iid_ = GUID('{B6D22EB9-EC6D-46DB-B52A-5561433A1217}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsShapeOperation'
psShapeAdd = 1
psShapeXOR = 2
psShapeIntersect = 3
psShapeSubtract = 4
PsShapeOperation = c_int # enum
class PathPoints(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of path points'
    _iid_ = GUID('{8214A53C-0E67-49D4-A65A-D56F07B17D37}')
    _idlflags_ = []
    _methods_ = []
class PathPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A point on a path'
    _iid_ = GUID('{7D14BA29-1672-482F-8F48-9DA1E94800FD}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsPointKind'
psSmoothPoint = 1
psCornerPoint = 2
PsPointKind = c_int # enum
PathPoint._disp_methods_ = [
    DISPMETHOD([dispid(1347694904), helpstring('the position (coordinates) of the anchor point'), 'propget'], VARIANT, 'Anchor'),
    DISPMETHOD([dispid(1347694905), helpstring('location of the left direction point (in position)'), 'propget'], VARIANT, 'LeftDirection'),
    DISPMETHOD([dispid(1347695152), helpstring('location of the right direction point (out position)'), 'propget'], VARIANT, 'RightDirection'),
    DISPMETHOD([dispid(1265200740), helpstring('the type of point: smooth/corner'), 'propget'], PsPointKind, 'Kind'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
PathPoints._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(PathPoint), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(PathPoint), 'ItemPtr' )),
]
SubPathItem._disp_methods_ = [
    DISPMETHOD([dispid(1347695920), helpstring('is this path closed?'), 'propget'], VARIANT_BOOL, 'Closed'),
    DISPMETHOD([dispid(1347694647), helpstring('sub path operation on other sub paths'), 'propget'], PsShapeOperation, 'Operation'),
    DISPMETHOD([dispid(1347694644), 'propget'], POINTER(PathPoints), 'PathPoints'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
SubPathItems._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(SubPathItem), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(SubPathItem), 'ItemPtr' )),
]

# values for enumeration 'PsPathKind'
psNormalPath = 1
psClippingPath = 2
psWorkPath = 3
psVectorMask = 4
psTextMask = 5
PsPathKind = c_int # enum
PathItem._disp_methods_ = [
    DISPMETHOD([dispid(1886282093), helpstring('the name of the path item'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('the name of the path item'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1347695667), helpstring('sub items for this path item'), 'propget'], POINTER(SubPathItems), 'SubPathItems'),
    DISPMETHOD([dispid(1265200740), 'propget'], PsPathKind, 'Kind'),
    DISPMETHOD([dispid(1265200740), 'propput'], None, 'Kind',
               ( [], PsPathKind, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668050798), helpstring('duplicate this path')], POINTER(PathItem), 'Duplicate',
               ( ['in', 'optional'], VARIANT, 'Name' )),
    DISPMETHOD([dispid(1347694899), helpstring('make a selection from this path')], None, 'MakeSelection',
               ( ['in', 'optional'], VARIANT, 'Feather' ),
               ( ['in', 'optional'], VARIANT, 'AntiAlias' ),
               ( ['in', 'optional'], VARIANT, 'Operation' )),
    DISPMETHOD([dispid(1347694900), helpstring('fill the path with the following information')], None, 'FillPath',
               ( ['in', 'optional'], VARIANT, 'FillColor' ),
               ( ['in', 'optional'], VARIANT, 'Mode' ),
               ( ['in', 'optional'], VARIANT, 'Opacity' ),
               ( ['in', 'optional'], VARIANT, 'PreserveTransparency' ),
               ( ['in', 'optional'], VARIANT, 'Feather' ),
               ( ['in', 'optional'], VARIANT, 'AntiAlias' ),
               ( ['in', 'optional'], VARIANT, 'WholePath' )),
    DISPMETHOD([dispid(1347694901), helpstring('stroke the path with the following information')], None, 'StrokePath',
               ( ['in', 'optional'], VARIANT, 'Tool' ),
               ( ['in', 'optional'], VARIANT, 'SimulatePressure' )),
    DISPMETHOD([dispid(1347694903), helpstring('make this path item the clipping path for this document')], None, 'MakeClippingPath',
               ( ['in', 'optional'], VARIANT, 'Flatness' )),
    DISPMETHOD([dispid(1936483188), helpstring('make this path item the active or selected path item')], None, 'Select'),
    DISPMETHOD([dispid(1148415092), helpstring('unselect this path item, no paths items are selected')], None, 'Deselect'),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
PathItems._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(PathItem), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(PathItem), 'ItemPtr' )),
    DISPMETHOD([dispid(1347694643), helpstring('create a new path item')], POINTER(PathItem), 'Add',
               ( ['in'], BSTR, 'Name' ),
               ( ['in'], VARIANT, 'EntirePath' )),
]
class CountItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of count items'
    _iid_ = GUID('{9E01C1DA-DF69-4C2C-85EC-616370DF1CF0}')
    _idlflags_ = []
    _methods_ = []
class CountItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A counted item in a document. See the counting tool.'
    _iid_ = GUID('{66869370-9672-492D-93AC-0ADD62F427F1}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
CountItem._disp_methods_ = [
    DISPMETHOD([dispid(1332897646), helpstring('position of count item (unit value)'), 'propget'], VARIANT, 'Position'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
CountItems._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(CountItem), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(CountItem), 'ItemPtr' )),
    DISPMETHOD([dispid(1129590835), helpstring('a count item')], POINTER(CountItem), 'Add',
               ( ['in'], VARIANT, 'Position' )),
]
class ColorSamplers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of color samplers'
    _iid_ = GUID('{97C81476-3F5D-4934-8CAA-1ED0242105B0}')
    _idlflags_ = []
    _methods_ = []
class ColorSampler(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A color sampler in a document. See the color sampler tool.'
    _iid_ = GUID('{B125A66B-4C94-4E55-AF2F-57EC4DCB484B}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
ColorSampler._disp_methods_ = [
    DISPMETHOD([dispid(1332897646), helpstring('position of the color sampler (unit value)'), 'propget'], VARIANT, 'Position'),
    DISPMETHOD([dispid(1883456323), helpstring('color of the color sampler'), 'propget'], POINTER(_SolidColor), 'Color'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1129534261), helpstring('move the color sampler to a new location')], None, 'Move',
               ( ['in'], VARIANT, 'Position' )),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
ColorSamplers._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(ColorSampler), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(ColorSampler), 'ItemPtr' )),
    DISPMETHOD([dispid(1129534256), helpstring('a color sampler')], POINTER(ColorSampler), 'Add',
               ( ['in'], VARIANT, 'Position' )),
]

# values for enumeration 'PsIntent'
psPerceptual = 1
psSaturation = 2
psRelativeColorimetric = 3
psAbsoluteColorimetric = 4
PsIntent = c_int # enum

# values for enumeration 'PsChangeMode'
psConvertToGrayscale = 1
psConvertToRGB = 2
psConvertToCMYK = 3
psConvertToLab = 4
psConvertToBitmap = 5
psConvertToIndexedColor = 6
psConvertToMultiChannel = 7
PsChangeMode = c_int # enum
Document._disp_methods_ = [
    DISPMETHOD([dispid(1147292786), helpstring('The background layer for the document. Only valid for documents that have a background layer'), 'propget'], POINTER(ArtLayer), 'BackgroundLayer'),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propget'], PsBitsPerChannelType, 'BitsPerChannel'),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propput'], None, 'BitsPerChannel',
               ( [], PsBitsPerChannelType, 'rhs' )),
    DISPMETHOD([dispid(1147367508), helpstring('Type of color profile management for document.  Note: If you want to set a custom color profile, do not set a value for color profile kind; rather, set the appropriate color profile name.'), 'propget'], PsColorProfileType, 'ColorProfileType'),
    DISPMETHOD([dispid(1147367508), helpstring('Type of color profile management for document.  Note: If you want to set a custom color profile, do not set a value for color profile kind; rather, set the appropriate color profile name.'), 'propput'], None, 'ColorProfileType',
               ( [], PsColorProfileType, 'rhs' )),
    DISPMETHOD([dispid(1147367502), helpstring('Name of color profile for document. Valid when no value is specified for color profile kind (to indicate a custom color profile).'), 'propget'], BSTR, 'ColorProfileName'),
    DISPMETHOD([dispid(1147367502), helpstring('Name of color profile for document. Valid when no value is specified for color profile kind (to indicate a custom color profile).'), 'propput'], None, 'ColorProfileName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1330472037), helpstring('document mode'), 'propget'], PsDocumentMode, 'Mode'),
    DISPMETHOD([dispid(1128493171), helpstring('all color component channels for this document'), 'propget'], VARIANT, 'ComponentChannels'),
    DISPMETHOD([dispid(1145268339), helpstring('the current history state for this document'), 'propget'], POINTER(HistoryState), 'ActiveHistoryState'),
    DISPMETHOD([dispid(1145268339), helpstring('the current history state for this document'), 'propput'], None, 'ActiveHistoryState',
               ( [], POINTER(HistoryState), 'rhs' )),
    DISPMETHOD([dispid(1145266802), helpstring('the current history state to use with the history brush for this document'), 'propget'], POINTER(HistoryState), 'ActiveHistoryBrushSource'),
    DISPMETHOD([dispid(1145266802), helpstring('the current history state to use with the history brush for this document'), 'propput'], None, 'ActiveHistoryBrushSource',
               ( [], POINTER(HistoryState), 'rhs' )),
    DISPMETHOD([dispid(1668435058), helpstring('selected layer for document'), 'propget'], POINTER(IDispatch), 'ActiveLayer'),
    DISPMETHOD([dispid(1668435058), helpstring('selected layer for document'), 'propput'], None, 'ActiveLayer',
               ( [], POINTER(IDispatch), 'rhs' )),
    DISPMETHOD([dispid(1145269868), helpstring('selected channels for document'), 'propget'], VARIANT, 'ActiveChannels'),
    DISPMETHOD([dispid(1145269868), helpstring('selected channels for document'), 'propput'], None, 'ActiveChannels',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1147760230), helpstring('document information'), 'propget'], POINTER(DocumentInfo), 'Info'),
    DISPMETHOD([dispid(1148220520), helpstring('full path name of document'), 'propget'], BSTR, 'FullName'),
    DISPMETHOD([dispid(1214736500), helpstring('height of document (unit value)'), 'propget'], c_double, 'Height'),
    DISPMETHOD([dispid(1682794340), helpstring('is the document a workgroup document?'), 'propget'], VARIANT_BOOL, 'Managed'),
    DISPMETHOD([dispid(1146320484), helpstring('has the document been saved since last change?'), 'propget'], VARIANT_BOOL, 'Saved'),
    DISPMETHOD([dispid(1886282093), helpstring("the document's name"), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1146123368), helpstring('the path of the document'), 'propget'], BSTR, 'Path'),
    DISPMETHOD([dispid(1364020580), helpstring('is the document in the quick mask mode?'), 'propget'], VARIANT_BOOL, 'QuickMaskMode'),
    DISPMETHOD([dispid(1364020580), helpstring('is the document in the quick mask mode?'), 'propput'], None, 'QuickMaskMode',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1936026725), helpstring("the document's selection"), 'propget'], POINTER(Selection), 'Selection'),
    DISPMETHOD([dispid(1466201192), helpstring('width of document (unit value)'), 'propget'], c_double, 'Width'),
    DISPMETHOD([dispid(1214870388), helpstring("a histogram of values for the composite document (only for RGB, CMYK and 'Indexed colors' documents)"), 'propget'], VARIANT, 'Histogram'),
    DISPMETHOD([dispid(1147744822), helpstring('the pixel aspect ration of the document'), 'propget'], c_double, 'PixelAspectRatio'),
    DISPMETHOD([dispid(1147744822), helpstring('the pixel aspect ration of the document'), 'propput'], None, 'PixelAspectRatio',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1666731364), helpstring('XMP metadata associated with the document'), 'propget'], POINTER(XMPMetadata), 'XMPMetadata'),
    DISPMETHOD([dispid(1666012003), helpstring('The measurement scale of the document'), 'propget'], POINTER(MeasurementScale), 'MeasurementScale'),
    DISPMETHOD([dispid(1229201440), helpstring('the unique ID of this document'), 'propget'], c_int, 'id'),
    DISPMETHOD([dispid(1665956210), helpstring('the top level layers in this document'), 'propget'], POINTER(Layers), 'Layers'),
    DISPMETHOD([dispid(1665948276), helpstring('the top level layer sets in this document'), 'propget'], POINTER(LayerSets), 'LayerSets'),
    DISPMETHOD([dispid(1665354866), helpstring('the top level art layers in this document'), 'propget'], POINTER(ArtLayers), 'ArtLayers'),
    DISPMETHOD([dispid(1665353838), helpstring('the channels in this document'), 'propget'], POINTER(Channels), 'Channels'),
    DISPMETHOD([dispid(1665692532), helpstring('the history states associated with this document'), 'propget'], POINTER(HistoryStates), 'HistoryStates'),
    DISPMETHOD([dispid(1279471665), helpstring('the layer comps associated with this document'), 'propget'], POINTER(LayerComps), 'LayerComps'),
    DISPMETHOD([dispid(1347694643), helpstring('the art paths associated with this document'), 'propget'], POINTER(PathItems), 'PathItems'),
    DISPMETHOD([dispid(1129590835), helpstring('the current count items'), 'propget'], POINTER(CountItems), 'CountItems'),
    DISPMETHOD([dispid(1129534256), helpstring('the current color samplers associated with this document'), 'propget'], POINTER(ColorSamplers), 'ColorSamplers'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668050803), helpstring('close the document')], None, 'Close',
               ( ['in', 'optional'], VARIANT, 'Saving' )),
    DISPMETHOD([dispid(1131827314), helpstring('convert the document from using one color profile to using an other')], None, 'ConvertProfile',
               ( ['in'], BSTR, 'DestinationProfile' ),
               ( ['in'], PsIntent, 'Intent' ),
               ( ['in', 'optional'], VARIANT, 'BlackPointCompensation' ),
               ( ['in', 'optional'], VARIANT, 'Dither' )),
    DISPMETHOD([dispid(1130906483), helpstring('change the mode of the document')], None, 'ChangeMode',
               ( ['in'], PsChangeMode, 'DestinationMode' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1131573104), helpstring('crop the document')], None, 'Crop',
               ( ['in'], VARIANT, 'Bounds' ),
               ( ['in', 'optional'], VARIANT, 'Angle' ),
               ( ['in', 'optional'], VARIANT, 'Width' ),
               ( ['in', 'optional'], VARIANT, 'Height' )),
    DISPMETHOD([dispid(1165521010)], None, 'Export',
               ( ['in'], BSTR, 'ExportIn' ),
               ( ['in', 'optional'], VARIANT, 'ExportAs' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1181500278), helpstring('flip the canvas horizontally or vertically')], None, 'FlipCanvas',
               ( ['in'], PsDirection, 'Direction' )),
    DISPMETHOD([dispid(1232093550), helpstring('import annotations into the document')], None, 'ImportAnnotations',
               ( ['in'], BSTR, 'File' )),
    DISPMETHOD([dispid(1181512814), helpstring('Flattens all visible layers in the document.')], None, 'Flatten'),
    DISPMETHOD([dispid(1299608418), helpstring('flatten all visible layers in the document')], None, 'MergeVisibleLayers'),
    DISPMETHOD([dispid(1885434740), helpstring('paste contents of clipboard into the document')], POINTER(ArtLayer), 'Paste',
               ( ['in', 'optional'], VARIANT, 'IntoSelection' )),
    DISPMETHOD([dispid(1349731152), helpstring('print the document')], None, 'PrintOut',
               ( ['in', 'optional'], VARIANT, 'SourceSpace' ),
               ( ['in', 'optional'], VARIANT, 'PrintSpace' ),
               ( ['in', 'optional'], VARIANT, 'Intent' ),
               ( ['in', 'optional'], VARIANT, 'BlackPointCompensation' )),
    DISPMETHOD([dispid(1383481708), helpstring('expand document to show clipped sections')], None, 'RevealAll'),
    DISPMETHOD([dispid(1383743852), helpstring('rasterize all layers')], None, 'RasterizeAllLayers'),
    DISPMETHOD([dispid(1296379956), helpstring('record measurements of document')], None, 'RecordMeasurements',
               ( ['in', 'optional'], VARIANT, 'Source' ),
               ( ['in', 'optional'], VARIANT, 'DataPoints' )),
    DISPMETHOD([dispid(1383351158), helpstring('rotate canvas of document')], None, 'RotateCanvas',
               ( ['in'], c_double, 'Angle' )),
    DISPMETHOD([dispid(1383744374), helpstring('change the size of the canvas')], None, 'ResizeCanvas',
               ( ['in', 'optional'], VARIANT, 'Width' ),
               ( ['in', 'optional'], VARIANT, 'Height' ),
               ( ['in', 'optional'], VARIANT, 'Anchor' )),
    DISPMETHOD([dispid(1383745901), helpstring('change the size of the image')], None, 'ResizeImage',
               ( ['in', 'optional'], VARIANT, 'Width' ),
               ( ['in', 'optional'], VARIANT, 'Height' ),
               ( ['in', 'optional'], VARIANT, 'Resolution' ),
               ( ['in', 'optional'], VARIANT, 'ResampleMethod' ),
               ( ['in', 'optional'], VARIANT, 'Amount' )),
    DISPMETHOD([dispid(1399866216), helpstring('split channels of the document')], VARIANT, 'SplitChannels'),
    DISPMETHOD([dispid(1346589558), helpstring('save the document')], None, 'Save'),
    DISPMETHOD([dispid(1400258931), helpstring('save the document with specific save options')], None, 'SaveAs',
               ( ['in'], BSTR, 'SaveIn' ),
               ( ['in', 'optional'], VARIANT, 'Options' ),
               ( ['in', 'optional'], VARIANT, 'AsCopy' ),
               ( ['in', 'optional'], VARIANT, 'ExtensionType' )),
    DISPMETHOD([dispid(1416782192), helpstring('apply trap to a CMYK document')], None, 'Trap',
               ( ['in'], c_int, 'Width' )),
    DISPMETHOD([dispid(1416784237)], None, 'Trim',
               ( ['in', 'optional'], VARIANT, 'Type' ),
               ( ['in', 'optional'], VARIANT, 'Top' ),
               ( ['in', 'optional'], VARIANT, 'Left' ),
               ( ['in', 'optional'], VARIANT, 'Bottom' ),
               ( ['in', 'optional'], VARIANT, 'Right' )),
    DISPMETHOD([dispid(1684235381), helpstring('duplicate this document with parameters')], POINTER(Document), 'Duplicate',
               ( ['in', 'optional'], VARIANT, 'Name' ),
               ( ['in', 'optional'], VARIANT, 'MergeLayersOnly' )),
    DISPMETHOD([dispid(1129590837), helpstring('automatically counts the objects in an image')], None, 'AutoCount',
               ( ['in'], POINTER(Channel), 'Channel' ),
               ( ['in'], c_int, 'Threshold' )),
]
class Preferences(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Preferences for Photoshop'
    _iid_ = GUID('{288BC58E-AB6A-467C-B244-D225349E3EB3}')
    _idlflags_ = ['nonextensible']
    _methods_ = []

# values for enumeration 'PsColorPicker'
psAdobeColorPicker = 1
psAppleColorPicker = 2
psWindowsColorPicker = 3
psPlugInColorPicker = 4
PsColorPicker = c_int # enum

# values for enumeration 'PsResampleMethod'
psNoResampling = 1
psNearestNeighbor = 2
psBilinear = 3
psBicubic = 4
psBicubicSharper = 5
psBicubicSmoother = 6
psBicubicAutomatic = 7
psAutomatic = 8
psPreserveDetails = 9
PsResampleMethod = c_int # enum

# values for enumeration 'PsSaveBehavior'
psNeverSave = 1
psAlwaysSave = 2
psAskWhenSaving = 3
PsSaveBehavior = c_int # enum

# values for enumeration 'PsQueryStateType'
psAlways = 1
psAsk = 2
psNever = 3
PsQueryStateType = c_int # enum

# values for enumeration 'PsPaintingCursors'
psStandard = 1
psPrecise = 2
psBrushSize = 3
PsPaintingCursors = c_int # enum

# values for enumeration 'PsOtherPaintingCursors'
psStandardOther = 1
psPreciseOther = 2
PsOtherPaintingCursors = c_int # enum

# values for enumeration 'PsGridSize'
psNoGrid = 1
psSmallGrid = 2
psMediumGrid = 3
psLargeGrid = 4
PsGridSize = c_int # enum

# values for enumeration 'PsUnits'
psPixels = 1
psInches = 2
psCM = 3
psMM = 4
psPoints = 5
psPicas = 6
psPercent = 7
PsUnits = c_int # enum

# values for enumeration 'PsTypeUnits'
psTypePixels = 1
psTypeMM = 4
psTypePoints = 5
PsTypeUnits = c_int # enum

# values for enumeration 'PsPointType'
psPostScriptPoints = 1
psTraditionalPoints = 2
PsPointType = c_int # enum

# values for enumeration 'PsGuideLineStyle'
psGuideSolidLine = 1
psGuideDashedLine = 2
PsGuideLineStyle = c_int # enum

# values for enumeration 'PsGridLineStyle'
psGridSolidLine = 1
psGridDashedLine = 2
psGridDottedLine = 3
PsGridLineStyle = c_int # enum

# values for enumeration 'PsSaveLogItemsType'
psMetadata = 1
psLogFile = 2
psLogFileAndMetadata = 3
PsSaveLogItemsType = c_int # enum

# values for enumeration 'PsEditLogItemsType'
psSessionOnly = 1
psConcise = 2
psDetailed = 3
PsEditLogItemsType = c_int # enum

# values for enumeration 'PsFontPreviewType'
psFontPreviewNone = 0
psFontPreviewSmall = 1
psFontPreviewMedium = 2
psFontPreviewLarge = 3
psFontPreviewExtraLarge = 4
psFontPreviewHuge = 5
PsFontPreviewType = c_int # enum
Preferences._disp_methods_ = [
    DISPMETHOD([dispid(1129343858), 'propget'], PsColorPicker, 'ColorPicker'),
    DISPMETHOD([dispid(1129343858), 'propput'], None, 'ColorPicker',
               ( [], PsColorPicker, 'rhs' )),
    DISPMETHOD([dispid(1232104545), 'propget'], PsResampleMethod, 'Interpolation'),
    DISPMETHOD([dispid(1232104545), 'propput'], None, 'Interpolation',
               ( [], PsResampleMethod, 'rhs' )),
    DISPMETHOD([dispid(1349660721), 'propget'], VARIANT_BOOL, 'ExportClipboard'),
    DISPMETHOD([dispid(1349660721), 'propput'], None, 'ExportClipboard',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660723), 'propget'], VARIANT_BOOL, 'ShowToolTips'),
    DISPMETHOD([dispid(1349660723), 'propput'], None, 'ShowToolTips',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661747), 'propget'], VARIANT_BOOL, 'KeyboardZoomResizesWindows'),
    DISPMETHOD([dispid(1349661747), 'propput'], None, 'KeyboardZoomResizesWindows',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660724), 'propget'], VARIANT_BOOL, 'AutoUpdateOpenDocuments'),
    DISPMETHOD([dispid(1349660724), 'propput'], None, 'AutoUpdateOpenDocuments',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660725), 'propget'], VARIANT_BOOL, 'ShowAsianTextOptions'),
    DISPMETHOD([dispid(1349660725), 'propput'], None, 'ShowAsianTextOptions',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660726), 'propget'], VARIANT_BOOL, 'BeepWhenDone'),
    DISPMETHOD([dispid(1349660726), 'propput'], None, 'BeepWhenDone',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660727), 'propget'], VARIANT_BOOL, 'DynamicColorSliders'),
    DISPMETHOD([dispid(1349660727), 'propput'], None, 'DynamicColorSliders',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660728), 'propget'], VARIANT_BOOL, 'SavePaletteLocations'),
    DISPMETHOD([dispid(1349660728), 'propput'], None, 'SavePaletteLocations',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660729), 'propget'], VARIANT_BOOL, 'ShowEnglishFontNames'),
    DISPMETHOD([dispid(1349660729), 'propput'], None, 'ShowEnglishFontNames',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660976), 'propget'], VARIANT_BOOL, 'UseShiftKeyForToolSwitch'),
    DISPMETHOD([dispid(1349660976), 'propput'], None, 'UseShiftKeyForToolSwitch',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660977), helpstring('number of history states to remember (between 1 and 100)'), 'propget'], c_int, 'NumberOfHistoryStates'),
    DISPMETHOD([dispid(1349660977), helpstring('number of history states to remember (between 1 and 100)'), 'propput'], None, 'NumberOfHistoryStates',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1349661497), helpstring('automatically make first snapshot when a new document is created?'), 'propget'], VARIANT_BOOL, 'CreateFirstSnapshot'),
    DISPMETHOD([dispid(1349661497), helpstring('automatically make first snapshot when a new document is created?'), 'propput'], None, 'CreateFirstSnapshot',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661744), helpstring('allow non-linear history?'), 'propget'], VARIANT_BOOL, 'NonLinearHistory'),
    DISPMETHOD([dispid(1349661744), helpstring('allow non-linear history?'), 'propput'], None, 'NonLinearHistory',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661745), 'propget'], VARIANT_BOOL, 'SmartQuotes'),
    DISPMETHOD([dispid(1349661745), 'propput'], None, 'SmartQuotes',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660978), 'propget'], PsSaveBehavior, 'ImagePreviews'),
    DISPMETHOD([dispid(1349660978), 'propput'], None, 'ImagePreviews',
               ( [], PsSaveBehavior, 'rhs' )),
    DISPMETHOD([dispid(1884507235), helpstring('should the file extension be lowercase'), 'propget'], VARIANT_BOOL, 'UseLowerCaseExtension'),
    DISPMETHOD([dispid(1884507235), helpstring('should the file extension be lowercase'), 'propput'], None, 'UseLowerCaseExtension',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660980), 'propget'], VARIANT_BOOL, 'AskBeforeSavingLayeredTIFF'),
    DISPMETHOD([dispid(1349660980), 'propput'], None, 'AskBeforeSavingLayeredTIFF',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884125251), helpstring('maximize compatibility for Photoshop (PSD) files'), 'propget'], PsQueryStateType, 'MaximizeCompatibility'),
    DISPMETHOD([dispid(1884125251), helpstring('maximize compatibility for Photoshop (PSD) files'), 'propput'], None, 'MaximizeCompatibility',
               ( [], PsQueryStateType, 'rhs' )),
    DISPMETHOD([dispid(1349660981), helpstring('number of items in the recent file list (between 0 and 30)'), 'propget'], c_int, 'RecentFileListLength'),
    DISPMETHOD([dispid(1349660981), helpstring('number of items in the recent file list (between 0 and 30)'), 'propput'], None, 'RecentFileListLength',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1349660982), 'propget'], VARIANT_BOOL, 'ColorChannelsInColor'),
    DISPMETHOD([dispid(1349660982), 'propput'], None, 'ColorChannelsInColor',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660983), 'propget'], VARIANT_BOOL, 'UseDiffusionDither'),
    DISPMETHOD([dispid(1349660983), 'propput'], None, 'UseDiffusionDither',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660984), 'propget'], VARIANT_BOOL, 'PixelDoubling'),
    DISPMETHOD([dispid(1349660984), 'propput'], None, 'PixelDoubling',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349660985), 'propget'], PsPaintingCursors, 'PaintingCursors'),
    DISPMETHOD([dispid(1349660985), 'propput'], None, 'PaintingCursors',
               ( [], PsPaintingCursors, 'rhs' )),
    DISPMETHOD([dispid(1349661232), 'propget'], PsOtherPaintingCursors, 'OtherCursors'),
    DISPMETHOD([dispid(1349661232), 'propput'], None, 'OtherCursors',
               ( [], PsOtherPaintingCursors, 'rhs' )),
    DISPMETHOD([dispid(1349661233), 'propget'], PsGridSize, 'GridSize'),
    DISPMETHOD([dispid(1349661233), 'propput'], None, 'GridSize',
               ( [], PsGridSize, 'rhs' )),
    DISPMETHOD([dispid(1349661235), helpstring('this option requires hardware support'), 'propget'], VARIANT_BOOL, 'UseVideoAlpha'),
    DISPMETHOD([dispid(1349661235), helpstring('this option requires hardware support'), 'propput'], None, 'UseVideoAlpha',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661236), 'propget'], c_double, 'GamutWarningOpacity'),
    DISPMETHOD([dispid(1349661236), 'propput'], None, 'GamutWarningOpacity',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1349661237), helpstring('Note: this is the unit that the scripting system will use when receiving and returning values'), 'propget'], PsUnits, 'RulerUnits'),
    DISPMETHOD([dispid(1349661237), helpstring('Note: this is the unit that the scripting system will use when receiving and returning values'), 'propput'], None, 'RulerUnits',
               ( [], PsUnits, 'rhs' )),
    DISPMETHOD([dispid(1349661238), 'propget'], PsTypeUnits, 'TypeUnits'),
    DISPMETHOD([dispid(1349661238), 'propput'], None, 'TypeUnits',
               ( [], PsTypeUnits, 'rhs' )),
    DISPMETHOD([dispid(1349661239), helpstring('width of columns (in points)'), 'propget'], c_double, 'ColumnWidth'),
    DISPMETHOD([dispid(1349661239), helpstring('width of columns (in points)'), 'propput'], None, 'ColumnWidth',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1349661240), helpstring('gutter of columns (in points)'), 'propget'], c_double, 'ColumnGutter'),
    DISPMETHOD([dispid(1349661240), helpstring('gutter of columns (in points)'), 'propput'], None, 'ColumnGutter',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1349661241), helpstring('size of point/pica'), 'propget'], PsPointType, 'PointSize'),
    DISPMETHOD([dispid(1349661241), helpstring('size of point/pica'), 'propput'], None, 'PointSize',
               ( [], PsPointType, 'rhs' )),
    DISPMETHOD([dispid(1349661488), 'propget'], PsGuideLineStyle, 'GuideStyle'),
    DISPMETHOD([dispid(1349661488), 'propput'], None, 'GuideStyle',
               ( [], PsGuideLineStyle, 'rhs' )),
    DISPMETHOD([dispid(1349661489), 'propget'], PsGridLineStyle, 'GridStyle'),
    DISPMETHOD([dispid(1349661489), 'propput'], None, 'GridStyle',
               ( [], PsGridLineStyle, 'rhs' )),
    DISPMETHOD([dispid(1349661491), 'propget'], c_int, 'GridSubDivisions'),
    DISPMETHOD([dispid(1349661491), 'propput'], None, 'GridSubDivisions',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1349661492), 'propget'], VARIANT_BOOL, 'ShowSliceNumber'),
    DISPMETHOD([dispid(1349661492), 'propput'], None, 'ShowSliceNumber',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661746), 'propget'], VARIANT_BOOL, 'UseAdditionalPluginFolder'),
    DISPMETHOD([dispid(1349661746), 'propput'], None, 'UseAdditionalPluginFolder',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661493), 'propget'], BSTR, 'AdditionalPluginFolder'),
    DISPMETHOD([dispid(1349661493), 'propput'], None, 'AdditionalPluginFolder',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1349661495), 'propget'], c_int, 'ImageCacheLevels'),
    DISPMETHOD([dispid(1349661495), 'propput'], None, 'ImageCacheLevels',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1349661496), 'propget'], VARIANT_BOOL, 'ImageCacheForHistograms'),
    DISPMETHOD([dispid(1349661496), 'propput'], None, 'ImageCacheForHistograms',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661748), helpstring('Maximum percentage of available RAM used by Photoshop ( 5 - 100 )'), 'propget'], c_int, 'MaxRAMuse'),
    DISPMETHOD([dispid(1349661748), helpstring('Maximum percentage of available RAM used by Photoshop ( 5 - 100 )'), 'propput'], None, 'MaxRAMuse',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1349661749), helpstring('Turn on and off the history logging'), 'propget'], VARIANT_BOOL, 'UseHistoryLog'),
    DISPMETHOD([dispid(1349661749), helpstring('Turn on and off the history logging'), 'propput'], None, 'UseHistoryLog',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349661750), helpstring('options for saving the history items'), 'propget'], PsSaveLogItemsType, 'SaveLogItems'),
    DISPMETHOD([dispid(1349661750), helpstring('options for saving the history items'), 'propput'], None, 'SaveLogItems',
               ( [], PsSaveLogItemsType, 'rhs' )),
    DISPMETHOD([dispid(1349661751), helpstring('options for edit log items'), 'propget'], PsEditLogItemsType, 'EditLogItems'),
    DISPMETHOD([dispid(1349661751), helpstring('options for edit log items'), 'propput'], None, 'EditLogItems',
               ( [], PsEditLogItemsType, 'rhs' )),
    DISPMETHOD([dispid(1349661752), helpstring('file to save the history log'), 'propget'], BSTR, 'SaveLogItemsFile'),
    DISPMETHOD([dispid(1349661752), helpstring('file to save the history log'), 'propput'], None, 'SaveLogItemsFile',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1179660340), helpstring('show font previews in the type tool font menus'), 'propget'], PsFontPreviewType, 'FontPreviewSize'),
    DISPMETHOD([dispid(1179660340), helpstring('show font previews in the type tool font menus'), 'propput'], None, 'FontPreviewSize',
               ( [], PsFontPreviewType, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]

# values for enumeration 'PsDialogModes'
psDisplayAllDialogs = 1
psDisplayErrorDialogs = 2
psDisplayNoDialogs = 3
PsDialogModes = c_int # enum
class Documents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of documents'
    _iid_ = GUID('{662506C7-6AAE-4422-ACA4-C63627CB1868}')
    _idlflags_ = []
    _methods_ = []
Documents._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(Document), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(Document), 'ItemPtr' )),
    DISPMETHOD([dispid(1685021557), helpstring('a document')], POINTER(Document), 'Add',
               ( ['in', 'optional'], VARIANT, 'Width' ),
               ( ['in', 'optional'], VARIANT, 'Height' ),
               ( ['in', 'optional'], VARIANT, 'Resolution' ),
               ( ['in', 'optional'], VARIANT, 'Name' ),
               ( ['in', 'optional'], VARIANT, 'Mode' ),
               ( ['in', 'optional'], VARIANT, 'InitialFill' ),
               ( ['in', 'optional'], VARIANT, 'PixelAspectRatio' ),
               ( ['in', 'optional'], VARIANT, 'BitsPerChannel' ),
               ( ['in', 'optional'], VARIANT, 'ColorProfileName' )),
]
class TextFonts(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of fonts'
    _iid_ = GUID('{BBCE52D6-5D4B-4691-99E3-62C174BD2855}')
    _idlflags_ = []
    _methods_ = []
class TextFont(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'An installed font'
    _iid_ = GUID('{C88838E3-5A82-4EE7-A66C-E0360C9B0356}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
TextFont._disp_methods_ = [
    DISPMETHOD([dispid(1886282093), helpstring("The font's text face name"), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1884312398), helpstring("the font's PostScript name"), 'propget'], BSTR, 'PostScriptName'),
    DISPMETHOD([dispid(1883653710), helpstring("the font's family"), 'propget'], BSTR, 'Family'),
    DISPMETHOD([dispid(1400142188), helpstring("the font's style name"), 'propget'], BSTR, 'Style'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
]
TextFonts._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(TextFont), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(TextFont), 'ItemPtr' )),
]
class Notifiers(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A collection of notifiers'
    _iid_ = GUID('{861C9290-2A0C-4614-8606-706B31BFD45B}')
    _idlflags_ = []
    _methods_ = []
class Notifier(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The parameters of the notifie'
    _iid_ = GUID('{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
Notifier._disp_methods_ = [
    DISPMETHOD([dispid(1162752052), helpstring('The id of the event, four characters or a unique string'), 'propget'], BSTR, 'Event'),
    DISPMETHOD([dispid(1162752053), helpstring('The file to execute when the event occurs'), 'propget'], BSTR, 'EventFile'),
    DISPMETHOD([dispid(1162752055), helpstring('The class id the event applies to, four characters or a unique string. Allows you to distinguish between the same event applied to different classes.'), 'propget'], BSTR, 'EventClass'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1684368495), helpstring('delete the object')], None, 'Delete'),
]
Notifiers._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1668183141), helpstring('number of elements in the collection'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], POINTER(IUnknown), '_NewEnum'),
    DISPMETHOD([dispid(1380009324)], None, 'RemoveAll'),
    DISPMETHOD([dispid(0), helpstring('get an element from the collection'), 'propget'], POINTER(Notifier), 'Item',
               ( ['in'], VARIANT, 'ItemKey' )),
    DISPMETHOD([dispid(1885955192)], c_int, 'Index',
               ( ['in'], POINTER(Notifier), 'ItemPtr' )),
    DISPMETHOD([dispid(1162752050), helpstring('a notifier')], POINTER(Notifier), 'Add',
               ( ['in'], BSTR, 'Event' ),
               ( ['in'], BSTR, 'EventFile' ),
               ( ['in', 'optional'], VARIANT, 'EventClass' )),
]
class MeasurementLog(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'the log of measurements taken'
    _iid_ = GUID('{84ADBF06-8354-4B5C-9CB1-EA2565B66C7C}')
    _idlflags_ = ['nonextensible']
    _methods_ = []
MeasurementLog._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1668574834), helpstring("the object's container"), 'propget'], POINTER(IDispatch), 'Parent'),
    DISPMETHOD([dispid(1296838709), helpstring('export measurements')], None, 'ExportMeasurements',
               ( ['in'], BSTR, 'File' ),
               ( ['in', 'optional'], VARIANT, 'Range' ),
               ( ['in', 'optional'], VARIANT, 'DataPoints' )),
    DISPMETHOD([dispid(1296838710), helpstring('delete measurements')], None, 'DeleteMeasurements',
               ( ['in', 'optional'], VARIANT, 'Range' )),
]

# values for enumeration 'PsPurgeTarget'
psUndoCaches = 1
psHistoryCaches = 2
psClipboardCache = 3
psAllCaches = 4
PsPurgeTarget = c_int # enum
class _ActionDescriptor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{70A60330-E866-46AA-A715-ABF418C41453}')
    _idlflags_ = ['hidden']
    _methods_ = []
class _ActionList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{55031766-E456-4E54-A0D0-8E545601A2D8}')
    _idlflags_ = ['hidden']
    _methods_ = []
class _ActionReference(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsReferenceFormType'
psReferenceNameType = 1
psReferenceIndexType = 2
psReferenceIdentifierType = 3
psReferenceOffsetType = 4
psReferenceEnumeratedType = 5
psReferencePropertyType = 6
psReferenceClassType = 7
PsReferenceFormType = c_int # enum
_ActionReference._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ActionReference), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ActionReference), 'rhs' )),
    DISPMETHOD([dispid(1296118579)], POINTER(_ActionReference), 'GetContainer'),
    DISPMETHOD([dispid(1296118580)], c_int, 'GetDesiredClass'),
    DISPMETHOD([dispid(1296118581), helpstring("Get type of enumeration of an ActionReference whose form is 'Enumerated'")], c_int, 'GetEnumeratedType'),
    DISPMETHOD([dispid(1296118582), helpstring("Get value of enumeration of an ActionReference whose form is 'Enumerated'")], c_int, 'GetEnumeratedValue'),
    DISPMETHOD([dispid(1296118583), helpstring('Get form of ActionReference')], PsReferenceFormType, 'GetForm'),
    DISPMETHOD([dispid(1296118584), helpstring("Get identifier value for an ActionReference whoxse form is 'Identifier'")], c_int, 'GetIdentifier'),
    DISPMETHOD([dispid(1296118585), helpstring("Get index value for an ActionReference whoxse form is 'Index'")], c_int, 'GetIndex'),
    DISPMETHOD([dispid(1296118832), helpstring("Get name value for an ActionReference whoxse form is 'Name'")], BSTR, 'GetName'),
    DISPMETHOD([dispid(1296118833), helpstring("Get offset value for an ActionReference whoxse form is 'Offset'")], c_int, 'GetOffset'),
    DISPMETHOD([dispid(1296118834), helpstring("Get property ID value for an ActionReference whoxse form is 'Property'")], c_int, 'GetProperty'),
    DISPMETHOD([dispid(1296118835)], None, 'PutClass',
               ( ['in'], c_int, 'DesiredClass' )),
    DISPMETHOD([dispid(1296118836)], None, 'PutEnumerated',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], c_int, 'EnumType' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118837)], None, 'PutIdentifier',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118838)], None, 'PutIndex',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118839)], None, 'PutName',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], BSTR, 'Value' )),
    DISPMETHOD([dispid(1296118840)], None, 'PutOffset',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118841)], None, 'PutProperty',
               ( ['in'], c_int, 'DesiredClass' ),
               ( ['in'], c_int, 'Value' )),
]

# values for enumeration 'PsDescValueType'
psIntegerType = 1
psDoubleType = 2
psUnitDoubleType = 3
psStringType = 4
psBooleanType = 5
psListType = 6
psObjectType = 7
psEnumeratedType = 8
psReferenceType = 9
psClassType = 10
psAliasType = 11
psRawType = 12
psLargeIntegerType = 13
PsDescValueType = c_int # enum
_ActionList._disp_methods_ = [
    DISPMETHOD([dispid(1346462580), helpstring('number of items in the list'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ActionList), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ActionList), 'rhs' )),
    DISPMETHOD([dispid(1296117809), helpstring('Clear the list')], None, 'Clear'),
    DISPMETHOD([dispid(1296117811), helpstring('Get the value of an item of type boolean')], VARIANT_BOOL, 'GetBoolean',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296117812), helpstring('Get the value of an item of type class')], c_int, 'GetClass',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296117814), helpstring('Get the value of an item of type double')], c_double, 'GetDouble',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296117815), helpstring('Get the enumeration type of an item')], c_int, 'GetEnumerationType',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296117816), helpstring('Get the enumeration value of an item')], c_int, 'GetEnumerationValue',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296117817), helpstring('Get the value of an item of type integer')], c_int, 'GetInteger',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296119094), helpstring('Get the value of an item of type large integer')], c_int, 'GetLargeInteger',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118065), helpstring('Get the value of an item of type list')], POINTER(_ActionList), 'GetList',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118066), helpstring('Get the class ID of an object in an item of type object')], c_int, 'GetObjectType',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118067), helpstring('Get the value of an item of type object')], POINTER(_ActionDescriptor), 'GetObjectValue',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118068), helpstring('Get the value of an item of type Alias')], BSTR, 'GetPath',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118069), helpstring('Get the value of an item of type ActionReference')], POINTER(_ActionReference), 'GetReference',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118070), helpstring('Get the value of an item of type string')], BSTR, 'GetString',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118071), helpstring('Get the type of an item')], PsDescValueType, 'GetType',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118072), helpstring('Get the unit type of an item of type UnitDouble')], c_int, 'GetUnitDoubleType',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118073), helpstring('Get the value of anm item of type UnitDouble')], c_double, 'GetUnitDoubleValue',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118322)], None, 'PutBoolean',
               ( ['in'], VARIANT_BOOL, 'Value' )),
    DISPMETHOD([dispid(1296118323)], None, 'PutClass',
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118324)], None, 'PutDouble',
               ( ['in'], c_double, 'Value' )),
    DISPMETHOD([dispid(1296118325)], None, 'PutEnumerated',
               ( ['in'], c_int, 'EnumType' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118326)], None, 'PutInteger',
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296119093)], None, 'PutLargeInteger',
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118327)], None, 'PutList',
               ( ['in'], POINTER(_ActionList), 'Value' )),
    DISPMETHOD([dispid(1296118328)], None, 'PutObject',
               ( ['in'], c_int, 'ClassID' ),
               ( ['in'], POINTER(_ActionDescriptor), 'Value' )),
    DISPMETHOD([dispid(1296118329)], None, 'PutPath',
               ( ['in'], BSTR, 'Value' )),
    DISPMETHOD([dispid(1296118576)], None, 'PutReference',
               ( ['in'], POINTER(_ActionReference), 'Value' )),
    DISPMETHOD([dispid(1296118577)], None, 'PutString',
               ( ['in'], BSTR, 'Value' )),
    DISPMETHOD([dispid(1296118578)], None, 'PutUnitDouble',
               ( ['in'], c_int, 'UnitID' ),
               ( ['in'], c_double, 'Value' )),
]
_ActionDescriptor._disp_methods_ = [
    DISPMETHOD([dispid(1346462580), helpstring('number of keys contained in the descriptor'), 'propget'], c_int, 'Count'),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ActionDescriptor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ActionDescriptor), 'rhs' )),
    DISPMETHOD([dispid(1296117809), helpstring('Clear the descriptor')], None, 'Clear'),
    DISPMETHOD([dispid(1296117810), helpstring('Erase a key from the descriptor')], None, 'Erase',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117811), helpstring('Get the value of a key of type boolean')], VARIANT_BOOL, 'GetBoolean',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117812), helpstring('Get the value of a key of type class')], c_int, 'GetClass',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117814), helpstring('Get the value of a key of type double')], c_double, 'GetDouble',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117815), helpstring('Get the enumeration type of a key')], c_int, 'GetEnumerationType',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117816), helpstring('Get the enumeration value of a key')], c_int, 'GetEnumerationValue',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296117817), helpstring('Get the value of a key of type integer')], c_int, 'GetInteger',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296119094), helpstring('Get the value of a key of type large integer')], c_int, 'GetLargeInteger',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118064), helpstring('Get ID of the Nth key')], c_int, 'GetKey',
               ( ['in'], c_int, 'Index' )),
    DISPMETHOD([dispid(1296118065), helpstring('Get the value of a key of type list')], POINTER(_ActionList), 'GetList',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118066), helpstring('Get the class ID of an object in a key of type object')], c_int, 'GetObjectType',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118067), helpstring('Get the value of a key of type object')], POINTER(_ActionDescriptor), 'GetObjectValue',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118068), helpstring('Get the value of a key of type Alias')], BSTR, 'GetPath',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118069), helpstring('Get the value of a key of type ActionReference')], POINTER(_ActionReference), 'GetReference',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118070), helpstring('Get the value of a key of type string')], BSTR, 'GetString',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118071), helpstring('Get the type of a key')], PsDescValueType, 'GetType',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118072), helpstring('Get the unit type of a key of type UnitDouble')], c_int, 'GetUnitDoubleType',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118073), helpstring('Get the value of a key of type UnitDouble')], c_double, 'GetUnitDoubleValue',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118320), helpstring('does the descriptor contain the provided key?')], VARIANT_BOOL, 'HasKey',
               ( ['in'], c_int, 'Key' )),
    DISPMETHOD([dispid(1296118321)], VARIANT_BOOL, 'IsEqual',
               ( ['in'], POINTER(_ActionDescriptor), 'OtherDesc' )),
    DISPMETHOD([dispid(1296118322)], None, 'PutBoolean',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], VARIANT_BOOL, 'Value' )),
    DISPMETHOD([dispid(1296118323)], None, 'PutClass',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118324)], None, 'PutDouble',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_double, 'Value' )),
    DISPMETHOD([dispid(1296118325)], None, 'PutEnumerated',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'EnumType' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118326)], None, 'PutInteger',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296119093)], None, 'PutLargeInteger',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'Value' )),
    DISPMETHOD([dispid(1296118327)], None, 'PutList',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], POINTER(_ActionList), 'Value' )),
    DISPMETHOD([dispid(1296118328)], None, 'PutObject',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'ClassID' ),
               ( ['in'], POINTER(_ActionDescriptor), 'Value' )),
    DISPMETHOD([dispid(1296118329)], None, 'PutPath',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], BSTR, 'Value' )),
    DISPMETHOD([dispid(1296118576)], None, 'PutReference',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], POINTER(_ActionReference), 'Value' )),
    DISPMETHOD([dispid(1296118577)], None, 'PutString',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], BSTR, 'Value' )),
    DISPMETHOD([dispid(1296118578)], None, 'PutUnitDouble',
               ( ['in'], c_int, 'Key' ),
               ( ['in'], c_int, 'UnitID' ),
               ( ['in'], c_double, 'Value' )),
]
_Application._disp_methods_ = [
    DISPMETHOD([dispid(1129988974), helpstring('color settings'), 'propget'], BSTR, 'ColorSettings'),
    DISPMETHOD([dispid(1129988973), helpstring('color settings'), 'hidden', 'propget'], BSTR, 'WinColorSettings'),
    DISPMETHOD([dispid(1883325539), helpstring('the frontmost document'), 'propget'], POINTER(Document), 'ActiveDocument'),
    DISPMETHOD([dispid(1883325539), helpstring('the frontmost document'), 'propput'], None, 'ActiveDocument',
               ( [], POINTER(Document), 'rhs' )),
    DISPMETHOD([dispid(1886282093), helpstring("the application's name"), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1884320872), helpstring('the full path of the location of the Photoshop application'), 'propget'], BSTR, 'Path'),
    DISPMETHOD([dispid(1884320358), helpstring('preference settings'), 'propget'], POINTER(Preferences), 'Preferences'),
    DISPMETHOD([dispid(1884518003), helpstring('the version of the Scripting interface'), 'propget'], BSTR, 'ScriptingVersion'),
    DISPMETHOD([dispid(1883655501), helpstring('the amount of unused memory available to Adobe Photoshop'), 'propget'], c_double, 'FreeMemory'),
    DISPMETHOD([dispid(1986359923), helpstring('the version of Adobe Photoshop application'), 'propget'], BSTR, 'Version'),
    DISPMETHOD([dispid(1884640883), helpstring('is the Photoshop UI visible?'), 'propget'], VARIANT_BOOL, 'Visible'),
    DISPMETHOD([dispid(1884640883), helpstring('is the Photoshop UI visible?'), 'propput'], None, 'Visible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1096116556), helpstring('controls whether or not Photoshop displays dialogs'), 'propget'], PsDialogModes, 'DisplayDialogs'),
    DISPMETHOD([dispid(1096116556), helpstring('controls whether or not Photoshop displays dialogs'), 'propput'], None, 'DisplayDialogs',
               ( [], PsDialogModes, 'rhs' )),
    DISPMETHOD([dispid(1718043491), 'propget'], POINTER(_SolidColor), 'ForegroundColor'),
    DISPMETHOD([dispid(1718043491), 'propput'], None, 'ForegroundColor',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1718043491), 'propputref'], None, 'ForegroundColor',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1650934627), 'propget'], POINTER(_SolidColor), 'BackgroundColor'),
    DISPMETHOD([dispid(1650934627), 'propput'], None, 'BackgroundColor',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1650934627), 'propputref'], None, 'BackgroundColor',
               ( [], POINTER(_SolidColor), 'rhs' )),
    DISPMETHOD([dispid(1162752054), helpstring('enable or disable all notifiers'), 'propget'], VARIANT_BOOL, 'NotifiersEnabled'),
    DISPMETHOD([dispid(1162752054), helpstring('enable or disable all notifiers'), 'propput'], None, 'NotifiersEnabled',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(2003723892), helpstring('list of file image extensions Photoshop can open'), 'propget'], VARIANT, 'WindowsFileTypes'),
    DISPMETHOD([dispid(1836344948), helpstring('list of file image types Photoshop can open'), 'propget'], VARIANT, 'MacintoshFileTypes'),
    DISPMETHOD([dispid(1886545516), helpstring('full path to the preferences folder'), 'propget'], BSTR, 'PreferencesFolder'),
    DISPMETHOD([dispid(1818452332), helpstring('language locale of application'), 'propget'], BSTR, 'Locale'),
    DISPMETHOD([dispid(1685021557), helpstring('the open documents'), 'propget'], POINTER(Documents), 'Documents'),
    DISPMETHOD([dispid(1665560180), helpstring('the fonts installed on this system'), 'propget'], POINTER(TextFonts), 'Fonts'),
    DISPMETHOD([dispid(1162752050), helpstring('the notifiers currently installed'), 'propget'], POINTER(Notifiers), 'Notifiers'),
    DISPMETHOD([dispid(1935830116), helpstring('the build date of the scripting interface'), 'propget'], BSTR, 'ScriptingBuildDate'),
    DISPMETHOD([dispid(1919116908), helpstring('files in the recent file list'), 'propget'], VARIANT, 'RecentFiles'),
    DISPMETHOD([dispid(1114205284), helpstring('the build number of Adobe Photoshop application'), 'propget'], BSTR, 'Build'),
    DISPMETHOD([dispid(1400468297), helpstring('system information of the host application and machine'), 'propget'], BSTR, 'SystemInformation'),
    DISPMETHOD([dispid(1296838707), helpstring('the log of measurements taken'), 'propget'], POINTER(MeasurementLog), 'MeasurementLog'),
    DISPMETHOD([dispid(1666477932), helpstring('name of the current tool'), 'propget'], BSTR, 'CurrentTool'),
    DISPMETHOD([dispid(1666477932), helpstring('name of the current tool'), 'propput'], None, 'CurrentTool',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(1148141923), helpstring('play an action from the Actions Palette')], None, 'DoAction',
               ( ['in'], BSTR, 'Action' ),
               ( ['in'], BSTR, 'From' )),
    DISPMETHOD([dispid(1281643372), helpstring('load a support document')], None, 'Load',
               ( ['in'], BSTR, 'Document' )),
    DISPMETHOD([dispid(1349731151), helpstring('open the specified document')], POINTER(Document), 'Open',
               ( ['in'], BSTR, 'Document' ),
               ( ['in', 'optional'], VARIANT, 'As' ),
               ( ['in', 'optional'], VARIANT, 'AsSmartObject' )),
    DISPMETHOD([dispid(1349874279), helpstring('purges one or more caches')], None, 'Purge',
               ( ['in'], PsPurgeTarget, 'Target' )),
    DISPMETHOD([dispid(1147828311), helpstring('execute JavaScript code')], BSTR, 'DoJavaScript',
               ( ['in'], BSTR, 'JavaScriptCode' ),
               ( ['in', 'optional'], VARIANT, 'Arguments' ),
               ( ['in', 'optional'], VARIANT, 'ExecutionMode' )),
    DISPMETHOD([dispid(1147823703), helpstring('execute javascript file')], BSTR, 'DoJavaScriptFile',
               ( ['in'], BSTR, 'JavaScriptFile' ),
               ( ['in', 'optional'], VARIANT, 'Arguments' ),
               ( ['in', 'optional'], VARIANT, 'ExecutionMode' )),
    DISPMETHOD([dispid(2004316263), helpstring('Creates a web photo gallery')], BSTR, 'MakePhotoGallery',
               ( ['in'], VARIANT, 'InputFolder' ),
               ( ['in'], BSTR, 'OutputFolder' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1346651697), helpstring('create a PDF presentation file')], BSTR, 'MakePDFPresentation',
               ( ['in'], VARIANT, 'InputFiles' ),
               ( ['in'], BSTR, 'OutputFile' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1886678375), helpstring('DEPRECATED. Merges multiple files into one, user interaction required.')], BSTR, 'MakePhotomerge',
               ( ['in'], VARIANT, 'InputFiles' )),
    DISPMETHOD([dispid(1129599816), helpstring('create a contact sheet from multiple files')], BSTR, 'MakeContactSheet',
               ( ['in'], VARIANT, 'InputFiles' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1347702859), helpstring('create a picture package from multiple files')], BSTR, 'MakePicturePackage',
               ( ['in'], VARIANT, 'InputFiles' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1112813617), helpstring('run the batch automation routine')], BSTR, 'Batch',
               ( ['in'], VARIANT, 'InputFiles' ),
               ( ['in'], BSTR, 'Action' ),
               ( ['in'], BSTR, 'From' ),
               ( ['in', 'optional'], VARIANT, 'Options' )),
    DISPMETHOD([dispid(1903520116), helpstring('quit the application')], None, 'Quit'),
    DISPMETHOD([dispid(1382445928), helpstring('pause the script until the application refreshes')], None, 'Refresh'),
    DISPMETHOD([dispid(1718904174), helpstring('is the feature with the given name enabled?')], VARIANT_BOOL, 'FeatureEnabled',
               ( ['in'], BSTR, 'Name' )),
    DISPMETHOD([dispid(1886613360), helpstring('use the Photoshop open dialog to select files')], VARIANT, 'OpenDialog'),
    DISPMETHOD([dispid(1349280121), helpstring('play an ActionManager event')], POINTER(_ActionDescriptor), 'ExecuteAction',
               ( ['in'], c_int, 'EventID' ),
               ( ['in', 'optional'], VARIANT, 'Descriptor' ),
               ( ['in', 'optional'], VARIANT, 'DisplayDialogs' )),
    DISPMETHOD([dispid(1095198068), helpstring('obtain an action descriptor')], POINTER(_ActionDescriptor), 'ExecuteActionGet',
               ( ['in'], POINTER(_ActionReference), 'Reference' )),
    DISPMETHOD([dispid(1098002481), helpstring('convert from a string ID to a runtime ID')], c_int, 'StringIDToTypeID',
               ( ['in'], BSTR, 'StringID' )),
    DISPMETHOD([dispid(1098002482), helpstring('convert from a runtime ID to a string ID')], BSTR, 'TypeIDToStringID',
               ( ['in'], c_int, 'TypeID' )),
    DISPMETHOD([dispid(1098002483), helpstring('convert from a four character code to a runtime ID')], c_int, 'CharIDToTypeID',
               ( ['in'], BSTR, 'CharID' )),
    DISPMETHOD([dispid(1098002484), helpstring('convert from a runtime ID to a character ID')], BSTR, 'TypeIDToCharID',
               ( ['in'], c_int, 'TypeID' )),
    DISPMETHOD([dispid(1130906490), helpstring('set Color Settings to a named set or to the contents of a settings file')], None, 'ChangeColorSettings',
               ( ['in', 'optional'], VARIANT, 'Name' ),
               ( ['in', 'optional'], VARIANT, 'File' )),
]
_PNGSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1383550834), helpstring('should rows be interlaced? ( default: false )'), 'propget'], VARIANT_BOOL, 'Interlaced'),
    DISPMETHOD([dispid(1383550834), helpstring('should rows be interlaced? ( default: false )'), 'propput'], None, 'Interlaced',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1883467120), helpstring('compression used on the image. ( 0 - 9; default: 0 )'), 'propget'], c_int, 'Compression'),
    DISPMETHOD([dispid(1883467120), helpstring('compression used on the image. ( 0 - 9; default: 0 )'), 'propput'], None, 'Compression',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PNGSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PNGSaveOptions), 'rhs' )),
]
class _RawFormatOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a raw format document'
    _iid_ = GUID('{6B785D83-5B5F-4402-A712-BAEBD8C5B812}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsByteOrderType'
psIBMByteOrder = 1
psMacOSByteOrder = 2
PsByteOrderType = c_int # enum
_RawFormatOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1214736500), helpstring('height of image (in pixels)'), 'propget'], c_int, 'Height'),
    DISPMETHOD([dispid(1214736500), helpstring('height of image (in pixels)'), 'propput'], None, 'Height',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1466201192), helpstring('width of image (in pixels)'), 'propget'], c_int, 'Width'),
    DISPMETHOD([dispid(1466201192), helpstring('width of image (in pixels)'), 'propput'], None, 'Width',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1130909293), helpstring('number of channels in image'), 'propget'], c_int, 'ChannelNumber'),
    DISPMETHOD([dispid(1130909293), helpstring('number of channels in image'), 'propput'], None, 'ChannelNumber',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1666147442), helpstring('are the channels in the image interleaved?'), 'propget'], VARIANT_BOOL, 'InterleaveChannels'),
    DISPMETHOD([dispid(1666147442), helpstring('are the channels in the image interleaved?'), 'propput'], None, 'InterleaveChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits for each channel (8 or 16)'), 'propget'], c_int, 'BitsPerChannel'),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits for each channel (8 or 16)'), 'propput'], None, 'BitsPerChannel',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1415987823), helpstring('only relevant for images with 16 bits per channel'), 'propget'], PsByteOrderType, 'ByteOrder'),
    DISPMETHOD([dispid(1415987823), helpstring('only relevant for images with 16 bits per channel'), 'propput'], None, 'ByteOrder',
               ( [], PsByteOrderType, 'rhs' )),
    DISPMETHOD([dispid(1214534522), 'propget'], c_int, 'HeaderSize'),
    DISPMETHOD([dispid(1214534522), 'propput'], None, 'HeaderSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1383352420), helpstring('retain header when saving?'), 'propget'], VARIANT_BOOL, 'RetainHeader'),
    DISPMETHOD([dispid(1383352420), helpstring('retain header when saving?'), 'propput'], None, 'RetainHeader',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_RawFormatOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_RawFormatOpenOptions), 'rhs' )),
]
class _DICOMOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a DICOM document'
    _iid_ = GUID('{EE8364D9-B811-4C7D-A3A8-97C4EBFAB83A}')
    _idlflags_ = ['hidden']
    _methods_ = []
_DICOMOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1097750893), helpstring('Anonymize the patient information'), 'propget'], VARIANT_BOOL, 'Anonymize'),
    DISPMETHOD([dispid(1097750893), helpstring('Anonymize the patient information'), 'propput'], None, 'Anonymize',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1333152889), helpstring('Show Overlays (if present)'), 'propget'], VARIANT_BOOL, 'ShowOverlays'),
    DISPMETHOD([dispid(1333152889), helpstring('Show Overlays (if present)'), 'propput'], None, 'ShowOverlays',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1383028595), helpstring('The number of rows in n-up configuration'), 'propget'], c_int, 'Rows'),
    DISPMETHOD([dispid(1383028595), helpstring('The number of rows in n-up configuration'), 'propput'], None, 'Rows',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1131375693), helpstring('The number of columns in n-up configuration'), 'propget'], c_int, 'Columns'),
    DISPMETHOD([dispid(1131375693), helpstring('The number of columns in n-up configuration'), 'propput'], None, 'Columns',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1465346388), helpstring('Window Width'), 'propget'], c_int, 'WindowWidth'),
    DISPMETHOD([dispid(1465346388), helpstring('Window Width'), 'propput'], None, 'WindowWidth',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1466721622), helpstring('Window Level'), 'propget'], c_int, 'WindowLevel'),
    DISPMETHOD([dispid(1466721622), helpstring('Window Level'), 'propput'], None, 'WindowLevel',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1383494469), helpstring('Reverse(Invert) the image'), 'propget'], VARIANT_BOOL, 'Reverse'),
    DISPMETHOD([dispid(1383494469), helpstring('Reverse(Invert) the image'), 'propput'], None, 'Reverse',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_DICOMOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_DICOMOpenOptions), 'rhs' )),
]

# values for enumeration 'PsExportType'
psIllustratorPaths = 1
psSaveForWeb = 2
PsExportType = c_int # enum
class _GallerySecurityOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery security'
    _iid_ = GUID('{95D69B63-B319-44D3-8307-C988E96E7E58}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsGallerySecurityType'
psNoSecurity = 1
psCustomSecurityText = 2
psFilename = 3
psCopyright = 4
psCaption = 5
psCredit = 6
psTitle = 7
PsGallerySecurityType = c_int # enum

# values for enumeration 'PsGalleryFontType'
psArial = 1
psCourierNew = 2
psHelvetica = 3
psTimesNewRoman = 4
PsGalleryFontType = c_int # enum

# values for enumeration 'PsGallerySecurityTextPositionType'
psCentered = 1
psUpperLeft = 2
psLowerLeft = 3
psUpperRight = 4
psLowerRight = 5
PsGallerySecurityTextPositionType = c_int # enum

# values for enumeration 'PsGallerySecurityTextRotateType'
psZero = 1
psClockwise45 = 2
psClockwise90 = 3
psCounterClockwise45 = 4
psCounterClockwise90 = 5
PsGallerySecurityTextRotateType = c_int # enum
_GallerySecurityOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346844726), helpstring('web photo gallery security content ( default: NoSecurity )'), 'propget'], PsGallerySecurityType, 'Content'),
    DISPMETHOD([dispid(1346844726), helpstring('web photo gallery security content ( default: NoSecurity )'), 'propput'], None, 'Content',
               ( [], PsGallerySecurityType, 'rhs' )),
    DISPMETHOD([dispid(1346844727), helpstring('web photo gallery security custom text ( default:  )'), 'propget'], BSTR, 'Text'),
    DISPMETHOD([dispid(1346844727), helpstring('web photo gallery security custom text ( default:  )'), 'propput'], None, 'Text',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('web photo gallery security font ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('web photo gallery security font ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('web photo gallery security font size ( minimum 1; default: 36 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('web photo gallery security font size ( minimum 1; default: 36 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('web page security text color'), 'propget'], POINTER(_RGBColor), 'TextColor'),
    DISPMETHOD([dispid(1346844722), helpstring('web page security text color'), 'propput'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('web page security text color'), 'propputref'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1332765556), helpstring('web page security opacity as a percent ( default: 100 )'), 'propget'], c_int, 'Opacity'),
    DISPMETHOD([dispid(1332765556), helpstring('web page security opacity as a percent ( default: 100 )'), 'propput'], None, 'Opacity',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844979), helpstring('web photo gallery security text position ( default: Centered )'), 'propget'], PsGallerySecurityTextPositionType, 'TextPosition'),
    DISPMETHOD([dispid(1346844979), helpstring('web photo gallery security text position ( default: Centered )'), 'propput'], None, 'TextPosition',
               ( [], PsGallerySecurityTextPositionType, 'rhs' )),
    DISPMETHOD([dispid(1346844980), helpstring('web photo gallery security text rotate ( default: Zero )'), 'propget'], PsGallerySecurityTextRotateType, 'TextRotate'),
    DISPMETHOD([dispid(1346844980), helpstring('web photo gallery security text rotate ( default: Zero )'), 'propput'], None, 'TextRotate',
               ( [], PsGallerySecurityTextRotateType, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GallerySecurityOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GallerySecurityOptions), 'rhs' )),
]

# values for enumeration 'PsTextureType'
psBlocksTexture = 1
psCanvasTexture = 2
psFrostedTexture = 3
psTinyLensTexture = 4
psTextureFile = 5
PsTextureType = c_int # enum

# values for enumeration 'PsSelectionType'
psReplaceSelection = 1
psExtendSelection = 2
psDiminishSelection = 3
psIntersectSelection = 4
PsSelectionType = c_int # enum

# values for enumeration 'PsMeasurementSource'
psMeasureSelection = 1
psMeasureCountTool = 2
psMeasureRulerTool = 3
PsMeasurementSource = c_int # enum

# values for enumeration 'PsOrientation'
psLandscape = 1
psPortrait = 2
PsOrientation = c_int # enum
class _BMPSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a BMP document'
    _iid_ = GUID('{4D40BE2D-FE11-4060-B52A-DE31C837D51D}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsOperatingSystem'
psOS2 = 1
psWindows = 2
PsOperatingSystem = c_int # enum

# values for enumeration 'PsBMPDepthType'
psBMP1Bit = 1
psBMP4Bits = 4
psBMP8Bits = 8
psBMP16Bits = 16
psBMP24Bits = 24
psBMP32Bits = 32
psBMP_X1R5G5B5 = 60
psBMP_A1R5G5B5 = 61
psBMP_R5G6B5 = 62
psBMP_X4R4G4B4 = 63
psBMP_A4R4G4B4 = 64
psBMP_R8G8B8 = 65
psBMP_X8R8G8B8 = 66
psBMP_A8R8G8B8 = 67
PsBMPDepthType = c_int # enum
_BMPSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884573523), helpstring('target OS. Windows or OS/2 ( default: Windows )'), 'propget'], PsOperatingSystem, 'OSType'),
    DISPMETHOD([dispid(1884573523), helpstring('target OS. Windows or OS/2 ( default: Windows )'), 'propput'], None, 'OSType',
               ( [], PsOperatingSystem, 'rhs' )),
    DISPMETHOD([dispid(1145205613), helpstring('number of bits per sample ( default: BMP24Bits )'), 'propget'], PsBMPDepthType, 'Depth'),
    DISPMETHOD([dispid(1145205613), helpstring('number of bits per sample ( default: BMP24Bits )'), 'propput'], None, 'Depth',
               ( [], PsBMPDepthType, 'rhs' )),
    DISPMETHOD([dispid(1884441669), helpstring('should RLE compression be used?'), 'propget'], VARIANT_BOOL, 'RLECompression'),
    DISPMETHOD([dispid(1884441669), helpstring('should RLE compression be used?'), 'propput'], None, 'RLECompression',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1181766255), 'propget'], VARIANT_BOOL, 'FlipRowOrder'),
    DISPMETHOD([dispid(1181766255), 'propput'], None, 'FlipRowOrder',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_BMPSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_BMPSaveOptions), 'rhs' )),
]
class Application(CoClass):
    'The Adobe Photoshop application'
    _reg_clsid_ = GUID('{51F2E7DD-502F-4EB8-83FF-BD140AB3D50F}')
    _idlflags_ = ['appobject']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
Application._com_interfaces_ = [_Application]


# values for enumeration 'PsTiffEncodingType'
psNoTIFFCompression = 1
psTiffLZW = 2
psTiffJPEG = 3
psTiffZIP = 4
PsTiffEncodingType = c_int # enum

# values for enumeration 'PsLayerCompressionType'
psRLELayerCompression = 1
psZIPLayerCompression = 2
PsLayerCompressionType = c_int # enum
class _RawSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a document in raw format'
    _iid_ = GUID('{D74B820F-AA86-42DD-8D85-F4D67A62F200}')
    _idlflags_ = ['hidden']
    _methods_ = []
_RawSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_RawSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_RawSaveOptions), 'rhs' )),
]

# values for enumeration 'PsMatteType'
psNoMatte = 1
psForegroundColorMatte = 2
psBackgroundColorMatte = 3
psWhiteMatte = 4
psBlackMatte = 5
psSemiGray = 6
psNetscapeGrayMatte = 7
PsMatteType = c_int # enum
class _ContactSheetOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the Contact Sheet command'
    _iid_ = GUID('{064BBE94-396D-4B25-9071-AC5B14D0487F}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsNewDocumentMode'
psNewGray = 1
psNewRGB = 2
psNewCMYK = 3
psNewLab = 4
psNewBitmap = 5
PsNewDocumentMode = c_int # enum
_ContactSheetOptions._disp_methods_ = [
    DISPMETHOD([dispid(1466201192), helpstring('width of the resulting document in pixels ( default: 576 )'), 'propget'], c_int, 'Width'),
    DISPMETHOD([dispid(1466201192), helpstring('width of the resulting document in pixels ( default: 576 )'), 'propput'], None, 'Width',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1214736500), helpstring('height of the resulting document in pixels ( default: 720 )'), 'propget'], c_int, 'Height'),
    DISPMETHOD([dispid(1214736500), helpstring('height of the resulting document in pixels ( default: 720 )'), 'propput'], None, 'Height',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch) ( default: 72.0 )'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch) ( default: 72.0 )'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1330472037), helpstring('document mode (Grayscale, RGB, CMYK or Lab) ( default: NewRGB )'), 'propget'], PsNewDocumentMode, 'Mode'),
    DISPMETHOD([dispid(1330472037), helpstring('document mode (Grayscale, RGB, CMYK or Lab) ( default: NewRGB )'), 'propput'], None, 'Mode',
               ( [], PsNewDocumentMode, 'rhs' )),
    DISPMETHOD([dispid(1129525300), helpstring('flatten all layers in the final document ( default: true )'), 'propget'], VARIANT_BOOL, 'Flatten'),
    DISPMETHOD([dispid(1129525300), helpstring('flatten all layers in the final document ( default: true )'), 'propput'], None, 'Flatten',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1129525298), helpstring('place the images horizontally first ( default: true )'), 'propget'], VARIANT_BOOL, 'AcrossFirst'),
    DISPMETHOD([dispid(1129525298), helpstring('place the images horizontally first ( default: true )'), 'propput'], None, 'AcrossFirst',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1129525299), helpstring('auto space the images in the contact sheet ( default: true )'), 'propget'], VARIANT_BOOL, 'UseAutoSpacing'),
    DISPMETHOD([dispid(1129525299), helpstring('auto space the images in the contact sheet ( default: true )'), 'propput'], None, 'UseAutoSpacing',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844471), helpstring('contact sheet columns ( default: 5 )'), 'propget'], c_int, 'ColumnCount'),
    DISPMETHOD([dispid(1346844471), helpstring('contact sheet columns ( default: 5 )'), 'propput'], None, 'ColumnCount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844472), helpstring('contact sheet rows ( default: 6 )'), 'propget'], c_int, 'RowCount'),
    DISPMETHOD([dispid(1346844472), helpstring('contact sheet rows ( default: 6 )'), 'propput'], None, 'RowCount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1450463098), helpstring('vertical spacing between images in pixels ( default: 1 )'), 'propget'], c_int, 'Vertical'),
    DISPMETHOD([dispid(1450463098), helpstring('vertical spacing between images in pixels ( default: 1 )'), 'propput'], None, 'Vertical',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1215451002), helpstring('horizontal spacing between images in pixels ( default: 1 )'), 'propget'], c_int, 'Horizontal'),
    DISPMETHOD([dispid(1215451002), helpstring('horizontal spacing between images in pixels ( default: 1 )'), 'propput'], None, 'Horizontal',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129525301), helpstring('rotate images for best fit ( default: false )'), 'propget'], VARIANT_BOOL, 'BestFit'),
    DISPMETHOD([dispid(1129525301), helpstring('rotate images for best fit ( default: false )'), 'propput'], None, 'BestFit',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1147744305), helpstring('use the filename as a caption for the image ( default: true )'), 'propget'], VARIANT_BOOL, 'Caption'),
    DISPMETHOD([dispid(1147744305), helpstring('use the filename as a caption for the image ( default: true )'), 'propput'], None, 'Caption',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('font used for the caption ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('font used for the caption ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('font size used for the caption ( default: 12 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('font size used for the caption ( default: 12 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ContactSheetOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ContactSheetOptions), 'rhs' )),
]
class GrayColor(CoClass):
    'A gray color specification'
    _reg_clsid_ = GUID('{0ED8FB42-4D6A-4129-82AA-55DF4736BD02}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
GrayColor._com_interfaces_ = [_GrayColor]

class _CameraRAWOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a camera RAW document'
    _iid_ = GUID('{65D1B010-0D87-481C-B2E6-22EFB5A54129}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsColorSpaceType'
psAdobeRGB = 0
psColorMatchRGB = 1
psProPhotoRGB = 2
psSRGB = 3
PsColorSpaceType = c_int # enum

# values for enumeration 'PsCameraRAWSize'
psMinimumCameraRAW = 0
psSmallCameraRAW = 1
psMediumCameraRAW = 2
psLargeCameraRAW = 3
psExtraLargeCameraRAW = 4
psMaximumCameraRAW = 5
PsCameraRAWSize = c_int # enum

# values for enumeration 'PsCameraRAWSettingsType'
psCameraDefault = 0
psSelectedImage = 1
psCustomSettings = 2
PsCameraRAWSettingsType = c_int # enum

# values for enumeration 'PsWhiteBalanceType'
psAsShot = 0
psAuto = 1
psDaylight = 2
psCloudy = 3
psShade = 4
psTungsten = 5
psFluorescent = 6
psFlash = 7
psCustomCameraSettings = 8
PsWhiteBalanceType = c_int # enum
_CameraRAWOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1131172720), helpstring('colorspace for image'), 'propget'], PsColorSpaceType, 'ColorSpace'),
    DISPMETHOD([dispid(1131172720), helpstring('colorspace for image'), 'propput'], None, 'ColorSpace',
               ( [], PsColorSpaceType, 'rhs' )),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propget'], PsBitsPerChannelType, 'BitsPerChannel'),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propput'], None, 'BitsPerChannel',
               ( [], PsBitsPerChannelType, 'rhs' )),
    DISPMETHOD([dispid(1886679930), helpstring('size of the new document'), 'propget'], PsCameraRAWSize, 'Size'),
    DISPMETHOD([dispid(1886679930), helpstring('size of the new document'), 'propput'], None, 'Size',
               ( [], PsCameraRAWSize, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1884320358), helpstring('global settings for all Camera RAW options ( default: CameraDefault )'), 'propget'], PsCameraRAWSettingsType, 'Settings'),
    DISPMETHOD([dispid(1884320358), helpstring('global settings for all Camera RAW options ( default: CameraDefault )'), 'propput'], None, 'Settings',
               ( [], PsCameraRAWSettingsType, 'rhs' )),
    DISPMETHOD([dispid(1129460020), helpstring('white balance options for the image'), 'propget'], PsWhiteBalanceType, 'WhiteBalance'),
    DISPMETHOD([dispid(1129460020), helpstring('white balance options for the image'), 'propput'], None, 'WhiteBalance',
               ( [], PsWhiteBalanceType, 'rhs' )),
    DISPMETHOD([dispid(1129460021), helpstring('the temperature of the shot'), 'propget'], c_int, 'Temperature'),
    DISPMETHOD([dispid(1129460021), helpstring('the temperature of the shot'), 'propput'], None, 'Temperature',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460022), helpstring('the tint of the shot'), 'propget'], c_int, 'Tint'),
    DISPMETHOD([dispid(1129460022), helpstring('the tint of the shot'), 'propput'], None, 'Tint',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460023), helpstring('the exposure of the shot'), 'propget'], c_double, 'Exposure'),
    DISPMETHOD([dispid(1129460023), helpstring('the exposure of the shot'), 'propput'], None, 'Exposure',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1094004785), helpstring('the shadows of the shot'), 'propget'], c_int, 'Shadows'),
    DISPMETHOD([dispid(1094004785), helpstring('the shadows of the shot'), 'propput'], None, 'Shadows',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1114141806), helpstring('the brightness of the shot'), 'propget'], c_int, 'Brightness'),
    DISPMETHOD([dispid(1114141806), helpstring('the brightness of the shot'), 'propput'], None, 'Brightness',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460025), helpstring('the constrast of the shot'), 'propget'], c_int, 'Contrast'),
    DISPMETHOD([dispid(1129460025), helpstring('the constrast of the shot'), 'propput'], None, 'Contrast',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1884512628), helpstring('the saturation of the shot'), 'propget'], c_int, 'Saturation'),
    DISPMETHOD([dispid(1884512628), helpstring('the saturation of the shot'), 'propput'], None, 'Saturation',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460272), helpstring('the sharpness of the shot'), 'propget'], c_int, 'Sharpness'),
    DISPMETHOD([dispid(1129460272), helpstring('the sharpness of the shot'), 'propput'], None, 'Sharpness',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460273), helpstring('the luminance smoothing of the shot'), 'propget'], c_int, 'LuminanceSmoothing'),
    DISPMETHOD([dispid(1129460273), helpstring('the luminance smoothing of the shot'), 'propput'], None, 'LuminanceSmoothing',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460274), helpstring('the color noise reduction of the shot'), 'propget'], c_int, 'ColorNoiseReduction'),
    DISPMETHOD([dispid(1129460274), helpstring('the color noise reduction of the shot'), 'propput'], None, 'ColorNoiseReduction',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460275), helpstring('the chromatic aberration R/C of the shot'), 'propget'], c_int, 'ChromaticAberrationRC'),
    DISPMETHOD([dispid(1129460275), helpstring('the chromatic aberration R/C of the shot'), 'propput'], None, 'ChromaticAberrationRC',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460276), helpstring('the chromatic aberration B/Y of the shot'), 'propget'], c_int, 'ChromaticAberrationBY'),
    DISPMETHOD([dispid(1129460276), helpstring('the chromatic aberration B/Y of the shot'), 'propput'], None, 'ChromaticAberrationBY',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460277), helpstring('the vignetting amount of the shot'), 'propget'], c_int, 'VignettingAmount'),
    DISPMETHOD([dispid(1129460277), helpstring('the vignetting amount of the shot'), 'propput'], None, 'VignettingAmount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460278), helpstring('the vignetting mid point of the shot'), 'propget'], c_int, 'VignettingMidpoint'),
    DISPMETHOD([dispid(1129460278), helpstring('the vignetting mid point of the shot'), 'propput'], None, 'VignettingMidpoint',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460279), helpstring('the shadow tint of the shot'), 'propget'], c_int, 'ShadowTint'),
    DISPMETHOD([dispid(1129460279), helpstring('the shadow tint of the shot'), 'propput'], None, 'ShadowTint',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460280), helpstring('the red hue of the shot'), 'propget'], c_int, 'RedHue'),
    DISPMETHOD([dispid(1129460280), helpstring('the red hue of the shot'), 'propput'], None, 'RedHue',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460281), helpstring('the red saturation of the shot'), 'propget'], c_int, 'RedSaturation'),
    DISPMETHOD([dispid(1129460281), helpstring('the red saturation of the shot'), 'propput'], None, 'RedSaturation',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460528), helpstring('the green hue of the shot'), 'propget'], c_int, 'GreenHue'),
    DISPMETHOD([dispid(1129460528), helpstring('the green hue of the shot'), 'propput'], None, 'GreenHue',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460529), helpstring('the green saturation of the shot'), 'propget'], c_int, 'GreenSaturation'),
    DISPMETHOD([dispid(1129460529), helpstring('the green saturation of the shot'), 'propput'], None, 'GreenSaturation',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460530), helpstring('the blue hue of the shot'), 'propget'], c_int, 'BlueHue'),
    DISPMETHOD([dispid(1129460530), helpstring('the blue hue of the shot'), 'propput'], None, 'BlueHue',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129460531), helpstring('the blue saturation of the shot'), 'propget'], c_int, 'BlueSaturation'),
    DISPMETHOD([dispid(1129460531), helpstring('the blue saturation of the shot'), 'propput'], None, 'BlueSaturation',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_CameraRAWOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_CameraRAWOpenOptions), 'rhs' )),
]
class _GalleryCustomColorOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery colors'
    _iid_ = GUID('{2EB2592D-F02D-4117-A22C-26E5CDFAEEE2}')
    _idlflags_ = ['hidden']
    _methods_ = []
_GalleryCustomColorOptions._disp_methods_ = [
    DISPMETHOD([dispid(1114063730), helpstring('background color'), 'propget'], POINTER(_RGBColor), 'BackgroundColor'),
    DISPMETHOD([dispid(1114063730), helpstring('background color'), 'propput'], None, 'BackgroundColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1114063730), helpstring('background color'), 'propputref'], None, 'BackgroundColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844721), helpstring('banner color'), 'propget'], POINTER(_RGBColor), 'BannerColor'),
    DISPMETHOD([dispid(1346844721), helpstring('banner color'), 'propput'], None, 'BannerColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844721), helpstring('banner color'), 'propputref'], None, 'BannerColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propget'], POINTER(_RGBColor), 'TextColor'),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propput'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propputref'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844723), helpstring('active link color'), 'propget'], POINTER(_RGBColor), 'ActiveLinkColor'),
    DISPMETHOD([dispid(1346844723), helpstring('active link color'), 'propput'], None, 'ActiveLinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844723), helpstring('active link color'), 'propputref'], None, 'ActiveLinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844724), helpstring('link color'), 'propget'], POINTER(_RGBColor), 'LinkColor'),
    DISPMETHOD([dispid(1346844724), helpstring('link color'), 'propput'], None, 'LinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844724), helpstring('link color'), 'propputref'], None, 'LinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844725), helpstring('visited link color'), 'propget'], POINTER(_RGBColor), 'VisitedLinkColor'),
    DISPMETHOD([dispid(1346844725), helpstring('visited link color'), 'propput'], None, 'VisitedLinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844725), helpstring('visited link color'), 'propputref'], None, 'VisitedLinkColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GalleryCustomColorOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GalleryCustomColorOptions), 'rhs' )),
]

# values for enumeration 'PsCropToType'
psBoundingBox = 0
psMediaBox = 1
psCropBox = 2
psBleedBox = 3
psTrimBox = 4
psArtBox = 5
PsCropToType = c_int # enum

# values for enumeration 'PsPaletteType'
psExact = 1
psMacOSPalette = 2
psWindowsPalette = 3
psWebPalette = 4
psUniform = 5
psLocalPerceptual = 6
psLocalSelective = 7
psLocalAdaptive = 8
psMasterPerceptual = 9
psMasterSelective = 10
psMasterAdaptive = 11
psPreviousPalette = 12
PsPaletteType = c_int # enum

# values for enumeration 'PsGeometry'
psTriangle = 0
psPentagon = 1
psHexagon = 2
psSquareGeometry = 3
psHeptagon = 4
psOctagon = 5
PsGeometry = c_int # enum
class _SGIRGBSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a document in the SGI RGB format'
    _iid_ = GUID('{01CD87DE-1F53-485D-A096-0D318611AB6D}')
    _idlflags_ = ['hidden']
    _methods_ = []
_SGIRGBSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_SGIRGBSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_SGIRGBSaveOptions), 'rhs' )),
]
class RawFormatOpenOptions(CoClass):
    'Settings related to opening a raw format document'
    _reg_clsid_ = GUID('{BEC32A18-401C-4F10-8BC4-055B508016CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
RawFormatOpenOptions._com_interfaces_ = [_RawFormatOpenOptions]


# values for enumeration 'PsColorReductionType'
psPerceptualReduction = 0
psSelective = 1
psAdaptive = 2
psRestrictive = 3
psCustomReduction = 4
psBlackWhiteReduction = 5
psSFWGrayscale = 6
psMacintoshColors = 7
psWindowsColors = 8
PsColorReductionType = c_int # enum
class _ExportOptionsIllustrator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to exporting Illustrator paths'
    _iid_ = GUID('{FC08B435-5F19-49DF-ABE7-ADCE9F0729FF}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsIllustratorPathType'
psDocumentBounds = 1
psAllPaths = 2
psNamedPath = 3
PsIllustratorPathType = c_int # enum
_ExportOptionsIllustrator._disp_methods_ = [
    DISPMETHOD([dispid(1416056948), helpstring('which path to export ( default: DocumentBounds )'), 'propget'], PsIllustratorPathType, 'Path'),
    DISPMETHOD([dispid(1416056948), helpstring('which path to export ( default: DocumentBounds )'), 'propput'], None, 'Path',
               ( [], PsIllustratorPathType, 'rhs' )),
    DISPMETHOD([dispid(1414557293), helpstring('name of path to export. Only valid if you are exporting a named path'), 'propget'], BSTR, 'PathName'),
    DISPMETHOD([dispid(1414557293), helpstring('name of path to export. Only valid if you are exporting a named path'), 'propput'], None, 'PathName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ExportOptionsIllustrator), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ExportOptionsIllustrator), 'rhs' )),
]

# values for enumeration 'PsMeasurementRange'
psAllMeasurements = 1
psActiveMeasurements = 2
PsMeasurementRange = c_int # enum

# values for enumeration 'PsSourceSpaceType'
psDocumentSpace = 1
psProofSpace = 2
PsSourceSpaceType = c_int # enum
class _EPSOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a generic EPS document'
    _iid_ = GUID('{F715C957-54CE-4E55-9856-591D4CD082FD}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsOpenDocumentMode'
psOpenGray = 1
psOpenRGB = 2
psOpenCMYK = 3
psOpenLab = 4
PsOpenDocumentMode = c_int # enum
_EPSOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1214736500), helpstring('height of image (unit value)'), 'propget'], c_double, 'Height'),
    DISPMETHOD([dispid(1214736500), helpstring('height of image (unit value)'), 'propput'], None, 'Height',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1466201192), helpstring('width of image (unit value)'), 'propget'], c_double, 'Width'),
    DISPMETHOD([dispid(1466201192), helpstring('width of image (unit value)'), 'propput'], None, 'Width',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1330472037), helpstring('the document mode'), 'propget'], PsOpenDocumentMode, 'Mode'),
    DISPMETHOD([dispid(1330472037), helpstring('the document mode'), 'propput'], None, 'Mode',
               ( [], PsOpenDocumentMode, 'rhs' )),
    DISPMETHOD([dispid(1097744748), helpstring('use antialias?'), 'propget'], VARIANT_BOOL, 'AntiAlias'),
    DISPMETHOD([dispid(1097744748), helpstring('use antialias?'), 'propput'], None, 'AntiAlias',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1129345616), helpstring('constrain proportions of image'), 'propget'], VARIANT_BOOL, 'ConstrainProportions'),
    DISPMETHOD([dispid(1129345616), helpstring('constrain proportions of image'), 'propput'], None, 'ConstrainProportions',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_EPSOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_EPSOpenOptions), 'rhs' )),
]
class _DCS1_SaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a Photoshop DCS 1.0 document'
    _iid_ = GUID('{94C4A25A-2C91-4514-A783-3173AFC48430}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsPreviewType'
psNoPreview = 1
psMonochromeTIFF = 2
psEightBitTIFF = 3
PsPreviewType = c_int # enum

# values for enumeration 'PsDCSType'
psNoComposite = 1
psGrayscaleComposite = 2
psColorComposite = 3
PsDCSType = c_int # enum

# values for enumeration 'PsSaveEncoding'
psAscii = 3
psBinary = 1
psJPEGLow = 2
psJPEGMedium = 4
psJPEGHigh = 5
psJPEGMaximum = 6
PsSaveEncoding = c_int # enum
_DCS1_SaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propget'], PsPreviewType, 'Preview'),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propput'], None, 'Preview',
               ( [], PsPreviewType, 'rhs' )),
    DISPMETHOD([dispid(1145271139), helpstring('( default: ColorComposite )'), 'propget'], PsDCSType, 'DCS'),
    DISPMETHOD([dispid(1145271139), helpstring('( default: ColorComposite )'), 'propput'], None, 'DCS',
               ( [], PsDCSType, 'rhs' )),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propget'], PsSaveEncoding, 'Encoding'),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propput'], None, 'Encoding',
               ( [], PsSaveEncoding, 'rhs' )),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propget'], VARIANT_BOOL, 'HalftoneScreen'),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propput'], None, 'HalftoneScreen',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propget'], VARIANT_BOOL, 'TransferFunction'),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propput'], None, 'TransferFunction',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propget'], VARIANT_BOOL, 'VectorData'),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propput'], None, 'VectorData',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propget'], VARIANT_BOOL, 'Interpolation'),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propput'], None, 'Interpolation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_DCS1_SaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_DCS1_SaveOptions), 'rhs' )),
]

# values for enumeration 'PsStrokeLocation'
psInsideStroke = 1
psCenterStroke = 2
psOutsideStroke = 3
PsStrokeLocation = c_int # enum
class EPSOpenOptions(CoClass):
    'Settings related to opening a generic EPS document'
    _reg_clsid_ = GUID('{4E59F316-4517-4CA4-A565-F17EA7626A0F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
EPSOpenOptions._com_interfaces_ = [_EPSOpenOptions]

class _TargaSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a Target document'
    _iid_ = GUID('{F4E21694-AEBF-44FB-90AB-EECD58C1B6F3}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsTargaBitsPerPixels'
psTarga16Bits = 16
psTarga24Bits = 24
psTarga32Bits = 32
PsTargaBitsPerPixels = c_int # enum
_TargaSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1382380364), helpstring('number of bits per pixel ( default: Targa24Bits )'), 'propget'], PsTargaBitsPerPixels, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('number of bits per pixel ( default: Targa24Bits )'), 'propput'], None, 'Resolution',
               ( [], PsTargaBitsPerPixels, 'rhs' )),
    DISPMETHOD([dispid(1884441669), helpstring('should RLE compression be used? ( default: true )'), 'propget'], VARIANT_BOOL, 'RLECompression'),
    DISPMETHOD([dispid(1884441669), helpstring('should RLE compression be used? ( default: true )'), 'propput'], None, 'RLECompression',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_TargaSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_TargaSaveOptions), 'rhs' )),
]
class _DCS2_SaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a Photoshop DCS 2.0 document'
    _iid_ = GUID('{F1AF982E-2BBD-406D-9FD6-CA6C898A7FFE}')
    _idlflags_ = ['hidden']
    _methods_ = []
_DCS2_SaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propget'], PsPreviewType, 'Preview'),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propput'], None, 'Preview',
               ( [], PsPreviewType, 'rhs' )),
    DISPMETHOD([dispid(1145271139), helpstring('( default: NoComposite )'), 'propget'], PsDCSType, 'DCS'),
    DISPMETHOD([dispid(1145271139), helpstring('( default: NoComposite )'), 'propput'], None, 'DCS',
               ( [], PsDCSType, 'rhs' )),
    DISPMETHOD([dispid(1145269606), helpstring('( default: false )'), 'propget'], VARIANT_BOOL, 'MultiFileDCS'),
    DISPMETHOD([dispid(1145269606), helpstring('( default: false )'), 'propput'], None, 'MultiFileDCS',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propget'], PsSaveEncoding, 'Encoding'),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propput'], None, 'Encoding',
               ( [], PsSaveEncoding, 'rhs' )),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propget'], VARIANT_BOOL, 'HalftoneScreen'),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propput'], None, 'HalftoneScreen',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propget'], VARIANT_BOOL, 'TransferFunction'),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propput'], None, 'TransferFunction',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propget'], VARIANT_BOOL, 'VectorData'),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propput'], None, 'VectorData',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propget'], VARIANT_BOOL, 'Interpolation'),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propput'], None, 'Interpolation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_DCS2_SaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_DCS2_SaveOptions), 'rhs' )),
]
class _PDFOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a generic PDF document'
    _iid_ = GUID('{50D0174F-484D-4A2B-8BF0-A21B84167D82}')
    _idlflags_ = ['hidden']
    _methods_ = []
_PDFOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch)'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1330472037), helpstring('the document mode'), 'propget'], PsOpenDocumentMode, 'Mode'),
    DISPMETHOD([dispid(1330472037), helpstring('the document mode'), 'propput'], None, 'Mode',
               ( [], PsOpenDocumentMode, 'rhs' )),
    DISPMETHOD([dispid(1097744748), helpstring('use antialias?'), 'propget'], VARIANT_BOOL, 'AntiAlias'),
    DISPMETHOD([dispid(1097744748), helpstring('use antialias?'), 'propput'], None, 'AntiAlias',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884317518), helpstring('number of page or image to open'), 'propget'], c_int, 'Page'),
    DISPMETHOD([dispid(1884317518), helpstring('number of page or image to open'), 'propput'], None, 'Page',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1884312676), helpstring('number of 3d object to open'), 'propget'], c_int, 'Object'),
    DISPMETHOD([dispid(1884312676), helpstring('number of 3d object to open'), 'propput'], None, 'Object',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1129345616), helpstring('DEPRECATED, no longer used in CS2 ( constrain proportions of image )'), 'propget'], VARIANT_BOOL, 'ConstrainProportions'),
    DISPMETHOD([dispid(1129345616), helpstring('DEPRECATED, no longer used in CS2 ( constrain proportions of image )'), 'propput'], None, 'ConstrainProportions',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1214736500), helpstring('DEPRECATED, no longer used in CS2  ( height of image (unit value) )'), 'propget'], c_double, 'Height'),
    DISPMETHOD([dispid(1214736500), helpstring('DEPRECATED, no longer used in CS2  ( height of image (unit value) )'), 'propput'], None, 'Height',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1466201192), helpstring('DEPRECATED, no longer used in CS2  ( width of image (unit value) )'), 'propget'], c_double, 'Width'),
    DISPMETHOD([dispid(1466201192), helpstring('DEPRECATED, no longer used in CS2  ( width of image (unit value) )'), 'propput'], None, 'Width',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propget'], PsBitsPerChannelType, 'BitsPerChannel'),
    DISPMETHOD([dispid(1145201512), helpstring('number of bits per channel'), 'propput'], None, 'BitsPerChannel',
               ( [], PsBitsPerChannelType, 'rhs' )),
    DISPMETHOD([dispid(1884639335), helpstring('page property refers to page number, if false page property refers to image number'), 'propget'], VARIANT_BOOL, 'UsePageNumber'),
    DISPMETHOD([dispid(1884639335), helpstring('page property refers to page number, if false page property refers to image number'), 'propput'], None, 'UsePageNumber',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884640356), helpstring('3d property refers to using 3d object, if false then UsePageNumber is used'), 'propget'], VARIANT_BOOL, 'Use3DObjectNumber'),
    DISPMETHOD([dispid(1884640356), helpstring('3d property refers to using 3d object, if false then UsePageNumber is used'), 'propput'], None, 'Use3DObjectNumber',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1886282093), helpstring('name of the new document'), 'propget'], BSTR, 'Name'),
    DISPMETHOD([dispid(1886282093), helpstring('name of the new document'), 'propput'], None, 'Name',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1668445295), helpstring('crop the page'), 'propget'], PsCropToType, 'CropPage'),
    DISPMETHOD([dispid(1668445295), helpstring('crop the page'), 'propput'], None, 'CropPage',
               ( [], PsCropToType, 'rhs' )),
    DISPMETHOD([dispid(1936750450), helpstring('supress any warnings that may occur during opening'), 'propget'], VARIANT_BOOL, 'SuppressWarnings'),
    DISPMETHOD([dispid(1936750450), helpstring('supress any warnings that may occur during opening'), 'propput'], None, 'SuppressWarnings',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PDFOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PDFOpenOptions), 'rhs' )),
]
class PhotoCDOpenOptions(CoClass):
    'Settings related to opening a PhotoCD document'
    _reg_clsid_ = GUID('{31E250AD-747A-4CBF-80AF-39BFE7E6CDEA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PhotoCDOpenOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to opening a PhotoCD document'
    _iid_ = GUID('{68F15227-7568-47E1-A4F8-5615C24BDD28}')
    _idlflags_ = ['hidden']
    _methods_ = []
PhotoCDOpenOptions._com_interfaces_ = [_PhotoCDOpenOptions]


# values for enumeration 'PsGallerySecurityTextColorType'
psBlackText = 1
psWhiteText = 2
psCustomText = 3
PsGallerySecurityTextColorType = c_int # enum
class _GIFSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a GIF document'
    _iid_ = GUID('{89417281-E1AF-4800-B82A-9F37ED0478EF}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsDitherType'
psNoDither = 1
psDiffusion = 2
psPattern = 3
psNoise = 4
PsDitherType = c_int # enum

# values for enumeration 'PsForcedColors'
psNoForced = 1
psBlackWhite = 2
psPrimaries = 3
psWeb = 4
PsForcedColors = c_int # enum
_GIFSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette (only settable for some palette types)'), 'propget'], c_int, 'Colors'),
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette (only settable for some palette types)'), 'propput'], None, 'Colors',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither'), 'propget'], PsDitherType, 'Dither'),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither'), 'propput'], None, 'Dither',
               ( [], PsDitherType, 'rhs' )),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( 1 - 100; default: 75 )'), 'propget'], c_int, 'DitherAmount'),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( 1 - 100; default: 75 )'), 'propput'], None, 'DitherAmount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346790252), 'propget'], PsForcedColors, 'Forced'),
    DISPMETHOD([dispid(1346790252), 'propput'], None, 'Forced',
               ( [], PsForcedColors, 'rhs' )),
    DISPMETHOD([dispid(1383550834), helpstring('should rows be interlaced? ( default: false )'), 'propget'], VARIANT_BOOL, 'Interlaced'),
    DISPMETHOD([dispid(1383550834), helpstring('should rows be interlaced? ( default: false )'), 'propput'], None, 'Interlaced',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1299477605), 'propget'], PsMatteType, 'Matte'),
    DISPMETHOD([dispid(1299477605), 'propput'], None, 'Matte',
               ( [], PsMatteType, 'rhs' )),
    DISPMETHOD([dispid(1347447924), helpstring('( default: LocalSelective )'), 'propget'], PsPaletteType, 'Palette'),
    DISPMETHOD([dispid(1347447924), helpstring('( default: LocalSelective )'), 'propput'], None, 'Palette',
               ( [], PsPaletteType, 'rhs' )),
    DISPMETHOD([dispid(1146119544), 'propget'], VARIANT_BOOL, 'PreserveExactColors'),
    DISPMETHOD([dispid(1146119544), 'propput'], None, 'PreserveExactColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416786019), 'propget'], VARIANT_BOOL, 'Transparency'),
    DISPMETHOD([dispid(1416786019), 'propput'], None, 'Transparency',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GIFSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GIFSaveOptions), 'rhs' )),
]
class PDFOpenOptions(CoClass):
    'Settings related to opening a generic PDF document'
    _reg_clsid_ = GUID('{44436839-91CE-4C88-942B-9CD1CA633A20}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
PDFOpenOptions._com_interfaces_ = [_PDFOpenOptions]

class _EPSSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving an EPS document'
    _iid_ = GUID('{D54491EF-6F09-4DE3-B49A-D57EDB2F40B8}')
    _idlflags_ = ['hidden']
    _methods_ = []
_EPSSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propget'], PsPreviewType, 'Preview'),
    DISPMETHOD([dispid(1349997635), helpstring('type of preview ( default: MonochromeTIFF )'), 'propput'], None, 'Preview',
               ( [], PsPreviewType, 'rhs' )),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propget'], PsSaveEncoding, 'Encoding'),
    DISPMETHOD([dispid(1164854116), helpstring('type of encoding to use for document ( default: Binary )'), 'propput'], None, 'Encoding',
               ( [], PsSaveEncoding, 'rhs' )),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propget'], VARIANT_BOOL, 'HalftoneScreen'),
    DISPMETHOD([dispid(1214665838), helpstring('include halftone screen ( default: false )'), 'propput'], None, 'HalftoneScreen',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propget'], VARIANT_BOOL, 'TransferFunction'),
    DISPMETHOD([dispid(1416849010), helpstring('include transfer functions in document ( default: false )'), 'propput'], None, 'TransferFunction',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1349731149), helpstring('use Postscript color management ( default: false )'), 'propget'], VARIANT_BOOL, 'PSColorManagement'),
    DISPMETHOD([dispid(1349731149), helpstring('use Postscript color management ( default: false )'), 'propput'], None, 'PSColorManagement',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propget'], VARIANT_BOOL, 'VectorData'),
    DISPMETHOD([dispid(1449346164), helpstring('include vector data'), 'propput'], None, 'VectorData',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propget'], VARIANT_BOOL, 'Interpolation'),
    DISPMETHOD([dispid(1231898960), helpstring('use image interpolation ( default: false )'), 'propput'], None, 'Interpolation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416648552), helpstring('only valid when saving BitMap documents'), 'propget'], VARIANT_BOOL, 'TransparentWhites'),
    DISPMETHOD([dispid(1416648552), helpstring('only valid when saving BitMap documents'), 'propput'], None, 'TransparentWhites',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_EPSSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_EPSSaveOptions), 'rhs' )),
]
class DICOMOpenOptions(CoClass):
    'Settings related to opening a DICOM document'
    _reg_clsid_ = GUID('{BFBA8C38-FFD7-413D-8D39-19C720BEB773}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
DICOMOpenOptions._com_interfaces_ = [_DICOMOpenOptions]

class CameraRAWOpenOptions(CoClass):
    'Settings related to opening a camera RAW document'
    _reg_clsid_ = GUID('{A968B1DE-0535-4E12-82AC-AE59722C8AB3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
CameraRAWOpenOptions._com_interfaces_ = [_CameraRAWOpenOptions]

class PhotoshopSaveOptions(CoClass):
    'Settings related to saving a Photoshop document'
    _reg_clsid_ = GUID('{FF2616D4-A157-42AD-B0AF-F81DAEE9E846}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PhotoshopSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a Photoshop document'
    _iid_ = GUID('{436CE722-7369-4395-ACC2-2DE7A09269DF}')
    _idlflags_ = ['hidden']
    _methods_ = []
PhotoshopSaveOptions._com_interfaces_ = [_PhotoshopSaveOptions]

class _TiffSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a TIFF document'
    _iid_ = GUID('{372B4D75-EB10-4D0A-8203-5778D521253D}')
    _idlflags_ = ['hidden']
    _methods_ = []
_TiffSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propget'], VARIANT_BOOL, 'Layers'),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propput'], None, 'Layers',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propget'], VARIANT_BOOL, 'Annotations'),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propput'], None, 'Annotations',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1231897456), helpstring('compression type ( default: NoTIFFCompression )'), 'propget'], PsTiffEncodingType, 'ImageCompression'),
    DISPMETHOD([dispid(1231897456), helpstring('compression type ( default: NoTIFFCompression )'), 'propput'], None, 'ImageCompression',
               ( [], PsTiffEncodingType, 'rhs' )),
    DISPMETHOD([dispid(1347055719), helpstring('quality of produced image. Only valid for JPEG compressed TIFF documents ( 0 - 12 )'), 'propget'], c_int, 'JPEGQuality'),
    DISPMETHOD([dispid(1347055719), helpstring('quality of produced image. Only valid for JPEG compressed TIFF documents ( 0 - 12 )'), 'propput'], None, 'JPEGQuality',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1415987823), helpstring("Default value is 'Mac OS' when running on MacOS, and 'IBM PC' when running on a PC"), 'propget'], PsByteOrderType, 'ByteOrder'),
    DISPMETHOD([dispid(1415987823), helpstring("Default value is 'Mac OS' when running on MacOS, and 'IBM PC' when running on a PC"), 'propput'], None, 'ByteOrder',
               ( [], PsByteOrderType, 'rhs' )),
    DISPMETHOD([dispid(1884313970), helpstring('( default: false )'), 'propget'], VARIANT_BOOL, 'SaveImagePyramid'),
    DISPMETHOD([dispid(1884313970), helpstring('( default: false )'), 'propput'], None, 'SaveImagePyramid',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416786019), 'propget'], VARIANT_BOOL, 'Transparency'),
    DISPMETHOD([dispid(1416786019), 'propput'], None, 'Transparency',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1283015536), helpstring('should only be used when you are saving layers'), 'propget'], PsLayerCompressionType, 'LayerCompression'),
    DISPMETHOD([dispid(1283015536), helpstring('should only be used when you are saving layers'), 'propput'], None, 'LayerCompression',
               ( [], PsLayerCompressionType, 'rhs' )),
    DISPMETHOD([dispid(1666147442), helpstring('are the channels in the image interleaved? ( default: true )'), 'propget'], VARIANT_BOOL, 'InterleaveChannels'),
    DISPMETHOD([dispid(1666147442), helpstring('are the channels in the image interleaved? ( default: true )'), 'propput'], None, 'InterleaveChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_TiffSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_TiffSaveOptions), 'rhs' )),
]

# values for enumeration 'PsToolType'
psPencil = 1
psBrush = 2
psEraser = 3
psBackgroundEraser = 4
psCloneStamp = 5
psPatternStamp = 6
psHealingBrush = 7
psHistoryBrush = 8
psArtHistoryBrush = 9
psSmudge = 10
psBlur = 11
psSharpen = 12
psDodge = 13
psBurn = 14
psSponge = 15
psColorReplacementTool = 16
PsToolType = c_int # enum
class BMPSaveOptions(CoClass):
    'Settings related to saving a BMP document'
    _reg_clsid_ = GUID('{F54B2306-BF3E-4D11-8706-BCFD79D9A19F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
BMPSaveOptions._com_interfaces_ = [_BMPSaveOptions]

class GIFSaveOptions(CoClass):
    'Settings related to saving a GIF document'
    _reg_clsid_ = GUID('{343AE74B-1B10-4C60-BB4B-1528D299903A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
GIFSaveOptions._com_interfaces_ = [_GIFSaveOptions]

class EPSSaveOptions(CoClass):
    'Settings related to saving an EPS document'
    _reg_clsid_ = GUID('{DDF49D7C-0E10-4FE4-BC5B-83FCD17E7DCF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
EPSSaveOptions._com_interfaces_ = [_EPSSaveOptions]

class JPEGSaveOptions(CoClass):
    'Settings related to saving a JPEG document'
    _reg_clsid_ = GUID('{3201F372-7EAC-49C4-98D9-5EB8577A7392}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _JPEGSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a JPEG document'
    _iid_ = GUID('{5148663B-F632-4AB0-9484-2DBC197CEA82}')
    _idlflags_ = ['hidden']
    _methods_ = []
JPEGSaveOptions._com_interfaces_ = [_JPEGSaveOptions]

class _ExportOptionsSaveForWeb(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to exporting Save For Web files'
    _iid_ = GUID('{91A3D47B-9579-4013-9206-7B6859439DA2}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsSaveDocumentType'
psPhotoshopSave = 1
psBMPSave = 2
psCompuServeGIFSave = 3
psPhotoshopEPSSave = 4
psJPEGSave = 6
psPCXSave = 7
psPhotoshopPDFSave = 8
psPICTFileFormatSave = 10
psPICTResourceFormatSave = 11
psPixarSave = 12
psPNGSave = 13
psRawSave = 14
psScitexCTSave = 15
psTargaSave = 16
psTIFFSave = 17
psPhotoshopDCS_1Save = 18
psPhotoshopDCS_2Save = 19
psAliasPIXSave = 25
psElectricImageSave = 26
psPortableBitmapSave = 27
psWavefrontRLASave = 28
psSGIRGBSave = 29
psSoftImageSave = 30
psWirelessBitmapSave = 31
PsSaveDocumentType = c_int # enum
_ExportOptionsSaveForWeb._disp_methods_ = [
    DISPMETHOD([dispid(1718383728), helpstring('File format to use.  Note: Save For Web only supports Compuserve GIF, JPEG, PNG-8, PNG-24, and BMP formats. ( default: CompuServeGIFSave )'), 'propget'], PsSaveDocumentType, 'Format'),
    DISPMETHOD([dispid(1718383728), helpstring('File format to use.  Note: Save For Web only supports Compuserve GIF, JPEG, PNG-8, PNG-24, and BMP formats. ( default: CompuServeGIFSave )'), 'propput'], None, 'Format',
               ( [], PsSaveDocumentType, 'rhs' )),
    DISPMETHOD([dispid(1395939122), helpstring('if the format is PNG how many bits, true = 8, false = 24 ( default: true )'), 'propget'], VARIANT_BOOL, 'PNG8'),
    DISPMETHOD([dispid(1395939122), helpstring('if the format is PNG how many bits, true = 8, false = 24 ( default: true )'), 'propput'], None, 'PNG8',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1395939123), helpstring('controls amount of lossiness allowed ( default: 0 )'), 'propget'], c_int, 'Lossy'),
    DISPMETHOD([dispid(1395939123), helpstring('controls amount of lossiness allowed ( default: 0 )'), 'propput'], None, 'Lossy',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1395939124), helpstring('color reduction algorithm ( default: Selective )'), 'propget'], PsColorReductionType, 'ColorReduction'),
    DISPMETHOD([dispid(1395939124), helpstring('color reduction algorithm ( default: Selective )'), 'propput'], None, 'ColorReduction',
               ( [], PsColorReductionType, 'rhs' )),
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette ( default: 256 )'), 'propget'], c_int, 'Colors'),
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette ( default: 256 )'), 'propput'], None, 'Colors',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither ( default: Diffusion )'), 'propget'], PsDitherType, 'Dither'),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither ( default: Diffusion )'), 'propput'], None, 'Dither',
               ( [], PsDitherType, 'rhs' )),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( default: 100 )'), 'propget'], c_int, 'DitherAmount'),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( default: 100 )'), 'propput'], None, 'DitherAmount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1416786019), helpstring('( default: true )'), 'propget'], VARIANT_BOOL, 'Transparency'),
    DISPMETHOD([dispid(1416786019), helpstring('( default: true )'), 'propput'], None, 'Transparency',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1395939125), helpstring('transparency dither algorithm ( default: NoDither )'), 'propget'], PsDitherType, 'TransparencyDither'),
    DISPMETHOD([dispid(1395939125), helpstring('transparency dither algorithm ( default: NoDither )'), 'propput'], None, 'TransparencyDither',
               ( [], PsDitherType, 'rhs' )),
    DISPMETHOD([dispid(1395939126), helpstring('amount of transparency dither ( default: 100 )'), 'propget'], c_int, 'TransparencyAmount'),
    DISPMETHOD([dispid(1395939126), helpstring('amount of transparency dither ( default: 100 )'), 'propput'], None, 'TransparencyAmount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1383550834), helpstring('download in multiple passes, progressive ( default: false )'), 'propget'], VARIANT_BOOL, 'Interlaced'),
    DISPMETHOD([dispid(1383550834), helpstring('download in multiple passes, progressive ( default: false )'), 'propput'], None, 'Interlaced',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1299477605), helpstring('defines colors to blend transparent pixels against'), 'propget'], POINTER(_RGBColor), 'MatteColor'),
    DISPMETHOD([dispid(1299477605), helpstring('defines colors to blend transparent pixels against'), 'propput'], None, 'MatteColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1299477605), helpstring('defines colors to blend transparent pixels against'), 'propputref'], None, 'MatteColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1395939127), helpstring('snaps close colors to web palette based on tolerance ( default: 0 )'), 'propget'], c_int, 'WebSnap'),
    DISPMETHOD([dispid(1395939127), helpstring('snaps close colors to web palette based on tolerance ( default: 0 )'), 'propput'], None, 'WebSnap',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1395939128), helpstring('creates smaller but less compatible files ( default: true )'), 'propget'], VARIANT_BOOL, 'Optimized'),
    DISPMETHOD([dispid(1395939128), helpstring('creates smaller but less compatible files ( default: true )'), 'propput'], None, 'Optimized',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1366062201), helpstring('quality of produced image ( default: 60 )'), 'propget'], c_int, 'Quality'),
    DISPMETHOD([dispid(1366062201), helpstring('quality of produced image ( default: 60 )'), 'propput'], None, 'Quality',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1395939129), helpstring('include an ICC profile based on Photoshop color compensation ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeProfile'),
    DISPMETHOD([dispid(1395939129), helpstring('include an ICC profile based on Photoshop color compensation ( default: false )'), 'propput'], None, 'IncludeProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1177563185), helpstring('apply blur to image to reduce artifacts ( default: 0.0 )'), 'propget'], c_double, 'Blur'),
    DISPMETHOD([dispid(1177563185), helpstring('apply blur to image to reduce artifacts ( default: 0.0 )'), 'propput'], None, 'Blur',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_ExportOptionsSaveForWeb), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_ExportOptionsSaveForWeb), 'rhs' )),
]
class PDFSaveOptions(CoClass):
    'Settings related to saving a pdf document'
    _reg_clsid_ = GUID('{B91B10EF-EBC0-41BD-B6F4-3A147D6426D6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PDFSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a pdf document'
    _iid_ = GUID('{F867E6C9-B5DB-4C5A-B3BA-63224D08A01B}')
    _idlflags_ = ['hidden']
    _methods_ = []
PDFSaveOptions._com_interfaces_ = [_PDFSaveOptions]


# values for enumeration 'PsDepthMapSource'
psNoSource = 1
psTransparencyChannel = 2
psLayerMask = 3
psImageHighlight = 4
PsDepthMapSource = c_int # enum
class PICTFileSaveOptions(CoClass):
    'Settings related to saving a PICT document'
    _reg_clsid_ = GUID('{266577AA-ABF9-4DD1-B0D1-330F8E81ADF4}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PICTFileSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a PICT document'
    _iid_ = GUID('{D334A509-00F8-4092-A9AF-6E1176D06536}')
    _idlflags_ = ['hidden']
    _methods_ = []
PICTFileSaveOptions._com_interfaces_ = [_PICTFileSaveOptions]

class PixarSaveOptions(CoClass):
    'Settings related to saving a Pixar document'
    _reg_clsid_ = GUID('{74091CB2-0ADF-4CA9-9AC6-B3E3C954240C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PixarSaveOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to saving a Pixar document'
    _iid_ = GUID('{94C016CD-178F-4FD7-85BB-F5925A34A122}')
    _idlflags_ = ['hidden']
    _methods_ = []
PixarSaveOptions._com_interfaces_ = [_PixarSaveOptions]

class PNGSaveOptions(CoClass):
    'Settings related to saving a PNG document'
    _reg_clsid_ = GUID('{A89175E2-8FDC-45E3-8F49-281E8452F50D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
PNGSaveOptions._com_interfaces_ = [_PNGSaveOptions]

class RawSaveOptions(CoClass):
    'Settings related to saving a document in raw format'
    _reg_clsid_ = GUID('{D222C383-A577-4084-AE95-78F0D653D7E5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
RawSaveOptions._com_interfaces_ = [_RawSaveOptions]

class SGIRGBSaveOptions(CoClass):
    'Settings related to saving a document in the SGI RGB format'
    _reg_clsid_ = GUID('{5769A315-158E-47DB-B11A-65C99792D973}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
SGIRGBSaveOptions._com_interfaces_ = [_SGIRGBSaveOptions]

class TargaSaveOptions(CoClass):
    'Settings related to saving a Target document'
    _reg_clsid_ = GUID('{9A14EA13-17B7-4921-97C9-D07DF318DF5F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
TargaSaveOptions._com_interfaces_ = [_TargaSaveOptions]

class TiffSaveOptions(CoClass):
    'Settings related to saving a TIFF document'
    _reg_clsid_ = GUID('{A5244EF3-A30B-49E3-9866-24FB6E581253}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
TiffSaveOptions._com_interfaces_ = [_TiffSaveOptions]


# values for enumeration 'PsFileNamingType'
psDocumentNameMixed = 1
psDocumentNameLower = 2
psDocumentNameUpper = 3
psSerialNumber1 = 4
psSerialNumber2 = 5
psSerialNumber3 = 6
psSerialNumber4 = 7
psSerialLetterLower = 8
psSerialLetterUpper = 9
psMmddyy = 10
psMmdd = 11
psYyyymmdd = 12
psYymmdd = 13
psYyddmm = 14
psDdmmyy = 15
psDdmm = 16
psExtensionLower = 17
psExtensionUpper = 18
PsFileNamingType = c_int # enum
class DCS2_SaveOptions(CoClass):
    'Settings related to saving a Photoshop DCS 2.0 document'
    _reg_clsid_ = GUID('{F8E1ED4D-7C43-4B20-94C1-54BC9A8ECE7C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
DCS2_SaveOptions._com_interfaces_ = [_DCS2_SaveOptions]

class ExportOptionsSaveForWeb(CoClass):
    'Settings related to exporting Save For Web files'
    _reg_clsid_ = GUID('{F78D58E5-43EF-43B8-B96B-75B947DB951E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ExportOptionsSaveForWeb._com_interfaces_ = [_ExportOptionsSaveForWeb]

class Library(object):
    'Adobe Photoshop CC 2015.5 Object Library'
    name = 'Photoshop'
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)

class DCS1_SaveOptions(CoClass):
    'Settings related to saving a Photoshop DCS 1.0 document'
    _reg_clsid_ = GUID('{52CBBD17-456B-4DD5-9766-8BCCF6226AB1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
DCS1_SaveOptions._com_interfaces_ = [_DCS1_SaveOptions]

class ExportOptionsIllustrator(CoClass):
    'Settings related to exporting Illustrator paths'
    _reg_clsid_ = GUID('{38328845-644E-46F1-BB88-4E379ADB316E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ExportOptionsIllustrator._com_interfaces_ = [_ExportOptionsIllustrator]

class IndexedConversionOptions(CoClass):
    'Settings related to changing the document mode to Indexed'
    _reg_clsid_ = GUID('{AD6B918B-3F6C-47F4-9142-BF05F4798BB3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _IndexedConversionOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to changing the document mode to Indexed'
    _iid_ = GUID('{22D0B851-E811-40E2-9A79-E84EA602C9F1}')
    _idlflags_ = ['hidden']
    _methods_ = []
IndexedConversionOptions._com_interfaces_ = [_IndexedConversionOptions]


# values for enumeration 'PsMagnificationType'
psActualSize = 0
psFitPage = 1
PsMagnificationType = c_int # enum

# values for enumeration 'PsPDFStandardType'
psNoStandard = 0
psPDFX1A2001 = 1
psPDFX1A2003 = 2
psPDFX32002 = 3
psPDFX32003 = 4
psPDFX42008 = 5
PsPDFStandardType = c_int # enum
class SolidColor(CoClass):
    'A color value'
    _reg_clsid_ = GUID('{6B18097A-2B2E-4C89-A433-C53824FDB50B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
SolidColor._com_interfaces_ = [_SolidColor]

class _GalleryImagesOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery images'
    _iid_ = GUID('{46AB9A1D-1B32-4C59-8142-B223ECCF1F74}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsGalleryConstrainType'
psConstrainWidth = 1
psConstrainHeight = 2
psConstrainBoth = 3
PsGalleryConstrainType = c_int # enum
_GalleryImagesOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346843957), helpstring('add numeric links ( default: true )'), 'propget'], VARIANT_BOOL, 'NumericLinks'),
    DISPMETHOD([dispid(1346843957), helpstring('add numeric links ( default: true )'), 'propput'], None, 'NumericLinks',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843958), helpstring('resize images data ( default: true )'), 'propget'], VARIANT_BOOL, 'ResizeImages'),
    DISPMETHOD([dispid(1346843958), helpstring('resize images data ( default: true )'), 'propput'], None, 'ResizeImages',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843959), helpstring('resized image dimensions in pixels ( default: 350 )'), 'propget'], c_int, 'Dimension'),
    DISPMETHOD([dispid(1346843959), helpstring('resized image dimensions in pixels ( default: 350 )'), 'propput'], None, 'Dimension',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346843960), helpstring('how should the image be constrained ( default: ConstrainBoth )'), 'propget'], PsGalleryConstrainType, 'ResizeConstraint'),
    DISPMETHOD([dispid(1346843960), helpstring('how should the image be constrained ( default: ConstrainBoth )'), 'propput'], None, 'ResizeConstraint',
               ( [], PsGalleryConstrainType, 'rhs' )),
    DISPMETHOD([dispid(1346843961), helpstring('the quality setting for the JPEG image ( 0 - 12; default: 5 )'), 'propget'], c_int, 'ImageQuality'),
    DISPMETHOD([dispid(1346843961), helpstring('the quality setting for the JPEG image ( 0 - 12; default: 5 )'), 'propput'], None, 'ImageQuality',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844208), helpstring('the amount of border pixels you want between your images ( 0 - 99; default: 0 )'), 'propget'], c_int, 'Border'),
    DISPMETHOD([dispid(1346844208), helpstring('the amount of border pixels you want between your images ( 0 - 99; default: 0 )'), 'propput'], None, 'Border',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844209), helpstring('include the file name in the text for the gallery images ( default: true )'), 'propget'], VARIANT_BOOL, 'IncludeFilename'),
    DISPMETHOD([dispid(1346844209), helpstring('include the file name in the text for the gallery images ( default: true )'), 'propput'], None, 'IncludeFilename',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1147744305), helpstring('generate a caption for the images ( default: false )'), 'propget'], VARIANT_BOOL, 'Caption'),
    DISPMETHOD([dispid(1147744305), helpstring('generate a caption for the images ( default: false )'), 'propput'], None, 'Caption',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844211), helpstring('include the credits in the text for the gallery images ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeCredits'),
    DISPMETHOD([dispid(1346844211), helpstring('include the credits in the text for the gallery images ( default: false )'), 'propput'], None, 'IncludeCredits',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844212), helpstring('include the title in the text for the gallery images ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeTitle'),
    DISPMETHOD([dispid(1346844212), helpstring('include the title in the text for the gallery images ( default: false )'), 'propput'], None, 'IncludeTitle',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844213), helpstring('include the copyright in the text for the gallery images ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeCopyright'),
    DISPMETHOD([dispid(1346844213), helpstring('include the copyright in the text for the gallery images ( default: false )'), 'propput'], None, 'IncludeCopyright',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('font for the gallery images text ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('font for the gallery images text ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('font size for the gallery images text ( 1 - 7; default: 3 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('font size for the gallery images text ( 1 - 7; default: 3 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GalleryImagesOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GalleryImagesOptions), 'rhs' )),
]

# values for enumeration 'PsOpenDocumentType'
psPhotoshopOpen = 1
psBMPOpen = 2
psCompuServeGIFOpen = 3
psPhotoshopEPSOpen = 4
psFilmstripOpen = 5
psJPEGOpen = 6
psPCXOpen = 7
psPhotoshopPDFOpen = 8
psPhotoCDOpen = 9
psPICTFileFormatOpen = 10
psPICTResourceFormatOpen = 11
psPixarOpen = 12
psPNGOpen = 13
psRawOpen = 14
psScitexCTOpen = 15
psTargaOpen = 16
psTIFFOpen = 17
psPhotoshopDCS_1Open = 18
psPhotoshopDCS_2Open = 19
psPDFOpen = 21
psEPSOpen = 22
psEPSPICTPreviewOpen = 23
psEPSTIFFPreviewOpen = 24
psAliasPIXOpen = 25
psElectricImageOpen = 26
psPortableBitmapOpen = 27
psWavefrontRLAOpen = 28
psSGIRGBOpen = 29
psSoftImageOpen = 30
psWirelessBitmapOpen = 31
psCameraRAWOpen = 32
psDICOMOpen = 33
PsOpenDocumentType = c_int # enum

# values for enumeration 'PsSaveOptions'
psSaveChanges = 1
psDoNotSaveChanges = 2
psPromptToSaveChanges = 3
PsSaveOptions = c_int # enum
class BitmapConversionOptions(CoClass):
    'Settings related to changing the document mode to Bitmap'
    _reg_clsid_ = GUID('{13171A5D-8BEB-40BB-9241-75557F539828}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _BitmapConversionOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Settings related to changing the document mode to Bitmap'
    _iid_ = GUID('{643099A1-0B67-4920-9B14-E14BE8F63D5F}')
    _idlflags_ = ['hidden']
    _methods_ = []
BitmapConversionOptions._com_interfaces_ = [_BitmapConversionOptions]


# values for enumeration 'PsTrimType'
psTransparentPixels = 0
psTopLeftPixel = 1
psBottomRightPixel = 9
PsTrimType = c_int # enum
class CMYKColor(CoClass):
    'A CMYK color specification'
    _reg_clsid_ = GUID('{98206455-77EA-4168-A855-D1431EF0F312}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
CMYKColor._com_interfaces_ = [_CMYKColor]

class RGBColor(CoClass):
    'An RGB color specification'
    _reg_clsid_ = GUID('{FB4AA187-265D-4655-8B7C-96F659861104}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
RGBColor._com_interfaces_ = [_RGBColor]


# values for enumeration 'PsPDFEncodingType'
psPDFNone = 0
psPDFZip = 1
psPDFJPEG = 2
psPDFZip4Bit = 3
psPDFJPEGHIGH = 4
psPDFJPEGMEDHIGH = 5
psPDFJPEGMED = 6
psPDFJPEGMEDLOW = 7
psPDFJPEGLOW = 8
psPDFJPEG2000HIGH = 9
psPDFJPEG2000MEDHIGH = 10
psPDFJPEG2000MED = 11
psPDFJPEG2000MEDLOW = 12
psPDFJPEG2000LOW = 13
psPDFJPEG2000LOSSLESS = 14
PsPDFEncodingType = c_int # enum
class LabColor(CoClass):
    'An Lab color specification'
    _reg_clsid_ = GUID('{49CB02E8-64F9-4095-B849-71912C737943}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
LabColor._com_interfaces_ = [_LabColor]

class HSBColor(CoClass):
    'An HSB color specification'
    _reg_clsid_ = GUID('{DC85DE10-8204-4BFC-AEC4-FE939657F32B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
HSBColor._com_interfaces_ = [_HSBColor]

class NoColor(CoClass):
    'represents a missing color'
    _reg_clsid_ = GUID('{2448DE15-395B-4E3E-8832-DC1E1A915DF1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _NoColor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'represents a missing color'
    _iid_ = GUID('{750824C6-C347-4CDB-AA96-8ABA1EBDF9EA}')
    _idlflags_ = ['hidden']
    _methods_ = []
NoColor._com_interfaces_ = [_NoColor]

class GalleryImagesOptions(CoClass):
    'Options for the web photo gallery images'
    _reg_clsid_ = GUID('{5EEF46D8-D317-47AE-8847-DCF40D00516D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
GalleryImagesOptions._com_interfaces_ = [_GalleryImagesOptions]


# values for enumeration 'PsDocumentFill'
psWhite = 1
psBackgroundColor = 2
psTransparent = 3
PsDocumentFill = c_int # enum
class GalleryOptions(CoClass):
    'Options for the web photo gallery command'
    _reg_clsid_ = GUID('{9922AE42-F2BA-4320-BB4D-05F408EAB2FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _GalleryOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery command'
    _iid_ = GUID('{C2783141-B50D-4F0C-9E2E-BF76EA8A4E60}')
    _idlflags_ = ['hidden']
    _methods_ = []
GalleryOptions._com_interfaces_ = [_GalleryOptions]


# values for enumeration 'PsBatchDestinationType'
psNoDestination = 1
psSaveAndClose = 2
psFolder = 3
PsBatchDestinationType = c_int # enum
class PresentationOptions(CoClass):
    'options for the PDF presentation command'
    _reg_clsid_ = GUID('{21D3BD1E-3033-4458-88EC-EA5D742568B0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PresentationOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'options for the PDF presentation command'
    _iid_ = GUID('{376C4F3B-0345-440B-90D9-FE78AECA249C}')
    _idlflags_ = ['hidden']
    _methods_ = []
PresentationOptions._com_interfaces_ = [_PresentationOptions]

class _PicturePackageOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'options for the Picture Package command'
    _iid_ = GUID('{ABD0F9CE-822B-4BB1-A811-3EC852B43C0F}')
    _idlflags_ = ['hidden']
    _methods_ = []

# values for enumeration 'PsPicturePackageTextType'
psNoText = 1
psUserText = 2
psFilenameText = 3
psCopyrightText = 4
psCaptionText = 5
psCreditText = 6
psOriginText = 7
PsPicturePackageTextType = c_int # enum
_PicturePackageOptions._disp_methods_ = [
    DISPMETHOD([dispid(1347432752), helpstring('layout to use to generate the picture package ( default: (2)5x7 )'), 'propget'], BSTR, 'Layout'),
    DISPMETHOD([dispid(1347432752), helpstring('layout to use to generate the picture package ( default: (2)5x7 )'), 'propput'], None, 'Layout',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch) ( default: 72.0 )'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the document (in pixels per inch) ( default: 72.0 )'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1330472037), helpstring('document mode (Grayscale, RGB, CMYK or Lab) ( default: NewRGB )'), 'propget'], PsNewDocumentMode, 'Mode'),
    DISPMETHOD([dispid(1330472037), helpstring('document mode (Grayscale, RGB, CMYK or Lab) ( default: NewRGB )'), 'propput'], None, 'Mode',
               ( [], PsNewDocumentMode, 'rhs' )),
    DISPMETHOD([dispid(1129525300), helpstring('flatten all layers in the final document ( default: true )'), 'propget'], VARIANT_BOOL, 'Flatten'),
    DISPMETHOD([dispid(1129525300), helpstring('flatten all layers in the final document ( default: true )'), 'propput'], None, 'Flatten',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844726), helpstring('content information ( default: NoText )'), 'propget'], PsPicturePackageTextType, 'Content'),
    DISPMETHOD([dispid(1346844726), helpstring('content information ( default: NoText )'), 'propput'], None, 'Content',
               ( [], PsPicturePackageTextType, 'rhs' )),
    DISPMETHOD([dispid(1346844727), helpstring('picture package custom text ( default:  )'), 'propget'], BSTR, 'Text'),
    DISPMETHOD([dispid(1346844727), helpstring('picture package custom text ( default:  )'), 'propput'], None, 'Text',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('font used for the text ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('font used for the text ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('font size used for the caption ( default: 12 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('font size used for the caption ( default: 12 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1332765556), helpstring('web page security opacity as a percent ( default: 100 )'), 'propget'], c_int, 'Opacity'),
    DISPMETHOD([dispid(1332765556), helpstring('web page security opacity as a percent ( default: 100 )'), 'propput'], None, 'Opacity',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propget'], POINTER(_RGBColor), 'TextColor'),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propput'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844722), helpstring('text color'), 'propputref'], None, 'TextColor',
               ( [], POINTER(_RGBColor), 'rhs' )),
    DISPMETHOD([dispid(1346844979), helpstring('text position ( default: Centered )'), 'propget'], PsGallerySecurityTextPositionType, 'TextPosition'),
    DISPMETHOD([dispid(1346844979), helpstring('text position ( default: Centered )'), 'propput'], None, 'TextPosition',
               ( [], PsGallerySecurityTextPositionType, 'rhs' )),
    DISPMETHOD([dispid(1346844980), helpstring('text rotate ( default: Zero )'), 'propget'], PsGallerySecurityTextRotateType, 'TextRotate'),
    DISPMETHOD([dispid(1346844980), helpstring('text rotate ( default: Zero )'), 'propput'], None, 'TextRotate',
               ( [], PsGallerySecurityTextRotateType, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PicturePackageOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PicturePackageOptions), 'rhs' )),
]
class GalleryCustomColorOptions(CoClass):
    'Options for the web photo gallery colors'
    _reg_clsid_ = GUID('{C26A2449-3A80-4A1D-93C5-7FE4FB229224}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
GalleryCustomColorOptions._com_interfaces_ = [_GalleryCustomColorOptions]

class GalleryThumbnailOptions(CoClass):
    'Options for the web photo gallery thumbnail creation'
    _reg_clsid_ = GUID('{387A1668-383C-4083-899E-8CFC59CAA4C3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _GalleryThumbnailOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery thumbnail creation'
    _iid_ = GUID('{46DFAF34-75E0-470E-8217-B0C763137DD0}')
    _idlflags_ = ['hidden']
    _methods_ = []
GalleryThumbnailOptions._com_interfaces_ = [_GalleryThumbnailOptions]

_NoColor._disp_methods_ = [
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_NoColor), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_NoColor), 'rhs' )),
]

# values for enumeration 'PsBitmapConversionType'
psHalfThreshold = 1
psPatternDither = 2
psDiffusionDither = 3
psHalftoneScreen = 4
psCustomPattern = 5
PsBitmapConversionType = c_int # enum

# values for enumeration 'PsBitmapHalfToneType'
psHalftoneRound = 1
psHalftoneDiamond = 2
psHalftoneEllipse = 3
psHalftoneLine = 4
psHalftoneSquare = 5
psHalftoneCross = 6
PsBitmapHalfToneType = c_int # enum
_BitmapConversionOptions._disp_methods_ = [
    DISPMETHOD([dispid(1382380364), helpstring('output resolution (in pixels per inch) ( default: 72.0 )'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('output resolution (in pixels per inch) ( default: 72.0 )'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1131826548), helpstring('( default: DiffusionDither )'), 'propget'], PsBitmapConversionType, 'Method'),
    DISPMETHOD([dispid(1131826548), helpstring('( default: DiffusionDither )'), 'propput'], None, 'Method',
               ( [], PsBitmapConversionType, 'rhs' )),
    DISPMETHOD([dispid(1348554349), helpstring("only valid for 'custom pattern' conversions"), 'propget'], BSTR, 'PatternName'),
    DISPMETHOD([dispid(1348554349), helpstring("only valid for 'custom pattern' conversions"), 'propput'], None, 'PatternName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1181836153), helpstring("only valid for 'halftone screen' conversions"), 'propget'], c_double, 'Frequency'),
    DISPMETHOD([dispid(1181836153), helpstring("only valid for 'halftone screen' conversions"), 'propput'], None, 'Frequency',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1097754476), helpstring("only valid for 'halftone screen' conversions"), 'propget'], c_double, 'Angle'),
    DISPMETHOD([dispid(1097754476), helpstring("only valid for 'halftone screen' conversions"), 'propput'], None, 'Angle',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1399018344), helpstring("only valid for 'halftone screen' conversions"), 'propget'], PsBitmapHalfToneType, 'Shape'),
    DISPMETHOD([dispid(1399018344), helpstring("only valid for 'halftone screen' conversions"), 'propput'], None, 'Shape',
               ( [], PsBitmapHalfToneType, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_BitmapConversionOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_BitmapConversionOptions), 'rhs' )),
]
class GallerySecurityOptions(CoClass):
    'Options for the web photo gallery security'
    _reg_clsid_ = GUID('{81763510-1793-4D26-BEA9-9182026609A0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
GallerySecurityOptions._com_interfaces_ = [_GallerySecurityOptions]

class GalleryBannerOptions(CoClass):
    'Options for the web photo gallery banner options'
    _reg_clsid_ = GUID('{574B814D-FEA2-451F-9B01-907B8FE4A21F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _GalleryBannerOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Options for the web photo gallery banner options'
    _iid_ = GUID('{5F168D2A-F9EA-4866-8C55-4875E0940622}')
    _idlflags_ = ['hidden']
    _methods_ = []
GalleryBannerOptions._com_interfaces_ = [_GalleryBannerOptions]

class ContactSheetOptions(CoClass):
    'Options for the Contact Sheet command'
    _reg_clsid_ = GUID('{1C526093-0257-4B35-85F8-E2DFEB8CD2CB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ContactSheetOptions._com_interfaces_ = [_ContactSheetOptions]

class PicturePackageOptions(CoClass):
    'options for the Picture Package command'
    _reg_clsid_ = GUID('{1645A5D3-2592-441B-8C17-4232F7BCE043}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
PicturePackageOptions._com_interfaces_ = [_PicturePackageOptions]

_GalleryBannerOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346843705), helpstring('web photo gallery site name ( default: Adobe Web Photo Gallery )'), 'propget'], BSTR, 'SiteName'),
    DISPMETHOD([dispid(1346843705), helpstring('web photo gallery site name ( default: Adobe Web Photo Gallery )'), 'propput'], None, 'SiteName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346843952), helpstring('web photo gallery photographer ( default:  )'), 'propget'], BSTR, 'Photographer'),
    DISPMETHOD([dispid(1346843952), helpstring('web photo gallery photographer ( default:  )'), 'propput'], None, 'Photographer',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346843953), helpstring('web photo gallery contact info ( default:  )'), 'propget'], BSTR, 'ContactInfo'),
    DISPMETHOD([dispid(1346843953), helpstring('web photo gallery contact info ( default:  )'), 'propput'], None, 'ContactInfo',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346843954), helpstring('web photo gallery date ( default:  )'), 'propget'], BSTR, 'Date'),
    DISPMETHOD([dispid(1346843954), helpstring('web photo gallery date ( default:  )'), 'propput'], None, 'Date',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('the font setting for the banner text ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('the font setting for the banner text ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('the size of the font for the banner text ( 1 - 7; default: 3 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('the size of the font for the banner text ( 1 - 7; default: 3 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GalleryBannerOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GalleryBannerOptions), 'rhs' )),
]

# values for enumeration 'PsGalleryThumbSizeType'
psSmall = 1
psMedium = 2
psLarge = 3
psCustomThumbnail = 4
PsGalleryThumbSizeType = c_int # enum
_GalleryThumbnailOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346844209), helpstring('include file name for thumbnail ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeFilename'),
    DISPMETHOD([dispid(1346844209), helpstring('include file name for thumbnail ( default: false )'), 'propput'], None, 'IncludeFilename',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1147744305), helpstring('with caption ( default: false )'), 'propget'], VARIANT_BOOL, 'Caption'),
    DISPMETHOD([dispid(1147744305), helpstring('with caption ( default: false )'), 'propput'], None, 'Caption',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844211), helpstring('include credits for thumbnail ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeCredits'),
    DISPMETHOD([dispid(1346844211), helpstring('include credits for thumbnail ( default: false )'), 'propput'], None, 'IncludeCredits',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844212), helpstring('include title for thumbnail ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeTitle'),
    DISPMETHOD([dispid(1346844212), helpstring('include title for thumbnail ( default: false )'), 'propput'], None, 'IncludeTitle',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346844213), helpstring('include copyright for thumbnail ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeCopyright'),
    DISPMETHOD([dispid(1346844213), helpstring('include copyright for thumbnail ( default: false )'), 'propput'], None, 'IncludeCopyright',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1665560180), helpstring('web photo gallery font ( default: Arial )'), 'propget'], PsGalleryFontType, 'Font'),
    DISPMETHOD([dispid(1665560180), helpstring('web photo gallery font ( default: Arial )'), 'propput'], None, 'Font',
               ( [], PsGalleryFontType, 'rhs' )),
    DISPMETHOD([dispid(1346844468), helpstring('the size of the font for the thumbnail images text ( 1 - 7; default: 3 )'), 'propget'], c_int, 'FontSize'),
    DISPMETHOD([dispid(1346844468), helpstring('the size of the font for the thumbnail images text ( 1 - 7; default: 3 )'), 'propput'], None, 'FontSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1886679930), helpstring('the size of the thumbnail images ( default: Medium )'), 'propget'], PsGalleryThumbSizeType, 'Size'),
    DISPMETHOD([dispid(1886679930), helpstring('the size of the thumbnail images ( default: Medium )'), 'propput'], None, 'Size',
               ( [], PsGalleryThumbSizeType, 'rhs' )),
    DISPMETHOD([dispid(1346843959), helpstring('web photo gallery thumbnail dimension in pixels ( default: 75 )'), 'propget'], c_int, 'Dimension'),
    DISPMETHOD([dispid(1346843959), helpstring('web photo gallery thumbnail dimension in pixels ( default: 75 )'), 'propput'], None, 'Dimension',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844471), helpstring('web photo gallery thumbnail columns ( default: 5 )'), 'propget'], c_int, 'ColumnCount'),
    DISPMETHOD([dispid(1346844471), helpstring('web photo gallery thumbnail columns ( default: 5 )'), 'propput'], None, 'ColumnCount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844472), helpstring('web photo gallery thumbnail rows ( default: 3 )'), 'propget'], c_int, 'RowCount'),
    DISPMETHOD([dispid(1346844472), helpstring('web photo gallery thumbnail rows ( default: 3 )'), 'propput'], None, 'RowCount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346844208), helpstring('the amount of border pixels you want around your thumbnail images ( 0 - 99; default: 0 )'), 'propget'], c_int, 'Border'),
    DISPMETHOD([dispid(1346844208), helpstring('the amount of border pixels you want around your thumbnail images ( 0 - 99; default: 0 )'), 'propput'], None, 'Border',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GalleryThumbnailOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GalleryThumbnailOptions), 'rhs' )),
]
_GalleryOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346843448), helpstring('the style to use for laying out the web page ( default: Centered Frame 1 - Basic )'), 'propget'], BSTR, 'LayoutStyle'),
    DISPMETHOD([dispid(1346843448), helpstring('the style to use for laying out the web page ( default: Centered Frame 1 - Basic )'), 'propput'], None, 'LayoutStyle',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346843449), helpstring('the email address to show on the web page ( default:  )'), 'propget'], BSTR, 'EmailAddress'),
    DISPMETHOD([dispid(1346843449), helpstring('the email address to show on the web page ( default:  )'), 'propput'], None, 'EmailAddress',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346843696), helpstring('short web page extension .htm or long web page extension .html ( default: true )'), 'propget'], VARIANT_BOOL, 'UseShortExtension'),
    DISPMETHOD([dispid(1346843696), helpstring('short web page extension .htm or long web page extension .html ( default: true )'), 'propput'], None, 'UseShortExtension',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843697), helpstring('web page should use UTF-8 encoding ( default: false )'), 'propget'], VARIANT_BOOL, 'UseUTF8Encoding'),
    DISPMETHOD([dispid(1346843697), helpstring('web page should use UTF-8 encoding ( default: false )'), 'propput'], None, 'UseUTF8Encoding',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843698), helpstring('include all files found in sub folders of the input folder ( default: true )'), 'propget'], VARIANT_BOOL, 'IncludeSubFolders'),
    DISPMETHOD([dispid(1346843698), helpstring('include all files found in sub folders of the input folder ( default: true )'), 'propput'], None, 'IncludeSubFolders',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843699), helpstring('add width and height attributes for images ( default: true )'), 'propget'], VARIANT_BOOL, 'AddSizeAttributes'),
    DISPMETHOD([dispid(1346843699), helpstring('add width and height attributes for images ( default: true )'), 'propput'], None, 'AddSizeAttributes',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843955), helpstring('save all of the metadata in the JPEG files ( default: false )'), 'propget'], VARIANT_BOOL, 'PreserveAllMetadata'),
    DISPMETHOD([dispid(1346843955), helpstring('save all of the metadata in the JPEG files ( default: false )'), 'propput'], None, 'PreserveAllMetadata',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346843956), helpstring('options related to banner settings'), 'propget'], POINTER(_GalleryBannerOptions), 'BannerOptions'),
    DISPMETHOD([dispid(1346843956), helpstring('options related to banner settings'), 'propput'], None, 'BannerOptions',
               ( [], POINTER(_GalleryBannerOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843956), helpstring('options related to banner settings'), 'propputref'], None, 'BannerOptions',
               ( [], POINTER(_GalleryBannerOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843701), helpstring('options related to images settings'), 'propget'], POINTER(_GalleryImagesOptions), 'ImagesOptions'),
    DISPMETHOD([dispid(1346843701), helpstring('options related to images settings'), 'propput'], None, 'ImagesOptions',
               ( [], POINTER(_GalleryImagesOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843701), helpstring('options related to images settings'), 'propputref'], None, 'ImagesOptions',
               ( [], POINTER(_GalleryImagesOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843702), helpstring('options related to thumbnail settings'), 'propget'], POINTER(_GalleryThumbnailOptions), 'ThumbnailOptions'),
    DISPMETHOD([dispid(1346843702), helpstring('options related to thumbnail settings'), 'propput'], None, 'ThumbnailOptions',
               ( [], POINTER(_GalleryThumbnailOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843702), helpstring('options related to thumbnail settings'), 'propputref'], None, 'ThumbnailOptions',
               ( [], POINTER(_GalleryThumbnailOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843703), helpstring('options related to custom color settings'), 'propget'], POINTER(_GalleryCustomColorOptions), 'CustomColorOptions'),
    DISPMETHOD([dispid(1346843703), helpstring('options related to custom color settings'), 'propput'], None, 'CustomColorOptions',
               ( [], POINTER(_GalleryCustomColorOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843703), helpstring('options related to custom color settings'), 'propputref'], None, 'CustomColorOptions',
               ( [], POINTER(_GalleryCustomColorOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843704), helpstring('options related to security settings'), 'propget'], POINTER(_GallerySecurityOptions), 'SecurityOptions'),
    DISPMETHOD([dispid(1346843704), helpstring('options related to security settings'), 'propput'], None, 'SecurityOptions',
               ( [], POINTER(_GallerySecurityOptions), 'rhs' )),
    DISPMETHOD([dispid(1346843704), helpstring('options related to security settings'), 'propputref'], None, 'SecurityOptions',
               ( [], POINTER(_GallerySecurityOptions), 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_GalleryOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_GalleryOptions), 'rhs' )),
]
class BatchOptions(CoClass):
    'options for the Batch command'
    _reg_clsid_ = GUID('{7AFC616F-AD29-47FA-9DC0-0D1579811A58}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _BatchOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'options for the Batch command'
    _iid_ = GUID('{B0D18870-EAC3-4D35-8612-6F734B3FA656}')
    _idlflags_ = ['hidden']
    _methods_ = []
BatchOptions._com_interfaces_ = [_BatchOptions]

class SubPathInfo(CoClass):
    'Sub path information (returned by entire path dataClassProperty of path item class)'
    _reg_clsid_ = GUID('{0B6F1761-32F5-47B5-8F12-03AFD920EB89}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _SubPathInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Sub path information (returned by entire path dataClassProperty of path item class)'
    _iid_ = GUID('{7E8F9046-9F8E-4594-A22C-9F6B4C227CD7}')
    _idlflags_ = ['hidden']
    _methods_ = []
SubPathInfo._com_interfaces_ = [_SubPathInfo]

class PathPointInfo(CoClass):
    'Path point information (returned by entire path dataClassProperty of path item class)'
    _reg_clsid_ = GUID('{A089C1CD-459C-44B0-9B34-444121B53521}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
class _PathPointInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Path point information (returned by entire path dataClassProperty of path item class)'
    _iid_ = GUID('{B3C35001-B625-48D7-9D3B-C9D66D9CF5F1}')
    _idlflags_ = ['hidden']
    _methods_ = []
PathPointInfo._com_interfaces_ = [_PathPointInfo]

class ActionDescriptor(CoClass):
    _reg_clsid_ = GUID('{977B366B-3BF8-4545-B5E5-C90464663E12}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ActionDescriptor._com_interfaces_ = [_ActionDescriptor]

class ActionList(CoClass):
    _reg_clsid_ = GUID('{9479F1E2-2C00-4AE3-A065-2E0661E4DAB8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ActionList._com_interfaces_ = [_ActionList]


# values for enumeration 'PsFormatOptionsType'
psStandardBaseline = 1
psOptimizedBaseline = 2
psProgressive = 3
PsFormatOptionsType = c_int # enum
_JPEGSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1246777200), helpstring('( default: StandardBaseline )'), 'propget'], PsFormatOptionsType, 'FormatOptions'),
    DISPMETHOD([dispid(1246777200), helpstring('( default: StandardBaseline )'), 'propput'], None, 'FormatOptions',
               ( [], PsFormatOptionsType, 'rhs' )),
    DISPMETHOD([dispid(1299477605), 'propget'], PsMatteType, 'Matte'),
    DISPMETHOD([dispid(1299477605), 'propput'], None, 'Matte',
               ( [], PsMatteType, 'rhs' )),
    DISPMETHOD([dispid(1399025267), helpstring('number of scans. Only valid for progressive type JPEG files ( 3 - 5 )'), 'propget'], c_int, 'Scans'),
    DISPMETHOD([dispid(1399025267), helpstring('number of scans. Only valid for progressive type JPEG files ( 3 - 5 )'), 'propput'], None, 'Scans',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1366062201), helpstring('quality of produced image ( 0 - 12; default: 3 )'), 'propget'], c_int, 'Quality'),
    DISPMETHOD([dispid(1366062201), helpstring('quality of produced image ( 0 - 12; default: 3 )'), 'propput'], None, 'Quality',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_JPEGSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_JPEGSaveOptions), 'rhs' )),
]
class ActionReference(CoClass):
    _reg_clsid_ = GUID('{7365C2DB-D6A0-4D84-A48E-604EE9C2DC85}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}', 1, 0)
ActionReference._com_interfaces_ = [_ActionReference]


# values for enumeration 'PsPICTBitsPerPixels'
psPICT2Bits = 2
psPICT4Bits = 4
psPICT8Bits = 8
psPICT16Bits = 16
psPICT32Bits = 32
PsPICTBitsPerPixels = c_int # enum

# values for enumeration 'PsPICTCompression'
psNoPICTCompression = 1
psJPEGLowPICT = 2
psJPEGMediumPICT = 4
psJPEGHighPICT = 5
psJPEGMaximumPICT = 6
PsPICTCompression = c_int # enum
_PICTFileSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('number of bits per pixel'), 'propget'], PsPICTBitsPerPixels, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('number of bits per pixel'), 'propput'], None, 'Resolution',
               ( [], PsPICTBitsPerPixels, 'rhs' )),
    DISPMETHOD([dispid(1883467120), helpstring('( default: NoPICTCompression )'), 'propget'], PsPICTCompression, 'Compression'),
    DISPMETHOD([dispid(1883467120), helpstring('( default: NoPICTCompression )'), 'propput'], None, 'Compression',
               ( [], PsPICTCompression, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PICTFileSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PICTFileSaveOptions), 'rhs' )),
]

# values for enumeration 'PsTransitionType'
psBlindsHorizontal = 1
psBlindsVertical = 2
psDissolveTransition = 3
psBoxIn = 4
psBoxOut = 5
psGlitterDown = 6
psGlitterRight = 7
psGlitterRightDown = 8
psNoTrasition = 9
psRandom = 10
psSplitHorizontalIn = 11
psSplitHorizontalOut = 12
psSplitVerticalIn = 13
psSplitVerticalOut = 14
psWipeDown = 15
psWipeLeft = 16
psWipeRight = 17
psWipeUp = 18
PsTransitionType = c_int # enum

# values for enumeration 'PsPDFCompatibilityType'
psPDF13 = 1
psPDF14 = 2
psPDF15 = 3
psPDF16 = 4
psPDF17 = 5
PsPDFCompatibilityType = c_int # enum

# values for enumeration 'PsPDFResampleType'
psNoResample = 0
psPDFAverage = 1
psPDFSubSample = 2
psPDFBicubic = 3
PsPDFResampleType = c_int # enum
_PDFSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propget'], VARIANT_BOOL, 'Layers'),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propput'], None, 'Layers',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propget'], VARIANT_BOOL, 'Annotations'),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propput'], None, 'Annotations',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1883531088), helpstring('DEPRECATED, no longer used in CS2 ( should the embedded color profile be downgraded to version 2 )'), 'propget'], VARIANT_BOOL, 'DowngradeColorProfile'),
    DISPMETHOD([dispid(1883531088), helpstring('DEPRECATED, no longer used in CS2 ( should the embedded color profile be downgraded to version 2 )'), 'propput'], None, 'DowngradeColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1416786019), helpstring('DEPRECATED, no longer used in CS2'), 'propget'], VARIANT_BOOL, 'Transparency'),
    DISPMETHOD([dispid(1416786019), helpstring('DEPRECATED, no longer used in CS2'), 'propput'], None, 'Transparency',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1231898960), helpstring('DEPRECATED, no longer used in CS2 ( use image interpolation? )'), 'propget'], VARIANT_BOOL, 'Interpolation'),
    DISPMETHOD([dispid(1231898960), helpstring('DEPRECATED, no longer used in CS2 ( use image interpolation? )'), 'propput'], None, 'Interpolation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1449346164), helpstring('DEPRECATED, no longer used in CS2 ( include vector data )'), 'propget'], VARIANT_BOOL, 'VectorData'),
    DISPMETHOD([dispid(1449346164), helpstring('DEPRECATED, no longer used in CS2 ( include vector data )'), 'propput'], None, 'VectorData',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1164789364), helpstring('DEPRECATED, no longer used in CS2 ( embed fonts? Only valid if a text layer is included )'), 'propget'], VARIANT_BOOL, 'EmbedFonts'),
    DISPMETHOD([dispid(1164789364), helpstring('DEPRECATED, no longer used in CS2 ( embed fonts? Only valid if a text layer is included )'), 'propput'], None, 'EmbedFonts',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1417170796), helpstring('DEPRECATED, no longer used in CS2 ( use outlines for text? Only valid if vector data is included )'), 'propget'], VARIANT_BOOL, 'UseOutlines'),
    DISPMETHOD([dispid(1417170796), helpstring('DEPRECATED, no longer used in CS2 ( use outlines for text? Only valid if vector data is included )'), 'propput'], None, 'UseOutlines',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1164854116), helpstring('ZIP, JPEG and JPEG2000 encoding and compression options'), 'propget'], PsPDFEncodingType, 'Encoding'),
    DISPMETHOD([dispid(1164854116), helpstring('ZIP, JPEG and JPEG2000 encoding and compression options'), 'propput'], None, 'Encoding',
               ( [], PsPDFEncodingType, 'rhs' )),
    DISPMETHOD([dispid(1347055719), helpstring('Only valid for JPEG encoding. Use encoding options instead of this property. Quality of produced image. Only valid for JPEG encoded PDF documents ( 0 - 12 )'), 'propget'], c_int, 'JPEGQuality'),
    DISPMETHOD([dispid(1347055719), helpstring('Only valid for JPEG encoding. Use encoding options instead of this property. Quality of produced image. Only valid for JPEG encoded PDF documents ( 0 - 12 )'), 'propput'], None, 'JPEGQuality',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1885759852), helpstring("preset file to use for settings, may override 'save as' dialog settings"), 'propget'], BSTR, 'PresetFile'),
    DISPMETHOD([dispid(1885759852), helpstring("preset file to use for settings, may override 'save as' dialog settings"), 'propput'], None, 'PresetFile',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346646070), helpstring('PDF Standard to be compatible with'), 'propget'], PsPDFStandardType, 'PDFStandard'),
    DISPMETHOD([dispid(1346646070), helpstring('PDF Standard to be compatible with'), 'propput'], None, 'PDFStandard',
               ( [], PsPDFStandardType, 'rhs' )),
    DISPMETHOD([dispid(1346646071), helpstring('PDF version to be compatible with'), 'propget'], PsPDFCompatibilityType, 'PDFCompatibility'),
    DISPMETHOD([dispid(1346646071), helpstring('PDF version to be compatible with'), 'propput'], None, 'PDFCompatibility',
               ( [], PsPDFCompatibilityType, 'rhs' )),
    DISPMETHOD([dispid(1346646583), helpstring('description of the save options in use'), 'propget'], BSTR, 'Description'),
    DISPMETHOD([dispid(1346646583), helpstring('description of the save options in use'), 'propput'], None, 'Description',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346646323), helpstring('Lets you reopen the PDF in Photoshop with native Photoshop data intact'), 'propget'], VARIANT_BOOL, 'PreserveEditing'),
    DISPMETHOD([dispid(1346646323), helpstring('Lets you reopen the PDF in Photoshop with native Photoshop data intact'), 'propput'], None, 'PreserveEditing',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646324), helpstring('Includes a small preview image in Acrobat'), 'propget'], VARIANT_BOOL, 'EmbedThumbnail'),
    DISPMETHOD([dispid(1346646324), helpstring('Includes a small preview image in Acrobat'), 'propput'], None, 'EmbedThumbnail',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646582), helpstring('Improves performance of PDFs on Web servers'), 'propget'], VARIANT_BOOL, 'OptimizeForWeb'),
    DISPMETHOD([dispid(1346646582), helpstring('Improves performance of PDFs on Web servers'), 'propput'], None, 'OptimizeForWeb',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346651702), helpstring('Opens the saved PDF in Acrobat'), 'propget'], VARIANT_BOOL, 'View'),
    DISPMETHOD([dispid(1346651702), helpstring('Opens the saved PDF in Acrobat'), 'propput'], None, 'View',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646325), helpstring('down sample method to use'), 'propget'], PsPDFResampleType, 'DownSample'),
    DISPMETHOD([dispid(1346646325), helpstring('down sample method to use'), 'propput'], None, 'DownSample',
               ( [], PsPDFResampleType, 'rhs' )),
    DISPMETHOD([dispid(1346646584), helpstring('down sample images to this size if they exceed limit (in pixels per inch)'), 'propget'], c_double, 'DownSampleSize'),
    DISPMETHOD([dispid(1346646584), helpstring('down sample images to this size if they exceed limit (in pixels per inch)'), 'propput'], None, 'DownSampleSize',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1346646585), helpstring('limits downsampleing/subsampling to images that exceed this value (in pixels per inch)'), 'propget'], c_double, 'DownSampleSizeLimit'),
    DISPMETHOD([dispid(1346646585), helpstring('limits downsampleing/subsampling to images that exceed this value (in pixels per inch)'), 'propput'], None, 'DownSampleSizeLimit',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1346646576), helpstring('compression option supported only with JPEG2000 compression'), 'propget'], c_int, 'TileSize'),
    DISPMETHOD([dispid(1346646576), helpstring('compression option supported only with JPEG2000 compression'), 'propput'], None, 'TileSize',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346646577), helpstring('converts a 16-bit image to 8-bit for better compatibility with other applications'), 'propget'], VARIANT_BOOL, 'ConvertToEightBit'),
    DISPMETHOD([dispid(1346646577), helpstring('converts a 16-bit image to 8-bit for better compatibility with other applications'), 'propput'], None, 'ConvertToEightBit',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646832), helpstring('convert the color profile to a destination profile'), 'propget'], VARIANT_BOOL, 'ColorConversion'),
    DISPMETHOD([dispid(1346646832), helpstring('convert the color profile to a destination profile'), 'propput'], None, 'ColorConversion',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646578), helpstring('describes the final RGB or CMYK output device, such as your monitor or a certain press standard'), 'propget'], BSTR, 'DestinationProfile'),
    DISPMETHOD([dispid(1346646578), helpstring('describes the final RGB or CMYK output device, such as your monitor or a certain press standard'), 'propput'], None, 'DestinationProfile',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346646833), helpstring('shows which profiles to include'), 'propget'], VARIANT_BOOL, 'ProfileInclusionPolicy'),
    DISPMETHOD([dispid(1346646833), helpstring('shows which profiles to include'), 'propput'], None, 'ProfileInclusionPolicy',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346646579), helpstring('an optional comment field for inserting descriptions of the output condition. The text is stored in the PDF/X file.'), 'propget'], BSTR, 'OutputCondition'),
    DISPMETHOD([dispid(1346646579), helpstring('an optional comment field for inserting descriptions of the output condition. The text is stored in the PDF/X file.'), 'propput'], None, 'OutputCondition',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346646580), helpstring('identifier for the output condition'), 'propget'], BSTR, 'OutputConditionID'),
    DISPMETHOD([dispid(1346646580), helpstring('identifier for the output condition'), 'propput'], None, 'OutputConditionID',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1346646581), helpstring('URL where the output condition is registered'), 'propget'], BSTR, 'RegistryName'),
    DISPMETHOD([dispid(1346646581), helpstring('URL where the output condition is registered'), 'propput'], None, 'RegistryName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PDFSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PDFSaveOptions), 'rhs' )),
]
_PresentationOptions._disp_methods_ = [
    DISPMETHOD([dispid(1346651701), helpstring('true if the file type is presentation false for Multi-Page document ( default: false )'), 'propget'], VARIANT_BOOL, 'Presentation'),
    DISPMETHOD([dispid(1346651701), helpstring('true if the file type is presentation false for Multi-Page document ( default: false )'), 'propput'], None, 'Presentation',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346651703), helpstring('auto advance when viewing ( default: true )'), 'propget'], VARIANT_BOOL, 'AutoAdvance'),
    DISPMETHOD([dispid(1346651703), helpstring('auto advance when viewing ( default: true )'), 'propput'], None, 'AutoAdvance',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346651704), helpstring('time in seconds before auto advancing the view ( default: 5 )'), 'propget'], c_int, 'Interval'),
    DISPMETHOD([dispid(1346651704), helpstring('time in seconds before auto advancing the view ( default: 5 )'), 'propput'], None, 'Interval',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346651705), helpstring('loop after last page ( default: false )'), 'propget'], VARIANT_BOOL, 'Loop'),
    DISPMETHOD([dispid(1346651705), helpstring('loop after last page ( default: false )'), 'propput'], None, 'Loop',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346651745), helpstring('transition type when switching to the next document ( default: NoTrasition )'), 'propget'], PsTransitionType, 'Transition'),
    DISPMETHOD([dispid(1346651745), helpstring('transition type when switching to the next document ( default: NoTrasition )'), 'propput'], None, 'Transition',
               ( [], PsTransitionType, 'rhs' )),
    DISPMETHOD([dispid(1346651765), helpstring('magnification type when viewing the image ( default: ActualSize )'), 'propget'], PsMagnificationType, 'Magnification'),
    DISPMETHOD([dispid(1346651765), helpstring('magnification type when viewing the image ( default: ActualSize )'), 'propput'], None, 'Magnification',
               ( [], PsMagnificationType, 'rhs' )),
    DISPMETHOD([dispid(1346844209), helpstring('include file name for image ( default: false )'), 'propget'], VARIANT_BOOL, 'IncludeFilename'),
    DISPMETHOD([dispid(1346844209), helpstring('include file name for image ( default: false )'), 'propput'], None, 'IncludeFilename',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1346651764), helpstring('Options used when creating the PDF file'), 'propget'], POINTER(_PDFSaveOptions), 'PDFFileOptions'),
    DISPMETHOD([dispid(1346651764), helpstring('Options used when creating the PDF file'), 'propput'], None, 'PDFFileOptions',
               ( [], POINTER(_PDFSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(1346651764), helpstring('Options used when creating the PDF file'), 'propputref'], None, 'PDFFileOptions',
               ( [], POINTER(_PDFSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PresentationOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PresentationOptions), 'rhs' )),
]
_BatchOptions._disp_methods_ = [
    DISPMETHOD([dispid(1112813619), helpstring('override action open commands ( default: false )'), 'propget'], VARIANT_BOOL, 'OverrideOpen'),
    DISPMETHOD([dispid(1112813619), helpstring('override action open commands ( default: false )'), 'propput'], None, 'OverrideOpen',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813620), helpstring('suppress file open options dialogs ( default: false )'), 'propget'], VARIANT_BOOL, 'SuppressOpen'),
    DISPMETHOD([dispid(1112813620), helpstring('suppress file open options dialogs ( default: false )'), 'propput'], None, 'SuppressOpen',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813621), helpstring('suppress color profile warnings ( default: false )'), 'propget'], VARIANT_BOOL, 'SuppressProfile'),
    DISPMETHOD([dispid(1112813621), helpstring('suppress color profile warnings ( default: false )'), 'propput'], None, 'SuppressProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813622), helpstring('final destination of processed files ( default: NoDestination )'), 'propget'], PsBatchDestinationType, 'Destination'),
    DISPMETHOD([dispid(1112813622), helpstring('final destination of processed files ( default: NoDestination )'), 'propput'], None, 'Destination',
               ( [], PsBatchDestinationType, 'rhs' )),
    DISPMETHOD([dispid(1112814391), helpstring('folder location when using destination to a folder'), 'propget'], BSTR, 'DestinationFolder'),
    DISPMETHOD([dispid(1112814391), helpstring('folder location when using destination to a folder'), 'propput'], None, 'DestinationFolder',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1112813623), helpstring('override save as action steps with destination specified here ( default: false )'), 'propget'], VARIANT_BOOL, 'OverrideSave'),
    DISPMETHOD([dispid(1112813623), helpstring('override save as action steps with destination specified here ( default: false )'), 'propput'], None, 'OverrideSave',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813624), helpstring('list of file naming options 6 max.'), 'propget'], VARIANT, 'FileNaming'),
    DISPMETHOD([dispid(1112813624), helpstring('list of file naming options 6 max.'), 'propput'], None, 'FileNaming',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1112813625), helpstring('starting serial number to use ( default: 1 )'), 'propget'], c_int, 'StartingSerial'),
    DISPMETHOD([dispid(1112813625), helpstring('starting serial number to use ( default: 1 )'), 'propput'], None, 'StartingSerial',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1112813872), helpstring('make final file name Windows compatible ( default: true )'), 'propget'], VARIANT_BOOL, 'WindowsCompatible'),
    DISPMETHOD([dispid(1112813872), helpstring('make final file name Windows compatible ( default: true )'), 'propput'], None, 'WindowsCompatible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813873), helpstring('make final file name Macintosh compatible ( default: true )'), 'propget'], VARIANT_BOOL, 'MacintoshCompatible'),
    DISPMETHOD([dispid(1112813873), helpstring('make final file name Macintosh compatible ( default: true )'), 'propput'], None, 'MacintoshCompatible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813874), helpstring('make final file name Unix compatible ( default: true )'), 'propget'], VARIANT_BOOL, 'UnixCompatible'),
    DISPMETHOD([dispid(1112813874), helpstring('make final file name Unix compatible ( default: true )'), 'propput'], None, 'UnixCompatible',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1112813875), helpstring('file to log errors encountered, leave this blank to stop for errors'), 'propget'], BSTR, 'ErrorFile'),
    DISPMETHOD([dispid(1112813875), helpstring('file to log errors encountered, leave this blank to stop for errors'), 'propput'], None, 'ErrorFile',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_BatchOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_BatchOptions), 'rhs' )),
]
_SubPathInfo._disp_methods_ = [
    DISPMETHOD([dispid(1347694647), helpstring('sub path operation on other sub paths'), 'propget'], PsShapeOperation, 'Operation'),
    DISPMETHOD([dispid(1347694647), helpstring('sub path operation on other sub paths'), 'propput'], None, 'Operation',
               ( [], PsShapeOperation, 'rhs' )),
    DISPMETHOD([dispid(1347695920), helpstring('is this path closed?'), 'propget'], VARIANT_BOOL, 'Closed'),
    DISPMETHOD([dispid(1347695920), helpstring('is this path closed?'), 'propput'], None, 'Closed',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1347695926), helpstring("all the sub path item's path points"), 'propget'], VARIANT, 'EntireSubPath'),
    DISPMETHOD([dispid(1347695926), helpstring("all the sub path item's path points"), 'propput'], None, 'EntireSubPath',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_SubPathInfo), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_SubPathInfo), 'rhs' )),
]
_PixarSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PixarSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PixarSaveOptions), 'rhs' )),
]

# values for enumeration 'PsPhotoCDSize'
psMinimumPhotoCD = 1
psSmallPhotoCD = 2
psMediumPhotoCD = 3
psLargePhotoCD = 4
psExtraLargePhotoCD = 5
psMaximumPhotoCD = 6
PsPhotoCDSize = c_int # enum

# values for enumeration 'PsPhotoCDColorSpace'
psRGB8 = 1
psRGB16 = 2
psLab8 = 3
psLab16 = 4
PsPhotoCDColorSpace = c_int # enum
_PhotoCDOpenOptions._disp_methods_ = [
    DISPMETHOD([dispid(1350069338), helpstring('dimensions of image'), 'propget'], PsPhotoCDSize, 'PixelSize'),
    DISPMETHOD([dispid(1350069338), helpstring('dimensions of image'), 'propput'], None, 'PixelSize',
               ( [], PsPhotoCDSize, 'rhs' )),
    DISPMETHOD([dispid(1147367502), helpstring('profile to use when reading the image'), 'propget'], BSTR, 'ColorProfileName'),
    DISPMETHOD([dispid(1147367502), helpstring('profile to use when reading the image'), 'propput'], None, 'ColorProfileName',
               ( [], BSTR, 'rhs' )),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the image (in pixels per inch)'), 'propget'], c_double, 'Resolution'),
    DISPMETHOD([dispid(1382380364), helpstring('the resolution of the image (in pixels per inch)'), 'propput'], None, 'Resolution',
               ( [], c_double, 'rhs' )),
    DISPMETHOD([dispid(1131172720), helpstring('colorspace for image'), 'propget'], PsPhotoCDColorSpace, 'ColorSpace'),
    DISPMETHOD([dispid(1131172720), helpstring('colorspace for image'), 'propput'], None, 'ColorSpace',
               ( [], PsPhotoCDColorSpace, 'rhs' )),
    DISPMETHOD([dispid(1148154473), 'propget'], PsOrientation, 'Orientation'),
    DISPMETHOD([dispid(1148154473), 'propput'], None, 'Orientation',
               ( [], PsOrientation, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PhotoCDOpenOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PhotoCDOpenOptions), 'rhs' )),
]

# values for enumeration 'PsAnchorPosition'
psTopLeft = 1
psTopCenter = 2
psTopRight = 3
psMiddleLeft = 4
psMiddleCenter = 5
psMiddleRight = 6
psBottomLeft = 7
psBottomCenter = 8
psBottomRight = 9
PsAnchorPosition = c_int # enum

# values for enumeration 'PsExtensionType'
psLowercase = 2
psUppercase = 3
PsExtensionType = c_int # enum
_IndexedConversionOptions._disp_methods_ = [
    DISPMETHOD([dispid(1347447924), helpstring('Type of palette ( default: Exact )'), 'propget'], PsPaletteType, 'Palette'),
    DISPMETHOD([dispid(1347447924), helpstring('Type of palette ( default: Exact )'), 'propput'], None, 'Palette',
               ( [], PsPaletteType, 'rhs' )),
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette (only settable for some palette types)'), 'propget'], c_int, 'Colors'),
    DISPMETHOD([dispid(1884308302), helpstring('number of colors in palette (only settable for some palette types)'), 'propput'], None, 'Colors',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1346790252), 'propget'], PsForcedColors, 'Forced'),
    DISPMETHOD([dispid(1346790252), 'propput'], None, 'Forced',
               ( [], PsForcedColors, 'rhs' )),
    DISPMETHOD([dispid(1416786019), 'propget'], VARIANT_BOOL, 'Transparency'),
    DISPMETHOD([dispid(1416786019), 'propput'], None, 'Transparency',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither'), 'propget'], PsDitherType, 'Dither'),
    DISPMETHOD([dispid(1148474480), helpstring('type of dither'), 'propput'], None, 'Dither',
               ( [], PsDitherType, 'rhs' )),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( 1 - 100 )'), 'propget'], c_int, 'DitherAmount'),
    DISPMETHOD([dispid(1148469613), helpstring('amount of dither. Only valid for diffusion ( 1 - 100 )'), 'propput'], None, 'DitherAmount',
               ( [], c_int, 'rhs' )),
    DISPMETHOD([dispid(1146119544), 'propget'], VARIANT_BOOL, 'PreserveExactColors'),
    DISPMETHOD([dispid(1146119544), 'propput'], None, 'PreserveExactColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1299477605), 'propget'], PsMatteType, 'Matte'),
    DISPMETHOD([dispid(1299477605), 'propput'], None, 'Matte',
               ( [], PsMatteType, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_IndexedConversionOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_IndexedConversionOptions), 'rhs' )),
]
_PhotoshopSaveOptions._disp_methods_ = [
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propget'], VARIANT_BOOL, 'AlphaChannels'),
    DISPMETHOD([dispid(1884504419), helpstring('save alpha channels'), 'propput'], None, 'AlphaChannels',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propget'], VARIANT_BOOL, 'Layers'),
    DISPMETHOD([dispid(1884507250), helpstring('save layers'), 'propput'], None, 'Layers',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propget'], VARIANT_BOOL, 'Annotations'),
    DISPMETHOD([dispid(1884504430), helpstring('save annotations'), 'propput'], None, 'Annotations',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propget'], VARIANT_BOOL, 'SpotColors'),
    DISPMETHOD([dispid(1884509043), helpstring('save spot colors'), 'propput'], None, 'SpotColors',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propget'], VARIANT_BOOL, 'EmbedColorProfile'),
    DISPMETHOD([dispid(1884505424), helpstring('embed color profile in document'), 'propput'], None, 'EmbedColorProfile',
               ( [], VARIANT_BOOL, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PhotoshopSaveOptions), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PhotoshopSaveOptions), 'rhs' )),
]
_PathPointInfo._disp_methods_ = [
    DISPMETHOD([dispid(1347694904), helpstring('the position of the anchor (in coordinates)'), 'propget'], VARIANT, 'Anchor'),
    DISPMETHOD([dispid(1347694904), helpstring('the position of the anchor (in coordinates)'), 'propput'], None, 'Anchor',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1347694905), helpstring('location of the left direction point (in position)'), 'propget'], VARIANT, 'LeftDirection'),
    DISPMETHOD([dispid(1347694905), helpstring('location of the left direction point (in position)'), 'propput'], None, 'LeftDirection',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1347695152), helpstring('location of the right direction point (out position)'), 'propget'], VARIANT, 'RightDirection'),
    DISPMETHOD([dispid(1347695152), helpstring('location of the right direction point (out position)'), 'propput'], None, 'RightDirection',
               ( [], VARIANT, 'rhs' )),
    DISPMETHOD([dispid(1265200740), helpstring('the point type, smooth/corner'), 'propget'], PsPointKind, 'Kind'),
    DISPMETHOD([dispid(1265200740), helpstring('the point type, smooth/corner'), 'propput'], None, 'Kind',
               ( [], PsPointKind, 'rhs' )),
    DISPMETHOD([dispid(1667330160), helpstring('application that the collection belongs to'), 'propget'], POINTER(_Application), 'Application'),
    DISPMETHOD([dispid(0), 'hidden', 'propput'], None, 'ObjectValue',
               ( [], POINTER(_PathPointInfo), 'rhs' )),
    DISPMETHOD([dispid(0), 'hidden', 'propputref'], None, 'ObjectValue',
               ( [], POINTER(_PathPointInfo), 'rhs' )),
]

# values for enumeration 'PsResetTarget'
psAllWarnings = 1
psAllTools = 2
psEverything = 3
PsResetTarget = c_int # enum
__all__ = [ 'psSerialNumber2', 'HSBColor', 'psSquareGeometry',
           'psNoAntialias', 'PsPDFResampleType', 'psPlaceAtEnd',
           'DCS2_SaveOptions', 'psFlag', 'psBackgroundColorMatte',
           'psDocument16Bits', 'psGrayscaleComposite',
           'PsMeasurementSource', 'psDarkenBlend', 'psFishEye',
           'PsStrikeThruType', 'psSquare', 'psBlindsHorizontal',
           'psRandom', 'psPDFJPEG2000MEDLOW', 'psWirelessBitmapSave',
           'psNamedPath', 'psClippingPath', 'psSaturationBlend',
           'PsPointType', 'psOpenCMYK', 'PsPicturePackageTextType',
           'psGrayscale', 'PsGridSize', 'psFontPreviewMedium',
           'PsDocumentMode', 'psPICTResourceFormatSave',
           'psPublicDomain', 'ArtLayers', 'GalleryOptions', 'psSRGB',
           'psFontPreviewExtraLarge', 'psHorizontal', 'psRGB16',
           'psHardMixBlend', 'HistoryStates', 'psPDF15', 'psStrong',
           'psReferenceNameType', 'psHexagon', 'psReplaceSelection',
           'PsPaletteType', 'psDutch',
           'PsGallerySecurityTextColorType', 'psPDFSubSample',
           'psMoviePrime', 'psMonochromeTIFF', 'LayerComps',
           'psTarga32Bits', 'psLightenBlend', 'psGaussianNoise',
           'psGridDashedLine', 'RGBColor', 'psCentered',
           'psHistoryBrush', 'psPostScriptPoints', 'psBMP_R5G6B5',
           'psSolidFillLayer', 'psTitle', 'psExact', 'psSmudge',
           'psThresholdLayer', 'psHalftoneCross', 'psNormalSpherize',
           'psSmall', 'psTimesNewRoman', 'PsWhiteBalanceType',
           'PsRasterizeType', 'psCustomText', '_GrayColor',
           'psNewLab', '_NoColor', '_PresentationOptions',
           'psSoftImageSave', 'psColorBlend', 'psGridDottedLine',
           'psCounterClockwise45', 'psBMP_A8R8G8B8', 'psMultiChannel',
           'psSoftLightBlend', '_DCS1_SaveOptions', 'psNoise',
           'psSerialNumber4', 'psTIFFOpen', 'PsPDFEncodingType',
           'psPlaceBefore', 'psSubtract', 'psBMP4Bits',
           'psStandardOther', 'psMmdd', 'psPortableBitmapOpen',
           'psPDFJPEGLOW', 'PsLayerCompressionType', 'psColorDodge',
           'psCMYK', 'psPhotoFilterLayer', 'psPDFJPEG2000LOSSLESS',
           'psCornerPoint', 'PsSaveBehavior', 'psGlitterRight',
           'psIndexedColor', 'psPICTFileFormatSave',
           'psHalftoneScreen', 'PsCropToType', 'psDarken',
           'PsFileNamingType', 'psWebPalette', 'PsCase',
           'ColorSamplers', 'psVideoLayer', 'psPicas', '_SubPathInfo',
           'PsGeometry', 'psFrench', 'Notifier',
           'psOffsetSetToLayerFill', 'psDarkerColor',
           'psPinLightBlend', 'Channels', 'Application',
           'psNoStandard', 'psStandardBaseline', 'psGlitterDown',
           'psEPSTIFFPreviewOpen', '_GalleryBannerOptions',
           'psNoResampling', 'psBrush', 'psCompuServeGIFSave',
           'psIntersectSelection', 'psPDFX32002', 'psPDFX42008',
           'psWipeUp', 'psOptical', 'PsNewDocumentMode',
           'PsIllustratorPathType', 'psGerman', 'psFolder',
           '_PICTFileSaveOptions', 'psMultiply', 'psConcise',
           'psAllCaches', 'psTIFFSave', 'psHalftoneEllipse',
           'psMiddleRight', 'psNewBitmap', 'psDarkerColorBlend',
           'psConvertToBitmap', 'psSelectedImage', 'psWeb', 'Layers',
           'psLinearBurnBlend', 'PsReferenceFormType', 'psClearBlend',
           'psMasterPerceptual', 'psElectricImageSave',
           'psCameraRAWOpen', 'psPDFJPEGHIGH',
           'psSaturationBlendColor', 'psLandscape', 'psOverlay',
           '_GalleryThumbnailOptions', 'psMaximumPhotoCD',
           'PsDialogModes', 'psPortrait', 'psSubtractBlend',
           'psOffsetWrapAround', 'psArcUpper', 'psExposureLayer',
           'psNo', 'psTiffJPEG', 'psZoomLens', 'psHigh',
           'psPhotoshopDCS_1Save', 'psCustomSettings', 'psPrimaries',
           'PsAntiAlias', 'psWrapAround', 'psGuideDashedLine',
           'PsJavaScriptExecutionMode', 'psPolarToRectangular',
           'psUpperLeft', 'psWhiteText', 'psJPEGOpen', 'psPDFOpen',
           'PsChangeMode', 'psPCXSave', 'psWindowsColors',
           'psLeftJustified', 'psFontPreviewSmall',
           'psColorBalanceLayer', 'psInches', 'psGradientFillLayer',
           'psPercent', 'psDdmm', 'PsSmartBlurMode', 'psListType',
           'psPhotoCDOpen', 'PsUnderlineType',
           'PicturePackageOptions', 'psOptimizedBaseline',
           'psArtHistoryBrush', 'psMetadata', 'psStandard',
           'psPDFNone', 'psMeasureRulerTool',
           'psBrazillianPortuguese', 'PsStrokeLocation',
           'psBrushSize', 'psPDFJPEGMEDLOW', 'psCMYKModel',
           'GalleryCustomColorOptions', 'psFillContent',
           'psPerceptualReduction', 'ExportOptionsSaveForWeb',
           'PsSelectionType', '_IndexedConversionOptions',
           'psBMP_R8G8B8', 'psNoTrasition', 'psSFWGrayscale',
           'psDdmmyy', 'psCloneStamp', 'psPosterizeLayer',
           'psExtraLargeCameraRAW', 'PsPICTCompression', 'psLab',
           'psArc', 'psDifferenceBlend', 'psClipboardCache',
           'psColorMatchRGB', 'psPICT8Bits', 'psLuminosity',
           'psBMPOpen', 'psPoints', 'PsZigZagType', 'psSessionOnly',
           'GalleryBannerOptions', 'psTextContents', 'psFish',
           'psMediaBox', 'psAdaptive', 'psSerialNumber3',
           'psActiveMeasurements', 'psOpenRGB', 'PsTiffEncodingType',
           '_HSBColor', 'psPointText', 'psPNGSave',
           'PsNoiseDistribution', 'TextFonts', 'psEverything',
           'ActionDescriptor', 'psUnmarked', 'psLighterColorBlend',
           'PhotoCDOpenOptions', 'psLuminosityBlend',
           'PsDocumentFill', 'psGrayscaleModel', 'psNever',
           'MeasurementLog', 'psColorDodgeBlend', 'psPortuguese',
           'psUniformNoise', 'psArch', 'psNoGrid', 'PathPoints',
           'psJPEGLowPICT', 'psHistoryCaches',
           '_PicturePackageOptions', 'psBoundingBox',
           'PsGallerySecurityTextRotateType', 'PsWaveType',
           'PsIntent', 'psOldGerman', 'BMPSaveOptions',
           '_PixarSaveOptions', 'psTextLayer', 'psHardLight',
           'PsDescValueType', 'psSemiGray', 'psSwissGerman',
           'psMeasureCountTool', 'psPinLight', 'psPDFJPEG2000MEDHIGH',
           'psFontPreviewNone', 'psCanadianFrench', 'psHue',
           'psSGIRGBOpen', 'psTransparent', 'psLocalPerceptual',
           'psAliasPIXSave', 'psFinnish', '_JPEGSaveOptions',
           'psPreserveDetails', 'psRGB', 'PsGuideLineStyle',
           'psTopLeftPixel', 'psSmallCaps', 'psDoubleType',
           'PsTextType', 'PsGalleryThumbSizeType',
           'psDissolveTransition', 'psJPEGMediumPICT',
           'PsCreateFields', 'psWindowsPalette',
           'psLayerClippingPath', 'PsOtherPaintingCursors',
           'PsExtensionType', 'psSaveForWeb', 'psLab8', 'Document',
           '_ActionList', 'psAscii', 'PsToolType', 'PsWarpStyle',
           'psPDFBicubic', 'psCM', 'psCopyright', 'psSerialNumber1',
           'psLinearLight', 'psSwedish', 'PsBitsPerChannelType',
           'psPDFX1A2003', 'psJPEGLow', 'psMinimumPhotoCD', 'psSine',
           '_PhotoCDOpenOptions', 'psLeft', 'psLargeGrid',
           'psJPEGMaximum', 'psPatternStamp', 'psDissolve',
           'psExclusion', 'psAllPaths', 'psLighterColor',
           'EPSSaveOptions', 'PsCameraRAWSize', 'psAliasPIXOpen',
           'psLowerLeft', 'psOS2', 'psBMP_X8R8G8B8', 'psHeptagon',
           'psGridSolidLine', 'psMacOSByteOrder', 'psWave',
           'psLargeIntegerType', 'PsTrimType', 'psMacOSPalette',
           'psCopyrightedWork', 'PsEliminateFields', 'psScitexCTSave',
           'psSponge', 'psDoNotSaveChanges', '_ContactSheetOptions',
           '_EPSOpenOptions', 'psYymmdd', 'PsTargaBitsPerPixels',
           'LabColor', 'psMediumPhotoCD', 'psOpenLab', 'psManual',
           'PsDirection', 'psBackgroundColor', 'psDifference',
           'psPencil', 'psDocumentBounds', 'psSplitHorizontalOut',
           'psRise', 'psNoResample', 'CameraRAWOpenOptions',
           'psColorReplacementTool', 'PsColorReductionType',
           'PsMeasurementRange', 'psSharpen', 'psLargePhotoCD',
           'PsUnits', '_TiffSaveOptions', 'psAllMeasurements',
           'psNoComposite', 'psCenter', 'psLinearDodgeBlend',
           'psGuideSolidLine', 'psBeforeRunning', 'PsPathKind',
           '_RawFormatOpenOptions', 'psPhotoshopDCS_2Open',
           'psIntegerType', 'psElectricImageOpen', 'psConvertToLab',
           'psCustomThumbnail', 'psScreen', 'psTwo', 'psLinearDodge',
           'SubPathItem', 'TiffSaveOptions', 'psMasterAdaptive',
           'psPDFX1A2001', 'psMiddleLeft', 'Notifiers', 'psHSBModel',
           '_GallerySecurityOptions', 'psSix', 'psNearestNeighbor',
           'psBinary', 'TargaSaveOptions', 'psNewGray',
           'psProofSpace', 'psConstrainWidth', 'psTriangular',
           'psWorking', 'PsRippleSize', 'psCustomPattern',
           'CountItem', 'psLocalSelective', 'psPromptToSaveChanges',
           'psAskWhenSaving', 'psCloudy', 'psHalftoneSquare',
           'PsLayerKind', 'psExtensionUpper', 'psEPSPICTPreviewOpen',
           'psPNGOpen', 'psPDF17', 'psShape', 'psArcLower',
           'PathPoint', 'psCaption', 'psSelectedAreaAlphaChannel',
           'psArial', 'psAsShot', 'psFontPreviewHuge',
           'psAdobeSingleLine', 'psHueBlend', 'PsTypeUnits', 'psAuto',
           'psPCXOpen', 'psBitmap', 'psBMP_A4R4G4B4', 'psNoDither',
           'psTypePoints', 'psNewCMYK', 'psOutsideStroke',
           'psCustomSecurityText', 'PsPICTBitsPerPixels',
           'PsDitherType', 'psJPEGSave', 'psConvertToRGB',
           'PsOpenDocumentType', '_PathPointInfo',
           'psSplitVerticalOut', 'psDocument8Bits', 'psPentagon',
           'psSplitVerticalIn', 'psBMP_A1R5G5B5',
           'psCustomCameraSettings', 'PsColorModel', 'psTile',
           'psTargaOpen', 'psDissolveBlend', 'psTextureFile',
           'psLinearBurn', 'psNormalBlend', 'MeasurementScale',
           'psCameraDefault', 'psConvertToCMYK', 'SubPathItems',
           'psFrostedTexture', '_SolidColor', 'ContactSheetOptions',
           'psDiffusion', 'PsOffsetUndefinedAreas', 'psYyyymmdd',
           'psParagraphText', 'DocumentInfo', 'psMM',
           'psColorBurnBlend', 'psEnglishUSA', 'psPixels', 'psPDF13',
           'psVerticalSpherize', 'PsAnchorPosition',
           'PsJustification', 'psWipeLeft', 'psAllCaps',
           'psPhotoshopOpen', 'psNoDestination',
           'PsBitmapHalfToneType', 'psWipeDown', 'psDivideBlend',
           'psNormal', 'psDocument1Bit', 'psRGB8', 'psRadialBlurGood',
           'psConvertToIndexedColor', 'psReferenceType',
           'psBackgroundEraser', 'psNetscapeGrayMatte', 'psOctagon',
           'PsUndefinedAreas', 'psConvertToMultiChannel', 'psAsk',
           'psNoWarp', 'psRestrictive', 'PsPurgeTarget', 'psBMP8Bits',
           'SGIRGBSaveOptions', 'psMaskedAreaAlphaChannel',
           'psPDFJPEG2000MED', 'psPDFJPEG2000HIGH',
           'PsGallerySecurityTextPositionType',
           'psRLELayerCompression', 'psCreditText', 'psZero',
           'psNone', 'psPassThrough', 'psBleedBox',
           'PsPDFStandardType', 'psDocumentNameMixed', 'psOriginText',
           'psNormalBlendColor', 'psNeverSave', 'psNormalCase',
           'psDisplayNoDialogs', 'PsGalleryConstrainType',
           'PsColorSpaceType', 'PsFormatOptionsType', 'psShapeXOR',
           '_ExportOptionsIllustrator', 'psUserText', 'psMedium',
           'psProPhotoRGB', 'psLarge', 'psSpanish', 'psCaptionText',
           'psHalfThreshold', 'psBMP24Bits',
           'psPICTResourceFormatOpen', 'psLayer3D', 'psUndoCaches',
           'psSqueeze', 'psNoModel', 'psVertical', 'psPrime35',
           'psTwist', 'psBicubicSmoother', 'PsSaveEncoding',
           'psJPEGHighPICT', 'PsForcedColors', 'psPhotoshopEPSSave',
           'ArtLayer', 'psRectangularToPolar', 'psCanvasTexture',
           'TextFont', 'psBottomCenter', 'PathItems', 'psBlackMatte',
           'psHalftoneDiamond', 'psVibrance',
           'GallerySecurityOptions', 'psEvenFields',
           'psWavefrontRLAOpen', 'psRelative', 'psFilename',
           'psZIPLayerCompression', 'psHelvetica', 'PDFOpenOptions',
           '_DCS2_SaveOptions', 'PsOpenDocumentMode',
           'psPlugInColorPicker', 'psBMP16Bits', 'psMediumGrid',
           '_EPSSaveOptions', 'psStrikeBox', 'psAllWarnings',
           'psNorwegian', 'psWindowsColorPicker', 'PsDCSType',
           'psPDFJPEGMED', 'psLinkedLayers', 'psEntireLayer',
           'PsSourceSpaceType', 'psTopRight', 'NoColor',
           'psLogFileAndMetadata', 'psBlackWhiteReduction',
           'psTransparentPixels', 'psCrisp', 'psWhiteMatte',
           'DICOMOpenOptions', 'psCounterClockwise90',
           'PsBMPDepthType', 'psPICT16Bits', 'psPreciseOther',
           'psComponentChannel', 'psPlaceAtBeginning',
           'PsDisplacementMapType', 'psRawSave', 'psJPEGMaximumPICT',
           'psGlitterRightDown', 'PsTextComposer', 'psInversionLayer',
           'psFluorescent', 'SolidColor', 'psScitexCTOpen',
           'psBlindsVertical', 'psBlackText', 'psFlash', 'psRawType',
           '_ActionDescriptor', 'psShapeAdd', 'psSmoothPoint',
           'psLocalAdaptive', 'psBooleanType', 'psPondRipples',
           'psUnderlineLeft', 'psLab16', 'psInflate',
           'psFullyJustified', 'psUpperRight', 'psBMP_X1R5G5B5',
           'psWavefrontRLASave', 'psNormalLayer', 'psBMP1Bit',
           'psPICT2Bits', 'psOverlayBlend', 'psDocument32Bits',
           'psZoom', 'psClockwise90', 'psPDFJPEG',
           'psReferencePropertyType', 'PsByteOrderType',
           'Preferences', 'psCurvesLayer', 'psSpin',
           'psCenterJustified', 'PsLayerType', '_CMYKColor',
           'PsResetTarget', 'psForegroundColorMatte', 'psBMPSave',
           'psPhotoshopEPSOpen', 'psTransparencyChannel',
           'psSaturation', 'psTarga24Bits', 'GalleryThumbnailOptions',
           'psLighten', 'HistoryState', 'LayerSet',
           'psIllustratorPaths', 'psBlackWhite', 'psPDFZip4Bit',
           'psSmartBlurNormal', 'psColorComposite', 'psTopCenter',
           'psCropBox', 'psPreviousPalette', 'LayerSets',
           'psSmallRipple', 'psDICOMOpen', 'psJPEGHigh', 'psNoText',
           'psPhotoshopPDFOpen', 'psFour', 'psTiffZIP', 'psBlur',
           'GalleryImagesOptions', 'psTinyLensTexture', 'psClassType',
           'PsPhotoCDSize', 'psHealingBrush', 'PsSaveDocumentType',
           'psPhotoshopSave', 'PsRadialBlurMethod', 'psPICT32Bits',
           'psBicubic', 'psSeven', 'PsGridLineStyle',
           'psSmallPhotoCD', '_CameraRAWOpenOptions', 'psMmddyy',
           'psDivide', 'psHardLightBlend', 'psExtensionLower',
           'PresentationOptions', 'psSoftLight', 'psHardMix',
           'PsColorProfileType', 'PsMatteType', 'psMaximumCameraRAW',
           '_ExportOptionsSaveForWeb', 'psWindows', 'psClockwise45',
           '_PDFOpenOptions', 'PsResampleMethod', 'psLargeRipple',
           'psUppercase', 'psReferenceOffsetType',
           'psNeverShowDebugger', 'PsCopyrightedType',
           'psIBMByteOrder', '_TargaSaveOptions', '_PDFSaveOptions',
           'psMacintoshColors', 'PhotoshopSaveOptions',
           'psSerialLetterUpper', 'psArtBox', 'CMYKColor', 'psDanish',
           'psSoftImageOpen', 'psDocumentSpace', 'PsElementPlacement',
           'psPlaceAfter', 'psSmartObjectLayer', 'psBoxOut',
           'psSmartBlurOverlayEdge', 'psExclusionBlend', 'psItalian',
           'psObjectType', 'psExtendSelection', 'PNGSaveOptions',
           'psMeasureSelection', 'PsAutoKernType', 'LayerComp',
           'PsChannelType', 'psDuotone', 'psPhotoshopPDFSave',
           'psTrimBox', 'psPlaceInside', 'psLinearLightBlend',
           'psOutFromCenter', 'psColorLookup', 'psEnglishUK',
           'psMediumRipple', 'psAroundCenter', 'psCredit',
           'RawSaveOptions', 'psSharp', 'psLow', 'psLayerMask',
           'psBlackAndWhiteLayer', 'PsPhotoCDColorSpace',
           'PsSaveLogItemsType', 'PsQueryStateType', 'psEPSOpen',
           'psNoPreview', 'psPhotoshopDCS_1Open', '_LabColor',
           'ExportOptionsIllustrator', 'psReferenceIndexType',
           'psRelativeColorimetric', 'psUnderlineRight', 'psCustom',
           'psAdobeRGB', 'psNoTIFFCompression', 'PsShapeOperation',
           'psProgressive', 'psSmallCameraRAW', 'psDocumentNameUpper',
           '_SGIRGBSaveOptions', 'psBottomLeft', 'psBilinear',
           'PsExportType', 'psWipeRight', 'psNynorskNorwegian',
           'psSplitHorizontalIn', 'psPDF16', 'psAllTools',
           'psGradientMapLayer', 'PsCameraRAWSettingsType',
           'PsColorBlendMode', 'psRight', 'DCS1_SaveOptions',
           'BatchOptions', 'psAlwaysSave', 'psTopLeft',
           'psFontPreviewLarge', 'psLogFile', 'psFilenameText',
           'JPEGSaveOptions', 'psMiddleCenter', 'psDisplayAllDialogs',
           'psArtLayer', 'psInsideStroke', 'psStrikeOff',
           'psPerceptual', 'psTraditionalPoints', 'psTungsten',
           '_PhotoshopSaveOptions', 'psConstrainBoth',
           'psLevelsLayer', 'psSmartBlurLow', 'psBicubicSharper',
           'psOddFields', 'psDisplayErrorDialogs', 'psPDF14',
           'psLabModel', 'psHorizontalSpherize', 'psVividLightBlend',
           'Documents', 'psPixarSave', 'PsTextureType', 'psYyddmm',
           'psHalftoneLine', '_PNGSaveOptions',
           '_GalleryCustomColorOptions', 'RawFormatOpenOptions',
           'PDFSaveOptions', 'psPICTFileFormatOpen',
           'PsPDFCompatibilityType', '_BatchOptions', 'psVividLight',
           'PsEditLogItemsType', 'psStringType', 'psMasterSelective',
           'psSmooth', 'PsSmartBlurQuality', 'psActualSize',
           'psPDFJPEG2000LOW', 'psBoxIn', 'psAliasType',
           'PsAdjustmentReference', 'psTextMask', 'PsUrgency',
           'psEightBitTIFF', 'XMPMetadata', 'psCenterStroke',
           'PsBitmapConversionType', 'PsPointKind', '_RGBColor',
           'psFitPage', 'psDodge', 'psHalftoneRound',
           'psPatternDither', 'CountItems', 'PsBlendMode',
           'psJPEGMedium', 'psDocumentNameLower', 'psPixarOpen',
           'psTriangle', 'psMinimumCameraRAW', 'psSmartBlurHigh',
           'psDebuggerOnError', 'psSpotColorChannel',
           'psPhotoshopDCS_2Save', 'psAbsoluteColorimetric',
           'PsColorPicker', 'psSaveAndClose', 'psInterpolation',
           'psBulge', 'psEnumeratedType', 'psBottomRightPixel',
           'psMetrics', 'PsGalleryFontType', 'PsFontPreviewType',
           'PsBatchDestinationType', 'psBMP_X4R4G4B4', 'psThree',
           'psCompuServeGIFOpen', 'psRGBModel', '_ActionReference',
           'psUnitDoubleType', '_BMPSaveOptions', 'psNewRGB',
           'psAdobeEveryLine', 'PsOperatingSystem', 'psFilmstripOpen',
           'psDiffusionDither', 'psChannelMixerLayer', 'psLayerSet',
           'ColorSampler', 'psTypeMM', 'psNoSecurity',
           'psSmartBlurMedium', 'psMediumCameraRAW',
           'psCustomReduction', 'psConstrainHeight', '_Application',
           'PsOrientation', 'IndexedConversionOptions',
           'psCourierNew', 'PsSpherizeMode', 'psDuplication',
           '_GalleryOptions', 'psLowercase', 'psRawOpen',
           'psImageHighlight', 'PsLensType', 'psHueSaturationLayer',
           'PsDepthMapSource', 'psStretchToFit', 'psPDFX32003',
           'psVectorMask', 'psBehindBlend', 'psPrime105',
           'psReferenceIdentifierType', 'TextItem', 'GIFSaveOptions',
           'psPortableBitmapSave', 'psReferenceClassType',
           'PixarSaveOptions', 'Selection', 'psAutomatic',
           'psNoSource', 'ActionReference', 'psPrecise',
           'psTargaSave', 'psRadialBlurBest', 'psAdobeColorPicker',
           'PICTFileSaveOptions', 'BitmapConversionOptions',
           'psCopyrightText', 'psNormalPath', 'PsMagnificationType',
           'GrayColor', 'psExtraLargePhotoCD', 'psBurn',
           'psShapeIntersect', 'PsSaveOptions', 'psNoPICTCompression',
           'PathItem', 'psPatternFillLayer', 'Channel', 'psDetailed',
           'psRightJustified', 'psBicubicAutomatic', 'psSaveChanges',
           'PsRadialBlurQuality', 'psSelectiveColorLayer',
           'psNoForced', 'psConvertToGrayscale', 'psBlocksTexture',
           'PsLanguage', 'psLowerRight', 'psLargeCameraRAW',
           'EPSOpenOptions', 'psEraser', '_GalleryImagesOptions',
           'psShellUpper', 'SubPathInfo', 'psSmallGrid',
           'psBMP32Bits', 'psPDFZip', 'psBottomRight', 'psTypePixels',
           'psSGIRGBSave', 'psScreenBlend', 'psShellLower',
           'psAbsolute', '_RawSaveOptions', 'PathPointInfo',
           'psDiminishSelection', 'psPDFJPEGMEDHIGH', 'ActionList',
           'psReferenceEnumeratedType', 'psWhite', 'psShapeSubtract',
           'PsPaintingCursors', 'psMultiplyBlend', 'psStrikeHeight',
           'PsPolarConversionType', '_BitmapConversionOptions',
           'psDaylight', 'psSmartBlurEdgeOnly', '_GIFSaveOptions',
           'psWirelessBitmapOpen', 'psRepeatEdgePixels',
           'PsGallerySecurityType', 'psAppleColorPicker', 'psAlways',
           'psNoMatte', 'PsPreviewType', 'psPDFAverage',
           'psBrightnessContrastLayer', 'psRadialBlurDraft',
           'psSerialLetterLower', 'psUniform', 'psSelective',
           'PsTransitionType', 'psOffsetRepeatEdgePixels',
           'psWorkPath', 'psColorBurn', 'psTiffLZW', 'psPattern',
           'psOpenGray', '_DICOMOpenOptions', 'psTarga16Bits',
           'psPICT4Bits', 'psUnderlineOff', 'psShade']
from comtypes import _check_version; _check_version('')
