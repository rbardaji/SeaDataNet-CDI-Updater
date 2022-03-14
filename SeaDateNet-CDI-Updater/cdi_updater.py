import glob


class CDIUpdater:

   def __init__(self, new_l22_and_l5, split_tag):

      self.new_l22_and_l5 = new_l22_and_l5
      self.split_tag = split_tag
      self.cdi_original = None
      self.cdi_updated = None

   def __str__(self):

      response = f'new_l22_and_l5: {self.new_l22_and_l5}\n'
      response += f'split_tag: {self.split_tag}\n'

      return response

   def read_cdi(self, path):
      """
      Read the existing CDI from the Input path
      """
      cdi_content = None

      cdi_file = open(path, "r")
      cdi_content = cdi_file.read()

      if cdi_content is None:
         raise FileNotFoundError

      self.cdi_original = cdi_content
      return self.cdi_original

   def update_cdi(self):
      """
      Update the original CDI.
      """
      if self.cdi_original is None:
         raise Exception("Please, add a original CDI")
      
      end_tag = self.split_tag[0] + '/' + self.split_tag[1:]
      cdi_divided_start = self.cdi_original.split(self.split_tag)
      cdi_divided_end = self.cdi_original.split(end_tag)

      print('cdi_divided_start:', len(cdi_divided_start))
      print('cdi_divided_end:', len(cdi_divided_end))
      print()

      self.cdi_updated = cdi_divided_start[0] + self.split_tag + \
         cdi_divided_start[1] + self.split_tag + cdi_divided_start[2] + \
         self.new_l22_and_l5 + cdi_divided_end[3] + end_tag + \
         cdi_divided_end[4]

      return self.cdi_updated

   def save_cdi(self, path):
      """
      Save CDI to the specified path.
      """
      cdi_file = open(path, 'w')
      cdi_file.write(self.cdi_updated)

      return path


