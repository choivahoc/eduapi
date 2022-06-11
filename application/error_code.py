#!/usr/bin/env python
# -*- coding: utf-8 -*-

HTTP_100_CONTINUE = {
}
HTTP_101_SWITCHING_PROTOCOLS = {
}
HTTP_200_OK = {
}
HTTP_201_CREATED = {
}
HTTP_202_ACCEPTED = {
}
HTTP_203_NON_AUTHORITATIVE_INFORMATION = {
}
HTTP_204_NO_CONTENT = {
}
HTTP_205_RESET_CONTENT = {
}
HTTP_206_PARTIAL_CONTENT = {
}
HTTP_300_MULTIPLE_CHOICES = {
}
HTTP_301_MOVED_PERMANENTLY = {
}
HTTP_302_FOUND = {
}
HTTP_303_SEE_OTHER = {
}
HTTP_304_NOT_MODIFIED = {
}
HTTP_305_USE_PROXY = {
}
HTTP_306_RESERVED = {
}
HTTP_307_TEMPORARY_REDIRECT = {
}
HTTP_400_BAD_REQUEST = {
    # Error code for asset
    1040: 'System ID {0} does not exist',
    1041: 'System {0} already exists',
    1042: 'Data source {0} is not valid',
    1043: 'Application {0} and path {1} does not exist',
    1044: 'Application {0} does not exist',

    1050: "Key {0} is not valid",
    1051: "Field {0} is required and cannot be empty",
    1052: "Zone {0} does not exist",
    1053: "Data type is not valid",
    1054: "No information for Zone name",
    1055: "Server {0} does not exist",
    1056: "Tag {0} is not valid",
    1057: "Program {0} does not exist",
    1058: "Object ID {0} does not exist",
    1059: 'A zone with that zone-id already exists',

    # Error code for alert (v1.1)
    1060: "Alert '{0}' does not exist",
    1061: "Can not find alert in database",
    1062: "Parameter '{0}' is not valid",
    1063: "Can not update to database",
    1064: "Can not execute this query",

    # Error code for asset_verify
    1070: "Parameter '{0}' is not valid",
    1071: "Rule verify '{0}' does not exist",
    1072: "No fields updated",
    1073: "Missing parameter '{0}'",
    1074: "Can not find id '{0}'",
    1075: "Rule ID {0} does not exist",
    1076: 'Rule already exists',
    1077: 'Rule type {0} is not valid',

    # Error code for correlation
    1080: "Parameter '{0}' is not valid",
    1081: "Metakey does not exist",
    1082: "Delete metakey failed",
    1083: "Missing parameter '{0}'",
    1084: "Update failed",
    1085: "Staticlist does not exist",
    1086: "Delete staticlist failed",
    1087: "Staticlist name '{0}' already exists",
    1088: "Metakey name '{0}' already exists",
    1089: "Rule does not exist",
    1090: "Rule ID {0} already exists",
    1091: "Delete staticlist data failed",
    1092: "Staticlist data does not exist",
    1093: "Staticlist value '{1}' already exists",
    1094: "Invalid syntax",
    1095: "Undeploy: {0}",
    1096: "Deploy: {0}",
    1097: "Verify Syntax: {0}",
    1098: "Verify Syntax: {0}",
    1099: "Add staticlist failed",
    1100: "Activelist name '{0}' already exists",
    1101: "Activelist does not exist",
    1102: "Delete activelist data failed",
    1103: "Update data failed",
    1104: "Add activelist failed",
    1105: "Missing parameter",
    1106: "Invalid parameter",
    1107: "Request processing error",
    1108: "View file: {0} error",
    1109: "Get content file error",
    1110: "These fields 'maxsize' and 'TTL' must be an integer and larger than 0",

    # Error code for ticket
    1300: "Invalid argument",
    1301: "Missing parameter '{0}'",
    1302: "Parent ticket {0} does not exist",
    1303: "Alert {0} is assigned to another ticket",
    1304: "Alert {0} is assigned or marked as false-positive",
    1305: "There is nothing to update",
    1306: "Ticket title is used for another ticket",
    1307: "All child tickets must be closed before closing parent ticket",
    1308: "Can not add parent ticket",
    1309: "Can not delete because some alerts is assigned to this ticket",
    1310: "Can not delete because security baseline is assigned to this ticket",
    1311: "Data empty",
    1312: "Ticket {0} does not exist",
    1313: "Alert is assigned to another ticket",
    1314: "Assign group {0} does not exist",

    # Error code for ticket status
    1320: "Status index {0} already exists",
    1321: "Status index {0} does not exists",
    1330: "Status code {0} already exists",
    1331: "Status code {0} does not exist",
    1340: "Ticket status transition already exists",
    1341: "Ticket status transition does not exist",

    # Error code for report
    1400: "Parameter '{0}' is not valid",

    2000: "Cannot create confirmation",
    2001: "Request_id not found",
    2002: "Not supported",

    # Error code for notification
    40001: 'Rule name [{0}] already exists',
    40002: 'Metatada {0} with type {1} already exists',

    # Error code for SE
    4050: 'Error when requesting to RAWebservice with server {0}',
    4051: 'Private key of server {0} is not encrypted',
    4052: 'Task {0} not found',
    4053: 'Server {0} is existed',
    4054: 'Certification is currently used by server {0}',
    4055: 'Server {0} is not existed',
    4056: 'Server {0} is not allowed to be accepted',
    4057: 'Server {0} is not allowed to be rejected',
    4058: 'Server {0} is not allowed to be renewed',
    4059: 'Server {0} is recently updated',
    4060: 'Certification of {0} is existed',
    4061: 'RAWS authentication error at request for {0}',
    4062: 'RAWS missing information error at request for {0}',
    4063: 'RAWS username-duplication error at request for {0}',
    4064: 'RAWS unknown error at request for {0}',
    4065: 'RAWS cannot be connected at request for {0}',
    4066: 'Template {0} not found',
    4067: 'Parameter `servers` not valid',
    4068: 'Parameter `params` not valid',
    4069: 'Certification of {0} does not exist',


}
HTTP_401_UNAUTHORIZED = {
    # Error code for asset
    2040: "You do not have permission to view this server",
    2041: "You do not have permission to update this server",
    2042: "You do not have permission to update this application",
    2043: "You do not have permission to update this rule",
    2044: "You do not have permission to delete this rule",
    2045: "You do not have permission to view this rule",
    2046: "You do not have permission to create this rule",
    2047: "You do not have permission to view this application",
    2048: "You do not have permission to view this network device",

    # Error code for ticket
    2300: "Ticket does not exist or you don't have permission to view this ticket"
}
HTTP_402_PAYMENT_REQUIRED = {
}
HTTP_403_FORBIDDEN = {
}
HTTP_404_NOT_FOUND = {
    5050: 'Server {0} not found',
    5051: 'Cert of server {0} not found',
}
HTTP_405_METHOD_NOT_ALLOWED = {
}
HTTP_406_NOT_ACCEPTABLE = {
}
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = {
}
HTTP_408_REQUEST_TIMEOUT = {
}
HTTP_409_CONFLICT = {
}
HTTP_410_GONE = {
}
HTTP_411_LENGTH_REQUIRED = {
}
HTTP_412_PRECONDITION_FAILED = {
}
HTTP_413_REQUEST_ENTITY_TOO_LARGE = {
}
HTTP_414_REQUEST_URI_TOO_LONG = {
}
HTTP_415_UNSUPPORTED_MEDIA_TYPE = {
}
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = {
}
HTTP_417_EXPECTATION_FAILED = {
}
HTTP_422_UNPROCESSABLE_ENTITY = {
    42201: 'Rule name: {0} already exists',
    42202: 'Metadata: {0} - {1} already exists',
    42203: 'Language: {0} already exists'
}
HTTP_428_PRECONDITION_REQUIRED = {
}
HTTP_429_TOO_MANY_REQUESTS = {
}
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = {
}
HTTP_500_INTERNAL_SERVER_ERROR = {
    2000: 'Database error with query: {0}',
    50001: 'Failed to update rule.',
}
HTTP_501_NOT_IMPLEMENTED = {
}
HTTP_502_BAD_GATEWAY = {
}
HTTP_503_SERVICE_UNAVAILABLE = {
}
HTTP_504_GATEWAY_TIMEOUT = {
}
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = {
}
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = {
}
