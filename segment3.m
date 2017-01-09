function count= segment3(im,w,h)
xgrid=round(w/10);
ygrid=round(h/10);
count=[];
for i=1:10
  for j=1:10
  if i==10&&j!=10
    h=imhist(im(1+(i-1)*xgrid:w,1+(j-1)*ygrid:j*ygrid),10);
  elseif i==10&&j==10
  h=imhist(im(1+(i-1)*xgrid:w,1+(j-1)*ygrid:h),10);
  elseif j==10&&i!=10
  h=imhist(im(1+(i-1)*xgrid:i*xgrid,1+(j-1)*ygrid:h),10);
  else
  h=imhist(im(1+(i-1)*xgrid:i*xgrid,1+(j-1)*ygrid:j*ygrid),10);
  end
  count=[count h'];
  end;
end
endfunction