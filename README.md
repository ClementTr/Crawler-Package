# Crawler-Package

In your virtual env do:

pip install -r requirements.txt

Then install our own package doing:

cd mypkg ; pip install . -U ; mypkg-run

You can now create your own kernel for jupyter doing in your virtual env:

pip install ipykernel ; python -m ipykernel install --user --name ENVNAME --display-name "Python3crawler"

Now run the first notebook in order to recover data (select the kernel you created):
jupyter notebook Crawler.ipynb

Once you recovered your data saved in data repository you can run the notebook analysis (select the kernel you created):
jupyter notebook Crawler_Analysis.ipynb
