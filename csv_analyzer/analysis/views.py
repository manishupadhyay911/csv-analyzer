import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

def handle_uploaded_file(f):
    file_path = os.path.join('media', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)

            # Data Analysis
            head = data.head().to_html()
            description = data.describe().to_html()
            missing_values = data.isnull().sum().to_frame().to_html()

            # Data Visualization
            plt.figure(figsize=(10, 6))
            histograms = []
            for column in data.select_dtypes(include=[np.number]).columns:
                plt.figure()
                sns.histplot(data[column].dropna(), kde=True)
                plot_path = os.path.join('media', f'{column}_histogram.png')
                plt.savefig(plot_path)
                histograms.append(plot_path)
                plt.close()

            context = {
                'form': form,
                'head': head,
                'description': description,
                'missing_values': missing_values,
                'histograms': histograms,
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

