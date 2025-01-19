'''
    Creatinal : Simple factory
        have 3 component=.> 1-creator 2- product 3- client
'''



class Data:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension


class Processor:
    """
    have three section as : client , product, creator
    """

    #  client
    def edit(self, file):
        result = self.get_file(file)
        return result(file)

    #  section creator
    def get_file(self, file):
        if file.extension == 'yaml':
            return self.edit_yaml
        elif file.extension == 'json':
            return self.edit_json
        else:
            raise ValueError('this extension not valid for this software')

    # section product
    def edit_yaml(self, file):
        print(f'editing with yaml extension for file {file.name}.{file.extension}')

    def edit_json(self, file):
        print(f'editing with json extension for file {file.name}.{file.extension}')


data = Data('docker-compose', 'yaml')
processor = Processor()
processor.edit(data)
