# -*- coding: UTF-8 -*-
try:
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Package Not Installed")
finally:
    pass

class Covid19Trend:
    def __init__(self, year: str, file: str, country: str, inspect: bool) -> None:
        self.title = f"COVID19 TRENDS {year} {country}"
        self.file = file
        self.inspect = inspect
        
    def visualize(self) -> None:
        matplotlib.rcParams["font.family"] = "Heiti TC"
        
        data = pd.read_csv(self.file, header=0x1)
        
        columns = data.columns
        columns = [x.split()[0].lower() if len(x.split()) > 2 else x.lower() for x in columns]
        
        data.columns = columns    
            
        data["时间"] = pd.to_datetime(data["时间"])
        
        for col in data.columns:
            if data[col].dtype == "float64":
                data[col] = pd.to_numeric(data[col])
                
        data.set_index("时间", inplace=True)
        
        ax = data.plot.line(figsize=(10, 6), color=["orange", "red"], linewidth=6)
        plt.title("结核病与新冠肺炎随时间的趋势演变", fontsize=20)
        plt.xlabel("时间", fontsize=14)
        plt.ylabel("趋势数量", fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()
        
        if self.inspect:
            data.head()
            data.info()
        
        
if __name__ == "__main__":
    covidtrends = Covid19Trend(year="2023", country="MALAYSIA", file="data/29-11-2023.csv", inspect=True)
    covidtrends.visualize()
