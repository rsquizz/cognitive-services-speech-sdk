# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.dataset_identity import DatasetIdentity  # noqa: F401,E501
from swagger_client.models.model_identity import ModelIdentity  # noqa: F401,E501


class ModelDefinition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'base_model': 'ModelIdentity',
        'datasets': 'list[DatasetIdentity]',
        'model_kind': 'str',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, str)',
        'locale': 'str'
    }

    attribute_map = {
        'text': 'text',
        'base_model': 'baseModel',
        'datasets': 'datasets',
        'model_kind': 'modelKind',
        'name': 'name',
        'description': 'description',
        'properties': 'properties',
        'locale': 'locale'
    }

    def __init__(self, text=None, base_model=None, datasets=None, model_kind=None, name=None, description=None, properties=None, locale=None):  # noqa: E501
        """ModelDefinition - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._base_model = None
        self._datasets = None
        self._model_kind = None
        self._name = None
        self._description = None
        self._properties = None
        self._locale = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if base_model is not None:
            self.base_model = base_model
        if datasets is not None:
            self.datasets = datasets
        self.model_kind = model_kind
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if locale is not None:
            self.locale = locale

    @property
    def text(self):
        """Gets the text of this ModelDefinition.  # noqa: E501

        The text used to adapt this language model  # noqa: E501

        :return: The text of this ModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ModelDefinition.

        The text used to adapt this language model  # noqa: E501

        :param text: The text of this ModelDefinition.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def base_model(self):
        """Gets the base_model of this ModelDefinition.  # noqa: E501

        The base model used for adaptation  # noqa: E501

        :return: The base_model of this ModelDefinition.  # noqa: E501
        :rtype: ModelIdentity
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        """Sets the base_model of this ModelDefinition.

        The base model used for adaptation  # noqa: E501

        :param base_model: The base_model of this ModelDefinition.  # noqa: E501
        :type: ModelIdentity
        """

        self._base_model = base_model

    @property
    def datasets(self):
        """Gets the datasets of this ModelDefinition.  # noqa: E501

        Datasets used for adaptation  # noqa: E501

        :return: The datasets of this ModelDefinition.  # noqa: E501
        :rtype: list[DatasetIdentity]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ModelDefinition.

        Datasets used for adaptation  # noqa: E501

        :param datasets: The datasets of this ModelDefinition.  # noqa: E501
        :type: list[DatasetIdentity]
        """

        self._datasets = datasets

    @property
    def model_kind(self):
        """Gets the model_kind of this ModelDefinition.  # noqa: E501

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :return: The model_kind of this ModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._model_kind

    @model_kind.setter
    def model_kind(self, model_kind):
        """Sets the model_kind of this ModelDefinition.

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :param model_kind: The model_kind of this ModelDefinition.  # noqa: E501
        :type: str
        """
        if model_kind is None:
            raise ValueError("Invalid value for `model_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["Acoustic", "AcousticAndLanguage", "None", "Language", "CustomVoice", "LanguageGeneration", "Sentiment", "LanguageIdentification", "Diarization"]  # noqa: E501
        if model_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `model_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(model_kind, allowed_values)
            )

        self._model_kind = model_kind

    @property
    def name(self):
        """Gets the name of this ModelDefinition.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this ModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelDefinition.

        The name of the object  # noqa: E501

        :param name: The name of this ModelDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ModelDefinition.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this ModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelDefinition.

        The description of the object  # noqa: E501

        :param description: The description of this ModelDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this ModelDefinition.  # noqa: E501

        The custom properties of this entity  # noqa: E501

        :return: The properties of this ModelDefinition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ModelDefinition.

        The custom properties of this entity  # noqa: E501

        :param properties: The properties of this ModelDefinition.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def locale(self):
        """Gets the locale of this ModelDefinition.  # noqa: E501

        The locale of the contained data  # noqa: E501

        :return: The locale of this ModelDefinition.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ModelDefinition.

        The locale of the contained data  # noqa: E501

        :param locale: The locale of this ModelDefinition.  # noqa: E501
        :type: str
        """

        self._locale = locale

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ModelDefinition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
