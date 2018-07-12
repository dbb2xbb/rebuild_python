SEN = '查询小红关注的我的小明的前天昨天创建的任务。'
slots = [
    {'sname':'user_q','sval':'查询','offset':0},
    {'sname':'user_p','sval':'小红','offset':2},
    {'sname':'user_a','sval':'关注','offset':4},
    {'sname':'user_p','sval':'我','offset':7},
    {'sname':'user_p','sval':'小明','offset':9},
    {'sname':'user_t','sval':'前天','offset':12},
    {'sname':'user_t','sval':'昨天','offset':14},
    {'sname':'user_a','sval':'创建','offset':16},
    {'sname':'user_task','sval':'任务','offset':19},
]
class Parse(object):
    def __init__(self,sentence,slots):
        self.sentence = sentence
        self.slots = slots
        self.params = {}
        self.param_list = []
        self.init_hash()

    def __str__(self):
        return '###PARAMS:{}###'.format(self.params)


    def init_hash(self):
        self.ActionHashtb = {
           '创建' : 'creator',
           '执行' : 'executor',
           '关注' : 'Attention',
           '完成' : 'close',
        }

    def ParseSlot(self):
        re_slots = self.slots[::-1]
        for slot in re_slots:
            print(slot)
            if slot['sname'] == 'user_a' and slot['offset'] != 0:
                restIntent = re_slots[re_slots.index(slot)+1:]
                for item in restIntent:
                    if item['sname'] in ['user_t','user_p','user_st']:
                         self.param_list.append({item['sname']:item['sval']})

                self.params[self.ActionHashtb[slot['sval']]] = self.param_list
                self.param_list = []
            if slot['offset'] == 0:
                break


def main():
    p = Parse(SEN,slots)
    p.ParseSlot()
    print(p)

if __name__ == '__main__':
    main()


