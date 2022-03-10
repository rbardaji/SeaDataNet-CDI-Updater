

class CDIUpdater:

    def __init__(self, l5, l22):
        self.l5 = l5
        self.l22 = l22
        self.cdi_original = None
        self.cdi_updated = None

    def read_cdi(self, path):
        """
        Read the existing CDI from the Input path
        """
        cdi_content = None

        with (path) as cdi_file:
            cdi_content = cdi_file.read()
        
        if cdi_content is None:
            raise FileNotFoundError

        self.cdi_original = cdi_content
        return True

    def update_cdi(self):
        """
        Update the original CDI.
        """
        if self.cdi_original is None:
            raise 
