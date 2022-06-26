from PIL import Image


def find_val(_list, val):
    for i in range(len(_list)):
        if _list[i] == val:
            return i
    return -1


class GrayBlock:
    col = 0
    row = 0
    sum_rgb = 0
    rank = 0

    def __init__(self, colx, rowx, sum_val):
        self.col = colx
        self.row = rowx
        self.sum_rgb = sum_val


class SrcPic:
    src_img = None
    img_width = 0
    img_height = 0
    block_size = 0
    col_block_count = 0
    row_block_count = 0
    dice_size = 0
    dice_list = []
    grayscale_value_list = []
    grayscale_list = []

    def __init__(self, img_path):
        # 读取原图
        self.src_img = Image.open(img_path)
        self.src_img = self.src_img.convert("RGB")
        self.img_height = self.src_img.height
        self.img_width = self.src_img.width
        # 读取骰子图片
        for i in range(7):
            self.dice_list.append(Image.open(".\\dice_img\\dice_{0}.jpg".format(i)))
        return

    def SetBlockSize(self, size):
        self.block_size = size
        return

    def SetDiceSize(self, size):
        self.dice_size = size
        return

    def AnalyzeGrayImg(self):
        # 分析灰度图
        self.col_block_count = int((self.img_width - self.img_width % self.block_size) / self.block_size)
        # print(col_block_count)
        self.row_block_count = int((self.img_height - self.img_height % self.block_size) / self.block_size)
        # print(row_block_count)
        for col in range(self.col_block_count):
            for row in range(self.row_block_count):
                sum_rgb = 0
                r, g, b = self.src_img.getpixel((col * self.block_size, row * self.block_size))
                sum_rgb = r + g + b
                # 范围限制
                sum_rgb = (sum_rgb // 100) * 100
                if sum_rgb > 600:
                    sum_rgb = 600
                self.grayscale_list.append(GrayBlock(col, row, sum_rgb))

                if sum_rgb not in self.grayscale_value_list:
                    self.grayscale_value_list.append(sum_rgb)

        self.grayscale_value_list.sort()
        for k in range(len(self.grayscale_list)):
            self.grayscale_list[k].rank = find_val(self.grayscale_value_list, self.grayscale_list[k].sum_rgb)
        # print(self.grayscale_list)
        return

    def GeneratePic(self, file_name):
        self.AnalyzeGrayImg()
        obj = Image.new("RGB", (self.col_block_count * self.dice_size, self.row_block_count * self.dice_size))
        for i in range(len(self.grayscale_list)):
            obj.paste(self.dice_list[find_val(self.grayscale_value_list, self.grayscale_list[i].sum_rgb)],
                      (self.grayscale_list[i].col * self.dice_size, self.grayscale_list[i].row * self.dice_size))
        obj.save(file_name)
        pass


if __name__ == "__main__":
    sc = SrcPic(".\\src_block.jpg")
    sc.SetBlockSize(4)
    sc.SetDiceSize(63)
    sc.GeneratePic("src_dice.jpg")
    pass
