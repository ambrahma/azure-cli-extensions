# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic integration-account batch-configuration create",
)
class Create(AAZCommand):
    """Create a batch configuration for an integration account.

    :example: Create batch configuration
        az logic integration-account batch-configuration create -g rg -n batch --integration-account-name name --batch-group-name group --release-criteria '{recurrence:{frequency:Minute,interval:1},messageCount:10,batchSize:10000}'
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/batchconfigurations/{}", "2019-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.batch_configuration_name = AAZStrArg(
            options=["-n", "--name", "--batch-configuration-name"],
            help="The batch configuration name.",
            required=True,
        )
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "BatchConfiguration"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="BatchConfiguration",
            help="The resource location.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="BatchConfiguration",
            help="The resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.batch_group_name = AAZStrArg(
            options=["--batch-group-name"],
            arg_group="Properties",
            help="The name of the batch group.",
            required=True,
        )
        _args_schema.changed_time = AAZDateTimeArg(
            options=["--changed-time"],
            arg_group="Properties",
            help="The changed time.",
        )
        _args_schema.created_time = AAZDateTimeArg(
            options=["--created-time"],
            arg_group="Properties",
            help="The created time.",
        )
        _args_schema.metadata = AAZFreeFormDictArg(
            options=["--metadata"],
            arg_group="Properties",
            help="The metadata",
        )
        _args_schema.release_criteria = AAZObjectArg(
            options=["--release-criteria"],
            arg_group="Properties",
            help="The batch release criteria.",
            required=True,
        )

        release_criteria = cls._args_schema.release_criteria
        release_criteria.batch_size = AAZIntArg(
            options=["batch-size"],
            help="The batch size in bytes.",
        )
        release_criteria.message_count = AAZIntArg(
            options=["message-count"],
            help="The message count.",
        )
        release_criteria.recurrence = AAZObjectArg(
            options=["recurrence"],
            help="The recurrence.",
        )

        recurrence = cls._args_schema.release_criteria.recurrence
        recurrence.end_time = AAZStrArg(
            options=["end-time"],
            help="The end time.",
        )
        recurrence.frequency = AAZStrArg(
            options=["frequency"],
            help="The frequency.",
            enum={"Day": "Day", "Hour": "Hour", "Minute": "Minute", "Month": "Month", "NotSpecified": "NotSpecified", "Second": "Second", "Week": "Week", "Year": "Year"},
        )
        recurrence.interval = AAZIntArg(
            options=["interval"],
            help="The interval.",
        )
        recurrence.schedule = AAZObjectArg(
            options=["schedule"],
            help="The recurrence schedule.",
        )
        recurrence.start_time = AAZStrArg(
            options=["start-time"],
            help="The start time.",
        )
        recurrence.time_zone = AAZStrArg(
            options=["time-zone"],
            help="The time zone.",
        )

        schedule = cls._args_schema.release_criteria.recurrence.schedule
        schedule.hours = AAZListArg(
            options=["hours"],
            help="The hours.",
        )
        schedule.minutes = AAZListArg(
            options=["minutes"],
            help="The minutes.",
        )
        schedule.month_days = AAZListArg(
            options=["month-days"],
            help="The month days.",
        )
        schedule.monthly_occurrences = AAZListArg(
            options=["monthly-occurrences"],
            help="The monthly occurrences.",
        )
        schedule.week_days = AAZListArg(
            options=["week-days"],
            help="The days of the week.",
        )

        hours = cls._args_schema.release_criteria.recurrence.schedule.hours
        hours.Element = AAZIntArg()

        minutes = cls._args_schema.release_criteria.recurrence.schedule.minutes
        minutes.Element = AAZIntArg()

        month_days = cls._args_schema.release_criteria.recurrence.schedule.month_days
        month_days.Element = AAZIntArg()

        monthly_occurrences = cls._args_schema.release_criteria.recurrence.schedule.monthly_occurrences
        monthly_occurrences.Element = AAZObjectArg()

        _element = cls._args_schema.release_criteria.recurrence.schedule.monthly_occurrences.Element
        _element.day = AAZStrArg(
            options=["day"],
            help="The day of the week.",
            enum={"Friday": "Friday", "Monday": "Monday", "Saturday": "Saturday", "Sunday": "Sunday", "Thursday": "Thursday", "Tuesday": "Tuesday", "Wednesday": "Wednesday"},
        )
        _element.occurrence = AAZIntArg(
            options=["occurrence"],
            help="The occurrence.",
        )

        week_days = cls._args_schema.release_criteria.recurrence.schedule.week_days
        week_days.Element = AAZStrArg(
            enum={"Friday": "Friday", "Monday": "Monday", "Saturday": "Saturday", "Sunday": "Sunday", "Thursday": "Thursday", "Tuesday": "Tuesday", "Wednesday": "Wednesday"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountBatchConfigurationsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountBatchConfigurationsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "batchConfigurationName", self.ctx.args.batch_configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("batchGroupName", AAZStrType, ".batch_group_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("changedTime", AAZStrType, ".changed_time")
                properties.set_prop("createdTime", AAZStrType, ".created_time")
                properties.set_prop("metadata", AAZFreeFormDictType, ".metadata")
                properties.set_prop("releaseCriteria", AAZObjectType, ".release_criteria", typ_kwargs={"flags": {"required": True}})

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_anytype_elements(".")

            release_criteria = _builder.get(".properties.releaseCriteria")
            if release_criteria is not None:
                release_criteria.set_prop("batchSize", AAZIntType, ".batch_size")
                release_criteria.set_prop("messageCount", AAZIntType, ".message_count")
                release_criteria.set_prop("recurrence", AAZObjectType, ".recurrence")

            recurrence = _builder.get(".properties.releaseCriteria.recurrence")
            if recurrence is not None:
                recurrence.set_prop("endTime", AAZStrType, ".end_time")
                recurrence.set_prop("frequency", AAZStrType, ".frequency")
                recurrence.set_prop("interval", AAZIntType, ".interval")
                recurrence.set_prop("schedule", AAZObjectType, ".schedule")
                recurrence.set_prop("startTime", AAZStrType, ".start_time")
                recurrence.set_prop("timeZone", AAZStrType, ".time_zone")

            schedule = _builder.get(".properties.releaseCriteria.recurrence.schedule")
            if schedule is not None:
                schedule.set_prop("hours", AAZListType, ".hours")
                schedule.set_prop("minutes", AAZListType, ".minutes")
                schedule.set_prop("monthDays", AAZListType, ".month_days")
                schedule.set_prop("monthlyOccurrences", AAZListType, ".monthly_occurrences")
                schedule.set_prop("weekDays", AAZListType, ".week_days")

            hours = _builder.get(".properties.releaseCriteria.recurrence.schedule.hours")
            if hours is not None:
                hours.set_elements(AAZIntType, ".")

            minutes = _builder.get(".properties.releaseCriteria.recurrence.schedule.minutes")
            if minutes is not None:
                minutes.set_elements(AAZIntType, ".")

            month_days = _builder.get(".properties.releaseCriteria.recurrence.schedule.monthDays")
            if month_days is not None:
                month_days.set_elements(AAZIntType, ".")

            monthly_occurrences = _builder.get(".properties.releaseCriteria.recurrence.schedule.monthlyOccurrences")
            if monthly_occurrences is not None:
                monthly_occurrences.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.releaseCriteria.recurrence.schedule.monthlyOccurrences[]")
            if _elements is not None:
                _elements.set_prop("day", AAZStrType, ".day")
                _elements.set_prop("occurrence", AAZIntType, ".occurrence")

            week_days = _builder.get(".properties.releaseCriteria.recurrence.schedule.weekDays")
            if week_days is not None:
                week_days.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.batch_group_name = AAZStrType(
                serialized_name="batchGroupName",
                flags={"required": True},
            )
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
            )
            properties.metadata = AAZFreeFormDictType()
            properties.release_criteria = AAZObjectType(
                serialized_name="releaseCriteria",
                flags={"required": True},
            )

            release_criteria = cls._schema_on_200_201.properties.release_criteria
            release_criteria.batch_size = AAZIntType(
                serialized_name="batchSize",
            )
            release_criteria.message_count = AAZIntType(
                serialized_name="messageCount",
            )
            release_criteria.recurrence = AAZObjectType()

            recurrence = cls._schema_on_200_201.properties.release_criteria.recurrence
            recurrence.end_time = AAZStrType(
                serialized_name="endTime",
            )
            recurrence.frequency = AAZStrType()
            recurrence.interval = AAZIntType()
            recurrence.schedule = AAZObjectType()
            recurrence.start_time = AAZStrType(
                serialized_name="startTime",
            )
            recurrence.time_zone = AAZStrType(
                serialized_name="timeZone",
            )

            schedule = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule
            schedule.hours = AAZListType()
            schedule.minutes = AAZListType()
            schedule.month_days = AAZListType(
                serialized_name="monthDays",
            )
            schedule.monthly_occurrences = AAZListType(
                serialized_name="monthlyOccurrences",
            )
            schedule.week_days = AAZListType(
                serialized_name="weekDays",
            )

            hours = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.hours
            hours.Element = AAZIntType()

            minutes = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.minutes
            minutes.Element = AAZIntType()

            month_days = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.month_days
            month_days.Element = AAZIntType()

            monthly_occurrences = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.monthly_occurrences
            monthly_occurrences.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.monthly_occurrences.Element
            _element.day = AAZStrType()
            _element.occurrence = AAZIntType()

            week_days = cls._schema_on_200_201.properties.release_criteria.recurrence.schedule.week_days
            week_days.Element = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
