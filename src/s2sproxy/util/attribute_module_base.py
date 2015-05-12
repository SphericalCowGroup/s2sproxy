__author__ = 'mathiashedstrom'

class AttributeModuleBase(object):

    def __init__(self, translation, eduid_attr_name, module_attr_name):
        self.eduid_attr_name = eduid_attr_name
        self.module_attr_name = module_attr_name
        self.translation = translation
        self.DATA = self._get_user_data()
        self.GLOBAL_DATA = self._get_global_data()

    def _get_user_data(self):
        raise NotImplementedError

    def _get_global_data(self):
        raise NotImplementedError

    def _search(self, search_param):
        for user_data in self.DATA:
            for attribute_data in user_data[self.module_attr_name]:
                for param in search_param:
                    if attribute_data == param:
                        return user_data
        return {}

    def get_attributes(self, eduid_attributes):
        attr = self._search(eduid_attributes[self.eduid_attr_name])
        attr.update(self.GLOBAL_DATA)
        return self._translate(attr, self.translation)

    def _translate(self, attributes, translation):
        for key, value in translation.iteritems():
            attributes[value] = attributes.pop(key)
        return attributes
