# SPDX-FileCopyrightText: 2025 Intevation GmbH
#
# SPDX-License-Identifier: Apache-2.0

# generated with https://github.com/openapi-generators/openapi-python-client

"""Contains all the data models used in inputs/outputs"""

from .config_client import ConfigClient
from .config_feed_log_level import ConfigFeedLogLevel
from .forwarder_forward_target import ForwarderForwardTarget
from .get_diff_document_1_document_2_response_200 import GetDiffDocument1Document2Response200
from .get_documents_id_response_200 import GetDocumentsIdResponse200
from .get_pmd_response_200 import GetPmdResponse200
from .get_stats_critical_feed_id_response_200 import GetStatsCriticalFeedIdResponse200
from .get_stats_critical_response_200 import GetStatsCriticalResponse200
from .get_stats_critical_source_id_response_200 import GetStatsCriticalSourceIdResponse200
from .get_stats_cve_feed_id_response_200 import GetStatsCveFeedIdResponse200
from .get_stats_cve_response_200 import GetStatsCveResponse200
from .get_stats_cve_source_id_response_200 import GetStatsCveSourceIdResponse200
from .get_stats_imports_feed_id_response_200 import GetStatsImportsFeedIdResponse200
from .get_stats_imports_response_200 import GetStatsImportsResponse200
from .get_stats_imports_source_id_response_200 import GetStatsImportsSourceIdResponse200
from .get_tempdocuments_id_response_200 import GetTempdocumentsIdResponse200
from .models_advisory_state import ModelsAdvisoryState
from .models_error import ModelsError
from .models_event import ModelsEvent
from .models_id import ModelsID
from .models_publishers_tl_ps import ModelsPublishersTLPs
from .models_stored_query import ModelsStoredQuery
from .models_success import ModelsSuccess
from .models_tlp import ModelsTLP
from .models_workflow import ModelsWorkflow
from .models_workflow_role import ModelsWorkflowRole
from .post_aggregators_body import PostAggregatorsBody
from .post_comments_id_body import PostCommentsIdBody
from .post_documents_body import PostDocumentsBody
from .post_queries_body import PostQueriesBody
from .post_queries_body_kind import PostQueriesBodyKind
from .post_queries_body_role import PostQueriesBodyRole
from .post_sources_body import PostSourcesBody
from .post_sources_id_feeds_body import PostSourcesIdFeedsBody
from .post_sources_id_feeds_body_log_level import PostSourcesIdFeedsBodyLogLevel
from .post_tempdocuments_body import PostTempdocumentsBody
from .put_aggregators_id_body import PutAggregatorsIdBody
from .put_comments_post_id_body import PutCommentsPostIdBody
from .put_queries_id_body import PutQueriesIdBody
from .put_queries_id_body_kind import PutQueriesIdBodyKind
from .put_queries_id_body_role import PutQueriesIdBodyRole
from .put_sources_feeds_id_body import PutSourcesFeedsIdBody
from .put_sources_feeds_id_body_log_level import PutSourcesFeedsIdBodyLogLevel
from .put_sources_id_body import PutSourcesIdBody
from .query_parser_mode import QueryParserMode
from .sources_feed_subscription import SourcesFeedSubscription
from .sources_source_subscription import SourcesSourceSubscription
from .sources_source_subscriptions import SourcesSourceSubscriptions
from .sources_stats import SourcesStats
from .sql_null_string import SqlNullString
from .tempstore_entry import TempstoreEntry
from .time_duration import TimeDuration
from .web_about_info import WebAboutInfo
from .web_argumented_aggregator import WebArgumentedAggregator
from .web_attention_sources_attention import WebAttentionSourcesAttention
from .web_comment import WebComment
from .web_create_comment_comment_result import WebCreateCommentCommentResult
from .web_create_stored_query_create_result import WebCreateStoredQueryCreateResult
from .web_custom import WebCustom
from .web_default_source_config_source_config import WebDefaultSourceConfigSourceConfig
from .web_feed import WebFeed
from .web_feed_logs_entry import WebFeedLogsEntry
from .web_feed_logs_feed_log_entries import WebFeedLogsFeedLogEntries
from .web_feed_result import WebFeedResult
from .web_insert_default_query_exclusion_create_result import WebInsertDefaultQueryExclusionCreateResult
from .web_keep_feed_time_keep_feed_time_config import WebKeepFeedTimeKeepFeedTimeConfig
from .web_overview_documents_document_result import WebOverviewDocumentsDocumentResult
from .web_overview_documents_document_result_documents_item import WebOverviewDocumentsDocumentResultDocumentsItem
from .web_overview_documents_document_result_documents_item_additional_property import (
    WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty,
)
from .web_overview_events_events import WebOverviewEventsEvents
from .web_overview_events_events_events_item import WebOverviewEventsEventsEventsItem
from .web_overview_events_events_events_item_additional_property import (
    WebOverviewEventsEventsEventsItemAdditionalProperty,
)
from .web_overview_temp_documents_temp_documents import WebOverviewTempDocumentsTempDocuments
from .web_pmd_messages import WebPmdMessages
from .web_source import WebSource
from .web_source_age import WebSourceAge
from .web_update_order_query_order import WebUpdateOrderQueryOrder
from .web_view_aggregators_aggregator import WebViewAggregatorsAggregator
from .web_view_events_event import WebViewEventsEvent
from .web_view_sources_sources_result import WebViewSourcesSourcesResult

