#Main stores all data into one matrix called allData
pkg load image
tic
allData=[];
allLabel=[];
count=1;l=[];t=[];
for sub = 1:10
  for ges = 1:36
  if sub!=10&&ges<=9
  matFileName = sprintf('sub_depth_0%d_0%d.mat',sub,ges);
  elseif sub!=10 && ges>9
  matFileName = sprintf('sub_depth_0%d_%d.mat',sub,ges);
  elseif sub==10&&ges<=9
  matFileName = sprintf('sub_depth_%d_0%d.mat',sub,ges);
  else
  matFileName = sprintf('sub_depth_%d_%d.mat',sub,ges);
  endif
  
  if exist(matFileName, 'file')
  [l,t]=loadsample3(matFileName,ges);
  allData=[allData;t]
  allLabel=[allLabel;l]
  else 
  fprintf('File %s does not exist.\n', matFileName);
  endif
  endfor  
endfor


save AllLabel_3.txt allLabel;
save AllData_3.txt allData;
    
toc 