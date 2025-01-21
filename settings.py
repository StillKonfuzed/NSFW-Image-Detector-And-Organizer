


COMMITCHANGES = False #commit changes | set False if you do not want to commit changes to files

#paths
SCANPATH = 'G:/' #base folder path
TEMPPATH = SCANPATH + 'Zz_temp/' #I normally dump images on my temp folder

#add words to files
ISNUDE = '_processed_' #nude images will be renamed to _processed_{existingImageName}.{existingExtension}
ISNOTNUDE = '_filtered_' #non-nude images will be renamed to _filtered_{existingImageName}.{existingExtension}
ISCORRUPT = '_corrupt_' #corrupt images will be renamed to _corrupt_{existingImageName}.{existingExtension}


#resolution
ISLOWRES = '_lowres_'
LOWRESMB = 1 #images lower than 1024kb is considered low res, incresase 
ISHIGHRES = '_highres_'






