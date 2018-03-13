from comtypes.client import CreateObject
import pathlib

class Converter():
    '''This class converts files to different formats using the COM interface'''
    def __init__(self):
        self.ps = CreateObject('Photoshop.Application')
        self.ps.Preferences.RulerUnits = 1
    
    '''
    Converts files to PNG using Photoshop
    Args:
        files: list of file paths
    '''
    def convertToPNG(self, files):
        for file in files:
            self.ps.Application.Open(file)
            outFile = os.path.splitext(file)[0] + '.png'
            
            options = CreateObject('Photoshop.PNGSaveOptions')
            options.Compression = 1
            options.Interlaced = False
            saveAsCopy = True
            
            self.ps.ActiveDocument.SaveAs(outFile, options, saveAsCopy)
            self.ps.ActiveDocument.Close()

        #Close Photoshop if no documents are open
        if not self.ps.Documents.Count: self.ps.Application.Quit()
        
if __name__ == '__main__':
    import sys
    
    arguments = sys.argv[1:]
    pngConv = Converter().convertToPNG(arguments)