if __name__ == "__main__":

   split_tag = '<gmd:descriptiveKeywords>'

   folder_cdi_list = []
   new_l22_and_l5_list = []

   folder_cdi = '.\\met\\gdc\\pre082017\\'
   gdcpre2017_new_l22_and_l5 = """<gmd:descriptiveKeywords>
            <gmd:MD_Keywords>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1768" >Geonica METEODATA 3000C data logger</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1769" >Geonica STH-S331 {STH-5031} air temperature and relative humidity sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0195" >Young MA05106 Wind Monitor anemometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1001" >Young 61302 barometric pressure sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1770" >LI-COR LI-200R pyranometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1771" >Skye SKU 430 UVB sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0193" >LI-COR LI-190 PAR sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
               </gmd:keyword>
               <gmd:type>
                  <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="sensor_model" >sensor_model</gmd:MD_KeywordTypeCode>
               </gmd:type>
               <gmd:thesaurusName>
                  <gmd:CI_Citation>
                     <gmd:title>
                        <gco:CharacterString>SeaVoX Device Catalogue</gco:CharacterString>
                     </gmd:title>
                     <gmd:alternateTitle>
                        <gco:CharacterString>L22</gco:CharacterString>
                     </gmd:alternateTitle>
                     <gmd:date>
                        <gmd:CI_Date>
                           <gmd:date>
                              <gco:Date>2022-03-04</gco:Date>
                           </gmd:date>
                           <gmd:dateType>
                              <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                           </gmd:dateType>
                        </gmd:CI_Date>
                     </gmd:date>
                     <gmd:edition>
                        <gco:CharacterString>547</gco:CharacterString>
                     </gmd:edition>
                     <gmd:identifier>
                        <gmd:MD_Identifier>
                           <gmd:code>
                              <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L22</gco:CharacterString>
                           </gmd:code>
                        </gmd:MD_Identifier>
                     </gmd:identifier>
                  </gmd:CI_Citation>
               </gmd:thesaurusName>
            </gmd:MD_Keywords>
         </gmd:descriptiveKeywords>
         <gmd:descriptiveKeywords>
            <gmd:MD_Keywords>
               <gmd:keyword>
                  <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="122"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >radiometers</sdn:SDN_DeviceCategoryCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="DLOG"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >data loggers</sdn:SDN_DeviceCategoryCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="101"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >anemometers</sdn:SDN_DeviceCategoryCode>
               </gmd:keyword>
               <gmd:keyword>
                  <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="102"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >meteorological packages</sdn:SDN_DeviceCategoryCode>
               </gmd:keyword>
               <gmd:type>
                  <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="http://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="instrument" >instrument</gmd:MD_KeywordTypeCode>
               </gmd:type>
               <gmd:thesaurusName>
                  <gmd:CI_Citation>
                     <gmd:title>
                        <gco:CharacterString>SeaDataNet device categories</gco:CharacterString>
                     </gmd:title>
                     <gmd:alternateTitle>
                        <gco:CharacterString>L05</gco:CharacterString>
                     </gmd:alternateTitle>
                     <gmd:date>
                        <gmd:CI_Date>
                           <gmd:date>
                              <gco:Date>2016-10-04</gco:Date>
                           </gmd:date>
                           <gmd:dateType>
                              <gmd:CI_DateTypeCode codeList="http://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                           </gmd:dateType>
                        </gmd:CI_Date>
                     </gmd:date>
                     <gmd:edition>
                        <gco:CharacterString>56</gco:CharacterString>
                     </gmd:edition>
                     <gmd:identifier>
                        <gmd:MD_Identifier>
                           <gmd:code>
                              <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L05</gco:CharacterString>
                           </gmd:code>
                        </gmd:MD_Identifier>
                     </gmd:identifier>
                  </gmd:CI_Citation>
               </gmd:thesaurusName>
            </gmd:MD_Keywords>
         </gmd:descriptiveKeywords>
         """
   folder_cdi_list.append(folder_cdi)
   new_l22_and_l5_list.append(gdcpre2017_new_l22_and_l5)

   folder_cdi = '.\\met\\hes\\post012021\\'
   hespost2021_new_l22_and_l5 = """<gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1541" >Campbell Scientific CR1000 data logger</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1673" >Vaisala HMP 155 hygrometer series</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="sensor_model" >sensor_model</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaVoX Device Catalogue</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L22</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2022-03-04</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>547</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L22</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>
            <gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="102"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >meteorological packages</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="DLOG"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >data loggers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="instrument" >instrument</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaDataNet device categories</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L05</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2021-06-15</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>81</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L05</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>"""
   folder_cdi_list.append(folder_cdi)
   new_l22_and_l5_list.append(hespost2021_new_l22_and_l5)

   folder_cdi = '.\\met\\hes\\pre012021\\'
   hespre2021_new_l22_and_l5 = """<gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1541" >Campbell Scientific CR1000 data logger</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1673" >Vaisala HMP 155 hygrometer series</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="sensor_model" >sensor_model</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaVoX Device Catalogue</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L22</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2022-03-04</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>547</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L22</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>
            <gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="102"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >meteorological packages</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="DLOG"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >data loggers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="instrument" >instrument</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaDataNet device categories</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L05</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2021-06-15</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>81</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L05</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>"""
   folder_cdi_list.append(folder_cdi)
   new_l22_and_l5_list.append(hespre2021_new_l22_and_l5)

   folder_cdi = '.\\met\\sdg\\post112018\\'
   sdgpost2018_new_l22_and_l5 = """<gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1541" >Campbell Scientific CR1000 data logger</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0081" >Vaisala HMP temperature and humidity sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0195" >Young MA05106 Wind Monitor anemometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1001" >Young 61302 barometric pressure sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1770" >LI-COR LI-200R pyranometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0193" >LI-COR LI-190 PAR sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="sensor_model" >sensor_model</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaVoX Device Catalogue</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L22</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2022-03-04</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>547</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L22</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>
            <gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="102"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >meteorological packages</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="DLOG"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >data loggers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="122"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >radiometers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="101"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >anemometers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="instrument" >instrument</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaDataNet device categories</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L05</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2021-06-15</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>81</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L05</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>"""
   folder_cdi_list.append(folder_cdi)
   new_l22_and_l5_list.append(sdgpost2018_new_l22_and_l5)

   folder_cdi = '.\\met\\sdg\\pre102018\\'
   sdgpre2018_new_l22_and_l5 = """<gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1769" >Geonica STH-S331 {STH-5031} air temperature and relative humidity sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1768" >Geonica METEODATA 3000C data logger</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0195" >Young MA05106 Wind Monitor anemometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1001" >Young 61302 barometric pressure sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1770" >LI-COR LI-200R pyranometer</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL1771" >Skye SKU 430 UVB sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_SeaVoxDeviceCatalogueCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_SeaVoxDeviceCatalogueCode"  codeListValue="TOOL0193" >LI-COR LI-190 PAR sensor</sdn:SDN_SeaVoxDeviceCatalogueCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="sensor_model" >sensor_model</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaVoX Device Catalogue</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L22</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2022-03-04</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>547</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L22</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>
            <gmd:descriptiveKeywords>
               <gmd:MD_Keywords>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="102"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >meteorological packages</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="DLOG"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >data loggers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="101"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >anemometers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:keyword>
                     <sdn:SDN_DeviceCategoryCode codeSpace="SeaDataNet"  codeListValue="122"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/cdicsrCodeList.xml#SDN_DeviceCategoryCode" >radiometers</sdn:SDN_DeviceCategoryCode>
                  </gmd:keyword>
                  <gmd:type>
                     <gmd:MD_KeywordTypeCode codeSpace="SeaDataNet"  codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#MD_KeywordTypeCode"  codeListValue="instrument" >instrument</gmd:MD_KeywordTypeCode>
                  </gmd:type>
                  <gmd:thesaurusName>
                     <gmd:CI_Citation>
                        <gmd:title>
                           <gco:CharacterString>SeaDataNet device categories</gco:CharacterString>
                        </gmd:title>
                        <gmd:alternateTitle>
                           <gco:CharacterString>L05</gco:CharacterString>
                        </gmd:alternateTitle>
                        <gmd:date>
                           <gmd:CI_Date>
                              <gmd:date>
                                 <gco:Date>2019-12-20</gco:Date>
                              </gmd:date>
                              <gmd:dateType>
                                 <gmd:CI_DateTypeCode codeList="https://vocab.nerc.ac.uk/isoCodelists/sdnCodelists/gmxCodeLists.xml#CI_DateTypeCode"  codeListValue="revision"  codeSpace="ISOTC211/19115" >revision</gmd:CI_DateTypeCode>
                              </gmd:dateType>
                           </gmd:CI_Date>
                        </gmd:date>
                        <gmd:edition>
                           <gco:CharacterString>72</gco:CharacterString>
                        </gmd:edition>
                        <gmd:identifier>
                           <gmd:MD_Identifier>
                              <gmd:code>
                                 <gco:CharacterString>https://www.seadatanet.org/urnurl/SDN:L05</gco:CharacterString>
                              </gmd:code>
                           </gmd:MD_Identifier>
                        </gmd:identifier>
                     </gmd:CI_Citation>
                  </gmd:thesaurusName>
               </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>"""
   folder_cdi_list.append(folder_cdi)
   new_l22_and_l5_list.append(sdgpre2018_new_l22_and_l5)

   for folder_cdi, new_l22_and_l5 in zip(folder_cdi_list, new_l22_and_l5_list):
      filenames = glob.glob(folder_cdi + '\*.xml')
      updater = CDIUpdater(new_l22_and_l5=new_l22_and_l5, split_tag=split_tag)

      for file_cdi in filenames:

         file_cdi_parts = file_cdi.split('\\')
         updated_cdi = ('\\').join(file_cdi_parts[:-1]) + '\\updated\\' + \
            file_cdi_parts[-1]
         
         print('Adding CDI from file:', file_cdi)
         print(updater.read_cdi(file_cdi))
         print()

         print('Updating CDI.')
         print(updater.update_cdi())
         print()

         print('Saving CDI to file:', updater.save_cdi(updated_cdi))
