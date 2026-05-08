import geopandas as gpd
import tkinter as tk
from tkinter import filedialog

def select_and_convert():
    """
    主函数：打开文件选择对话框，执行 GeoJSON 到 Shapefile 的转换。
    """
    # 初始化 tkinter 窗口，但不可视
    root = tk.Tk()
    root.withdraw() 

    print("请选择要转换的 GeoJSON 文件")
    input_geojson = filedialog.askopenfilename(
        title="选择输入的 GeoJSON 文件",
        filetypes=[("GeoJSON files", "*.geojson"), ("All files", "*.*")]
    )
    
    if not input_geojson: # 如果用户取消
        print("未选择输入文件，程序退出。")
        return
        
    print(f"已选择输入文件: {input_geojson}")

    print("\n请选择输出 Shapefile 文件的保存位置和名称...")
    # 打开文件保存对话框
    output_shp = filedialog.asksaveasfilename(
        title="保存输出的 Shapefile 文件",
        defaultextension=".shp",
        filetypes=[("Shapefile", "*.shp"), ("All files", "*.*")]
    )
    
    if not output_shp: # 如果用户取消
        print("未选择输出文件，程序退出。")
        return
        
    print(f"已选择输出文件: {output_shp}")

    try:
        print("\n正在读取 GeoJSON 文件...")
        # 使用 geopandas 读取 GeoJSON 文件
        gdf = gpd.read_file(input_geojson)
        
        print("正在转换并保存为 Shapefile...")
        # 将 GeoDataFrame 保存为 Shapefile
        gdf.to_file(output_shp, driver='ESRI Shapefile', encoding='utf-8')
        
        print(f"\n转换成功！Shapefile 已保存至: {output_shp}")
        
        print(f"- 包含要素数量: {len(gdf)}")
        print(f"- 坐标参考系统 (CRS): {gdf.crs}")
        if not gdf.empty:
            print("- 属性字段:", list(gdf.columns))
        
    except Exception as e:
        print(f"转换过程中发生错误: {e}")
    finally:
        # 关闭 tkinter
        root.destroy()

if __name__ == "__main__":
    select_and_convert()