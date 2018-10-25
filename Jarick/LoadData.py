import pandas as pd

class getPostsFromExcel:
    def __init__(self, filename):
        self.df = pd.read_excel(filename)
        self.entries = self.df.drop(['group', 'url', 'post'], axis=1)

    def insertEntriesInPosts(self, post, entry_dict):
        return f'{post}'.format(**entry_dict)

    def fixPostsInDataFrame(self):
        for key, val in self.entries.T.to_dict().items():
            self.df.post[key] = self.insertEntriesInPosts(self.df.post[key], val)
        return self.df.post.values, self.df['group'].values, self.df.url.values

def main():
    data = getPostsFromExcel('test.xlsx')
    print (data.fixPostsInDataFrame())

if __name__ == "__main__":
    main()
