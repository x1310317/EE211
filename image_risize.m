path='C:\Users\x1310\Documents\UCLA\ee 211\image';
cd(path);
files = dir('*.jpg');




for i = 1 : length(files)
    img=imread(files(i).name);
    img_resized=imresize(img,[225,300]);
    filename=files(i).name;
    imwrite(img_resized,filename);
    disp(filename);
end


disp('all');