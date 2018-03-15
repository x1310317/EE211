path='C:\Users\x1310\Documents\UCLA\ee 211\image\image_processed';
path2='C:\Users\x1310\Documents\UCLA\ee 211\image';

cd(path2);
newfolder='img_delete';
if exist(newfolder,'dir')==0
   mkdir(newfolder);
end

cd(path);
files = dir('*.jpg');
newfolder='img_delete';
if exist(newfolder,'dir')==0
   mkdir(newfolder);
end

for f = 1 : length(files)
    img=imread(files(f).name);
    count =0;
    for i = 1: length(img(:,1))
        for j = 1: length(img(1,:))
            if img(i,j)>200
            count=count+1;
            end
        end
    end
    ratio=count/67500;
    if ratio<0.65
        filename=files(f).name;
        filename_delete=['img_delete\delete_',files(f).name];
        imwrite(img,filename_delete);
        delete(filename);
        cd(path2)
        img_front=imread(filename);
        filename_delete_front=['img_delete\delete_',files(f).name];
        imwrite(img_front,filename_delete);
        delete(filename);
        cd(path);
        disp(filename);
    end
end

disp('all');







