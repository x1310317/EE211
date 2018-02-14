path='C:\Users\x1310\Documents\UCLA\ee 211\image';
cd(path);
files = dir('*.jpg');
disp('Begin');
for i = 1 : length(files)
    img=imread(files(i).name);
    mysize=size(img);
    if numel(mysize)<3
        disp(files(i).name);
        delete(files(i).name);
    end
end
disp('End');