path='C:\Users\x1310\Documents\UCLA\ee 211\image';
cd(path);
files = dir('*.jpg');
%imshow(img1_binary);
se=[1 1 1 1 1;
    1 1 1 1 1;
    1 1 1 1 1;   
    1 1 1 1 1];
newfolder='image_processed';
if exist(newfolder,'dir')==0
   mkdir(newfolder);
end

for i = 1 : length(files)
    1 1 1 1 1;
    img=imread(files(i).name);
    img_binary=rgb2gray(img);
    img_dilation=imdilate(img_binary,se);
    %imshow(img_dilation);
    img_edge=img_dilation-img_binary;
    %imshow(img_edge);
    img_final=im2bw(img_edge,0.12);
    %imshow(~img_final);
    filename=['image_processed\binary_',files(i).name];
    imwrite(~img_final,filename);
    disp(filename);
end
