import unittest
import pandas as pd
import numpy as np
import logging 




#rom re_comp import translation, reverse_complement,reading_frame_generator, reading_frame_translator,peptide_frame_chooser
from getfilenames import stats_File_Names
from tabularformatter import disorder_statistics_table_generator
from table_generator import extract_headers,extract_Header_Info

class getNamesTestCase(unittest.TestCase):
     def test_Can_Obtain_Names(self):
        file_names = {'spA8NJZ7.fasta.stats', 'spA8QE76.fasta.stats', 'spP90697.fasta.stats', 'spA8NFF0.fasta.stats', 'spP29030.fasta.stats', 'spP90689.fasta.stats', 'spA8QCH0.fasta.stats', 'spA8Q3T2.fasta.stats', 'spQ27450.fasta.stats', 'spA8QBF3.fasta.stats', 'spA8QE42.fasta.stats', 'spA8NS61.fasta.stats', 'spA8PJX4.fasta.stats', 'spQ4VWF8.fasta.stats', 'spP90707.fasta.stats', 'spA8QDN3.fasta.stats', 'spA8Q8J2.fasta.stats', 'spA8QBB1.fasta.stats', 'spA8PB32.fasta.stats', 'spA8NY27.fasta.stats', 'spA8QC60.fasta.stats', 'spA8QFY9.fasta.stats', 'spA8QFQ3.fasta.stats', 'spA8PV03.fasta.stats', 'spP67877.fasta.stats', 'spA8QCY3.fasta.stats', 'spA8PW87.fasta.stats', 'spQ8IHI1.fasta.stats', 'spA8QB65.fasta.stats', 'spA8QCE7.fasta.stats', 'spA8PHP4.fasta.stats', 'spP90702.fasta.stats', 'spQ9Y193.fasta.stats', 'spA8QFF6.fasta.stats', 'spP10723.fasta.stats', 'spA8PGQ3.fasta.stats', 'spA8NS89.fasta.stats', 'spA8PJJ2.fasta.stats', 'spA8PWB6.fasta.stats', 'spQ17172.fasta.stats', 'spA8Q2R5.fasta.stats', 'spA8Q2H5.fasta.stats', 'spA8PJ38.fasta.stats', 'spA8Q8M5.fasta.stats', 'spQ17162.fasta.stats', 'spA0A0K0JFP3.fasta.stats', 'spA8PF69.fasta.stats', 'spA8NJ91.fasta.stats', 'spP27541.fasta.stats', 'spA8QHQ0.fasta.stats', 'spA8PKH2.fasta.stats', 'spA8QCE4.fasta.stats', 'spP48817.fasta.stats', 'spA8P7J8.fasta.stats', 'spA8QGZ7.fasta.stats', 'spP90703.fasta.stats', 'spP38542.fasta.stats', 'spQ01202.fasta.stats', 'spP48822.fasta.stats', 'spQ93140.fasta.stats', 'spP91850.fasta.stats', 'spO77049.fasta.stats', 'spQ93142.fasta.stats', 'spP48812.fasta.stats'}
        self.assertEqual(stats_File_Names("tests/b_malayi_reviewed"),file_names)

class generate_Headers_From_FastaTestCase(unittest.TestCase):
    def test_headers_from_file(self):
        from cache import getHeaders,subsetted_Headers
        headers = getHeaders()
        self.assertEqual(extract_headers("fasta/brugia_malayi_reviewed.fasta"), headers)

        ss_Headers = subsetted_Headers()
        self.assertEqual(extract_Header_Info(headers),ss_Headers)

class assure_Header_Formatting_is_LosslessTestCase(unittest.TestCase):
    #Fairly heavy editing/regexing of Fasta headers was going on, so this is 
    #assuring that thing was missing. It's hard to make a test for this sort of stuff,
    #as it's mostly eyeballing
        def test_formatted_header_in_raw_header(self):
            from cache import truncated_Headers,getHeaders
            control = truncated_Headers()
            # Constant - same as above, except >sp|P90689|ACT_BRUMA is taken out
            
            
            raw_Headers = getHeaders()

            subsetted_Headers = extract_Header_Info(raw_Headers)
            outputWithPadding = [[x[1], " "*(70-len(x[1]))] for x in subsetted_Headers]
            
            outputToTest = [x[0] for x in outputWithPadding]
            #control = control[0]
            logging.debug(control,outputToTest)
            
            
            for i in range(len(control)):
                
                self.assertIn(outputToTest[i],control[i])
                
                #Making sure parameters are taken out
                self.assertNotIn('OS=',outputToTest[i])
                self.assertNotIn('GN=',outputToTest[i])
                self.assertNotIn('PE=',outputToTest[i])
                self.assertNotIn('SV=',outputToTest[i])
                self.assertNotIn('malayi',outputToTest[i])
                
                #Test Validation
                
                self.assertIn('OS',control[i])
                self.assertIn('malayi',control[i])
                
          
    
    

class createPandaTableTestCase(unittest.TestCase):
    def test_produces_single_row(self):
        from cache import getPandaRow
        # This compares two singular tables by taking a pandas data frame and converting it by row.values
        #We then have a np.array (seen below) which is organized by set comprehensions
        row = getPandaRow()#np.array([[1, 100.0, 'A8NJZ7', 1, 1, 122]], dtype=object)
        row = {row[0][x] for x in range(0,6)}
        
        gen_row = disorder_statistics_table_generator("tests/b_malayi_reviewed/spA8NJZ7.fasta.stats")
        gen_row = gen_row.values
        gen_row = {gen_row[0][x] for x in range(0,6)}
        self.assertEqual(gen_row,row)
        
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main(verbosity=1)