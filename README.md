# 骰子画生成器(Dice Printing Generator)

### 用法

##### Step 1

先使用Photoshop等软件对原图进行去色和色调分离(色调分离中色阶填入 7 )

此步骤教程参见：https://www.bilibili.com/video/BV1UZ4y1d7t5?

##### Step 2

```python
if __name__ == "__main__":
    sc = SrcPic("源文件路径(名称)")
    sc.SetBlockSize(4)
    sc.SetDiceSize(63)
    sc.GeneratePic("保存的文件路径(名称)")
    pass
```

SetBlockSize()：设置单位马赛克的宽度(正方形)

sc.SetDiceSize()：设置每个骰子图片的宽度(最好也是正方形，我提供的图片就是63*63的)

### 依赖库

##### 解释器 Python 3.6.5 或其他 (作者的版本)

##### Pillow