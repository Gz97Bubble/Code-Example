using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Geoprocessor;
using ESRI.ArcGIS.Geoprocessing;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.DataManagementTools;
using ESRI.ArcGIS.Display;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.Output;
using ESRI.ArcGIS.SystemUI;
using ESRI.ArcGIS.esriSystem;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void 分析ToolStripMenuItem_Click(object sender, EventArgs e)
        {//缓冲区实验
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            ESRI.ArcGIS.AnalysisTools.Buffer pbuffer = new ESRI.ArcGIS.AnalysisTools.Buffer();
            ILayer pLayer = this.axMapControl1.get_Layer(0);
            IFeatureLayer featLayer = pLayer as FeatureLayer;
            pbuffer.in_features = featLayer;
            string filepath = @"D:\0实验";
            pbuffer.out_feature_class = filepath + "\\" + pLayer.Name + ".shp";
            pbuffer.buffer_distance_or_field = "500 Meters";
            pbuffer.dissolve_option = "ALL";
            gp.Execute(pbuffer, null);
            this.axMapControl1.AddShapeFile(filepath, pLayer.Name);
            this.axMapControl1.MoveLayerTo(0, 3);
        }

        private void 实验ToolStripMenuItem1_Click(object sender, EventArgs e)
        {//水质模型模型插值版（False）
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            gp.AddToolbox(@"D:\Document\dsa.tbx");
            IVariantArray para = new VarArrayClass();
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\工厂.shp");
            //   para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流.shp");
            //   para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流.shp");
            para.Add(@"C:\Users\郭昭\Documents\ArcGIS\Default.gdb\水质扩散");
            try
            {
                gp.Execute("sdf", para, null);
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }

        private void 实验2ToolStripMenuItem_Click(object sender, EventArgs e)
        {//缓冲区用作模型
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            IVariantArray para = new VarArrayClass();
            gp.AddToolbox(@"D:\Document\dsa.tbx");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\工厂.shp");
            para.Add(@"D:\Document\data\zxc.shp");
            try
            {
                gp.Execute("dsa", para, null);
                this.axMapControl1.AddShapeFile(@"D:\Document\data\", "zxc.shp");
                this.axMapControl1.MoveLayerTo(0, 3);
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }

        private void 实验3ToolStripMenuItem_Click(object sender, EventArgs e)
        {//沿线生成点实验
            /*
              Geoprocessor gp = new Geoprocessor();
              gp.OverwriteOutput = true;
                IVariantArray para = new VarArrayClass();
                gp.AddToolbox(@"D:\Document\dsa.tbx");
                 para.Add(@"D:\Document\data\gongchang.shp");
                 para.Add(@"D:\Document\data\hel.shp");
              //   para.Add(@"D:\Document\data\www.mdb\splitpoint");
               //  para.Add(@"D:\Document\data\zxc.shp");
                try
                {
                    gp.Execute("沿线生成点", para ,null);
                    this.axMapControl1.AddShapeFile(@"D:\Document\data\","zxc.shp");
                    this.axMapControl1.MoveLayerTo(0, 3);
                }
                catch (Exception ex)
                {
                    string message = "";
                    for (int i = 0; i < gp.MessageCount; i++)
                    {
                        message += gp.GetMessage(i) + "\r\n";
                    }
                    MessageBox.Show(message + ex.ToString());
                }
                */
            /*

           ESRI.ArcGIS.DataManagementTools.GeneratePointsAlongLines pGeneratePoints = new ESRI.ArcGIS.DataManagementTools.GeneratePointsAlongLines();
         pGeneratePoints.Input_Features = "D:/Document/data/heliu.shp";
           pGeneratePoints.Output_Feature_Class = "D:/Document/data/asd.shp";
           pGeneratePoints.Point_Placement = "DISTANCE";
           pGeneratePoints.Distance = "100 meters";
           pGeneratePoints.Include_End_Points = "false";
           try
            {
           gp.Execute(pGeneratePoints, null);
           axMapControl1.AddShapeFile("D://Document//data//", "asd.shp");
            }
             catch (Exception ex)
             {
                 string message = "";
                 for (int i = 0; i < gp.MessageCount; i++)
                 {
                     message += gp.GetMessage(i) + "\r\n";
                 }
                 MessageBox.Show(message + ex.ToString());
            }
           */
            /*
          IGeoProcessor gp = new GeoProcessor();
          gp.OverwriteOutput = true;
          IGeoProcessorResult result = new GeoProcessorResult();
          IVariantArray parameters = new VarArrayClass();
          try
          {
              parameters.Add(@"D:/Document/data/heliu.shp");
              parameters.Add(@"D:/Document/data/asd.shp");
              parameters.Add("DISTANCE");
              parameters.Add("100 meters");
              parameters.Add("#");
              parameters.Add("NO_END_POINTS");
              gp.Execute("GeneratePointsAlongLines_analysis", parameters, null);
          }
          catch (Exception ex)
          {
              string message = "";
              for (int i = 0; i < gp.MessageCount; i++)
              {
                  message += gp.GetMessage(i) + "\r\n";
              }
              MessageBox.Show(message + ex.ToString());
          }
          */
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            IVariantArray para = new VarArrayClass();
            gp.AddToolbox(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\data\Data.gdb\水质扩散模型");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流.shp");
            para.Add(@"D:\Document\data\points.shp");
            para.Add("100 Meters");
            //   para.Add(@"D:\Document\data\www.mdb\splitpoint");
            //  para.Add(@"D:\Document\data\zxc.shp");
            try
            {
                gp.Execute("沿线等距生成点", para, null);
                this.axMapControl1.AddShapeFile(@"D:\Document\data\", "points.shp");
                this.axMapControl1.MoveLayerTo(0, 3);
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }

        private void 实验4ToolStripMenuItem_Click(object sender, EventArgs e)
        {//沿线生成折点，打断
            IGeoProcessor gp = new GeoProcessor();
            gp.OverwriteOutput = true;
            gp.AddToolbox(@"D:\Document\dsa.tbx");
            IVariantArray para = new VarArrayClass();
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流_地理.shp");
            para.Add(@"D:\Document\data\heliu_splited.shp");
            try
            {
                gp.Execute("poi", para, null);
                this.axMapControl1.AddShapeFile(@"D:\Document\data\", "heliu_splited.shp");
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }

        private void 水质扩散模型ToolStripMenuItem_Click(object sender, EventArgs e)
        {//沿线生成点插值版（Farue）
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            IVariantArray para = new VarArrayClass();
            gp.AddToolbox(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\data\Data.gdb\水质扩散模型");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\工厂_地理.shp");//(@"D:\Document\data\gongchang.shp");
            para.Add("weight");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流_地理.shp");// (@"D:\Document\data\heliu2.shp");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流_地理.shp");// (@"D:\Document\data\heliu2.shp");
            para.Add(@"D:\Document\data\cxz.shp");
            try
            {
                gp.Execute("水质扩散模型插值版", para, null);
                this.axMapControl1.AddShapeFile(@"D:\Document\data\", "cxz.shp");

                //分级渲染
                IClassBreaksRenderer classBreaksRenderer = new ClassBreaksRenderer();
                classBreaksRenderer.Field = "GRIDCODE";             //分级字段
                classBreaksRenderer.BreakCount = 25;                 //分级数目
                int count = classBreaksRenderer.BreakCount;
                classBreaksRenderer.SortClassesAscending = true;    //定义分类是否在TOC中显示Legend
                int i;
                RgbColor color;
                ISimpleLineSymbol pSimpleLineSymbol = new SimpleLineSymbol();
                for (i = 0; i < count; i++){
                    pSimpleLineSymbol = new SimpleLineSymbol();
                    pSimpleLineSymbol.Width = 1.5;
                    color = new RgbColor();
                    if (i < 13) {
                        color.Green = 255;
                        color.Red = 0 + 255/ 13 * i;
                    }else{
                        color.Green = 255 - 255/ 13 * (i- 13);
                        color.Red = 255;
                    }
                   // color.Green = 255 - 255 / 24 * i;
                   // color.Red = 0 + 255 / 24 * i;
                    color.Blue = 0;
                    pSimpleLineSymbol.Color = color;
                    classBreaksRenderer.set_Break(i,i+1);
                    classBreaksRenderer.set_Symbol(i,(ISymbol)pSimpleLineSymbol);
                }
                ILayer ly = new FeatureLayer();
                ly = this.axMapControl1.get_Layer(0);
                IGeoFeatureLayer gf = ly as IGeoFeatureLayer;
                gf.Renderer = classBreaksRenderer as IFeatureRenderer;
                this.axMapControl1.Refresh();
                this.axTOCControl1.Update();
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }

        private void 水质扩散处理ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            IVariantArray para = new VarArrayClass();
            gp.AddToolbox(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\data\Data.gdb\水质扩散模型");

            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\工厂.shp");
            para.Add(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\河流.shp");
            para.Add("weight");
            para.Add(@"D:\Document\data\shuizhi.shp");
            para.Add(@"D:\Document\data\Temp");
            para.Add(false);
            para.Add(100);
            para.Add(4); 

            try
            {
                gp.Execute("水质扩散处理", para, null);
                this.axMapControl1.AddShapeFile(@"D:\Document\data\", "shuizhi.shp");
            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }
        }
 
        private void 弹窗ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 form2 = new Form2();
            form2.ShowDialog(this);

            /*
            MessageBox.Show(gongchang);
            MessageBox.Show(heliu);
            MessageBox.Show(weight);
            MessageBox.Show(Output);
            MessageBox.Show(tempFile);
            MessageBox.Show(Convert.ToString(check));
            MessageBox.Show(Convert.ToString(parameter));
            MessageBox.Show(Convert.ToString(speed));
            */
            Geoprocessor gp = new Geoprocessor();
            gp.OverwriteOutput = true;
            IVariantArray para = new VarArrayClass();
            gp.AddToolbox(@"D:\Document\Postgraduate\项目\化学品管理平台\水质扩散实验数据\data\Data.gdb\水质扩散模型");

            para.Add(gongchang);
            para.Add(heliu);
            para.Add(weight);
            para.Add(Output);
            para.Add(tempFile);
            para.Add(check);
            para.Add(parameter);
            para.Add(speed);

            try
            {
                gp.Execute("水质扩散处理", para, null);
                this.axMapControl1.AddShapeFile(System.IO.Path.GetDirectoryName(Output), System.IO.Path.GetFileName(Output));

                //分级渲染
                IClassBreaksRenderer classBreaksRenderer = new ClassBreaksRenderer();
                classBreaksRenderer.Field = "Value";             //分级字段
                classBreaksRenderer.BreakCount = 25;                 //分级数目
                int count = classBreaksRenderer.BreakCount;
                classBreaksRenderer.SortClassesAscending = true;    //定义分类是否在TOC中显示Legend
                int i;
                RgbColor color;
                ISimpleLineSymbol pSimpleLineSymbol = new SimpleLineSymbol();
                for (i = 0; i < count; i++)
                {
                    pSimpleLineSymbol = new SimpleLineSymbol();
                    pSimpleLineSymbol.Width = 1.5;
                    color = new RgbColor();
                    if (i < 13)
                    {
                        color.Green = 255;
                        color.Red = 0 + 255 / 13 * i;
                    }
                    else
                    {
                        color.Green = 255 - 255 / 13 * (i - 13);
                        color.Red = 255;
                    }
                    // color.Green = 255 - 255 / 24 * i;
                    // color.Red = 0 + 255 / 24 * i;
                    color.Blue = 0;
                    pSimpleLineSymbol.Color = color;
                    classBreaksRenderer.set_Break(i, i + 20);
                    classBreaksRenderer.set_Symbol(i, (ISymbol)pSimpleLineSymbol);
                }
                ILayer ly = new FeatureLayer();
                ly = this.axMapControl1.get_Layer(0);
                IGeoFeatureLayer gf = ly as IGeoFeatureLayer;
                gf.Renderer = classBreaksRenderer as IFeatureRenderer;
                this.axMapControl1.Refresh();
                this.axTOCControl1.Update();


            }
            catch (Exception ex)
            {
                string message = "";
                for (int i = 0; i < gp.MessageCount; i++)
                {
                    message += gp.GetMessage(i) + "\r\n";
                }
                MessageBox.Show(message + ex.ToString());
            }

        }
        string gongchang;
        string heliu;
        string weight;
        string Output;
        string tempFile;
        bool check;
        double parameter;
        double speed;

        public void change(string str1,string str2, string str3, string str4, 
            string str5, bool che, double num1, double num2)
        {
            gongchang = str1;
            heliu = str2;
            weight = str3;
            Output = str4;
            tempFile = str5;
            check = che;
            parameter = num1;
            speed = num2;
        }
    }
    
}