__all__ = (
    "ConfigClient",
    "ConfigFeedLogLevel",
    "ForwarderForwardTarget",
    "GetDiffDocument1Document2Response200",
    "GetDocumentsIdResponse200",
    "GetPmdResponse200",
    "GetStatsCriticalFeedIdResponse200",
    "GetStatsCriticalResponse200",
    "GetStatsCriticalSourceIdResponse200",
    "GetStatsCveFeedIdResponse200",
    "GetStatsCveResponse200",
    "GetStatsCveSourceIdResponse200",
    "GetStatsImportsFeedIdResponse200",
    "GetStatsImportsResponse200",
    "GetStatsImportsSourceIdResponse200",
    "GetTempdocumentsIdResponse200",
    "ModelsAdvisoryState",
    "ModelsError",
    "ModelsEvent",
    "ModelsID",
    "ModelsPublishersTLPs",
    "ModelsStoredQuery",
    "ModelsSuccess",
    "ModelsTLP",
    "ModelsWorkflow",
    "ModelsWorkflowRole",
    "PostAggregatorsBody",
    "PostCommentsIdBody",
    "PostDocumentsBody",
    "PostQueriesBody",
    "PostQueriesBodyKind",
    "PostQueriesBodyRole",
    "PostSourcesBody",
    "PostSourcesIdFeedsBody",
    "PostSourcesIdFeedsBodyLogLevel",
    "PostTempdocumentsBody",
    "PutAggregatorsIdBody",
    "PutCommentsPostIdBody",
    "PutQueriesIdBody",
    "PutQueriesIdBodyKind",
    "PutQueriesIdBodyRole",
    "PutSourcesFeedsIdBody",
    "PutSourcesFeedsIdBodyLogLevel",
    "PutSourcesIdBody",
    "QueryParserMode",
    "SourcesFeedSubscription",
    "SourcesSourceSubscription",
    "SourcesSourceSubscriptions",
    "SourcesStats",
    "SqlNullString",
    "TempstoreEntry",
    "TimeDuration",
    "WebAboutInfo",
    "WebArgumentedAggregator",
    "WebAttentionSourcesAttention",
    "WebComment",
    "WebCreateCommentCommentResult",
    "WebCreateStoredQueryCreateResult",
    "WebCustom",
    "WebDefaultSourceConfigSourceConfig",
    "WebFeed",
    "WebFeedLogsEntry",
    "WebFeedLogsFeedLogEntries",
    "WebFeedResult",
    "WebInsertDefaultQueryExclusionCreateResult",
    "WebKeepFeedTimeKeepFeedTimeConfig",
    "WebOverviewDocumentsDocumentResult",
    "WebOverviewDocumentsDocumentResultDocumentsItem",
    "WebOverviewDocumentsDocumentResultDocumentsItemAdditionalProperty",
    "WebOverviewEventsEvents",
    "WebOverviewEventsEventsEventsItem",
    "WebOverviewEventsEventsEventsItemAdditionalProperty",
    "WebOverviewTempDocumentsTempDocuments",
    "WebPmdMessages",
    "WebSource",
    "WebSourceAge",
    "WebUpdateOrderQueryOrder",
    "WebViewAggregatorsAggregator",
    "WebViewEventsEvent",
    "WebViewSourcesSourcesResult",
)
