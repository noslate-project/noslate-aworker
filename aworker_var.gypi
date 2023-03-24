{
  'variables': {
    'aworker_use_snapshot%': 'true',
    'aworker_use_curl%': 'true',

    'aworker_tag_v': '<!(git rev-parse --short=6 HEAD)',
    'mksnapshot_exec': '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)aworker_mksnapshot<(EXECUTABLE_SUFFIX)',
    'proto_files': [
      'src/proto/noslated.proto',
      'src/proto/rpc.proto',
      'src/proto/aworker_cache.proto',
    ],
    'proto_v8_files': [
      'src/proto/aworker_cache.proto',
    ],
    'proto_gen_files': [
      '<(SHARED_INTERMEDIATE_DIR)/proto/noslated.pb.cc',
      '<(SHARED_INTERMEDIATE_DIR)/proto/rpc.pb.cc',
      '<(SHARED_INTERMEDIATE_DIR)/proto/aworker_cache.pb.cc',
    ],
    'aworker_snapshot_main%': '',
    'aworker_source_files': [
      'src/agent_channel/noslated_data_channel.cc',
      'src/agent_channel/noslated_diag_channel.cc',
      'src/agent_channel/diag_channel.cc',
      'src/alarm_timer.cc',
      'src/async_wrap.cc',
      'src/binding/core/text.cc',
      'src/binding/internal/process.cc',
      'src/binding/internal/process_env_vars.cc',
      'src/binding/internal/aworker_bytes.cc',
      'src/binding/internal/aworker_cache.cc',
      'src/binding/internal/aworker_constants.cc',
      'src/binding/internal/aworker_crypto.cc',
      'src/binding/internal/aworker_file.cc',
      'src/binding/internal/aworker_i18n.cc',
      'src/binding/internal/aworker_immediate.cc',
      'src/binding/internal/aworker_perf.cc',
      'src/binding/internal/aworker_serdes.cc',
      'src/binding/internal/aworker_signals.cc',
      'src/binding/internal/aworker_timers.cc',
      'src/binding/internal/aworker_tracing.cc',
      'src/binding/internal/aworker_types.cc',
      'src/binding/internal/v8_utils.cc',
      'src/binding/url.cc',
      'src/contextify/context.cc',
      'src/contextify/contextify.cc',
      'src/contextify/script.cc',
      'src/debug_utils.cc',
      'src/diag_report_utils.cc',
      'src/diag_report.cc',
      'src/command_parser.cc',
      'src/command_parser_group.cc',
      'src/error_handling.cc',
      'src/external_references.cc',
      'src/handle_wrap.cc',
      'src/immortal.cc',
      'src/ipc/ipc_delegate_impl.cc',
      'src/ipc/ipc_service.cc',
      'src/ipc/ipc_socket.cc',
      'src/ipc/ipc_socket_server.cc',
      'src/ipc/ipc_socket_uv.cc',
      'src/ipc/uv_loop.cc',
      'src/json_utils.cc',
      'src/loop_latency_watchdog.cc',
      'src/macro_task_queue.cc',
      'src/metadata.cc',
      'src/module_wrap.cc',
      'src/native_module_manager.cc',
      'src/aworker.cc',
      'src/aworker_binding.cc',
      'src/aworker_logger.cc',
      'src/aworker_perf.cc',
      'src/aworker_platform.cc',
      'src/snapshot/snapshot_builder.cc',
      'src/snapshot/snapshotable.cc',
      'src/task_queue.cc',
      'src/tracing/trace_agent.cc',
      'src/tracing/trace_event.cc',
      'src/tracing/trace_writer.cc',
      'src/tracing/traced_value.cc',
      'src/url/uri_encode.cc',
      'src/url/url.cc',
      'src/util.cc',
      'src/watchdog.cc',
      'src/zero_copy_file_stream.cc',
      'src/zlib/unzip.cc',
      'src/zlib/unzip_task.cc',
      'src/zlib/zip.cc',
      'src/zlib/zip_task.cc',
      'src/zlib/zlib_task.cc',
      'src/zlib/zlib_wrapper.cc',
      '<(SHARED_INTERMEDIATE_DIR)/aworker_native_modules.cc',
      '<(SHARED_INTERMEDIATE_DIR)/proto-inl.pb.h',
      '<@(proto_gen_files)',
    ],
    'aworker_library_files': [
      'lib/agent_channel.js',
      'lib/assert.js',
      'lib/beacon.js',
      'lib/bytes.js',
      'lib/bootstrap/loader.js',
      'lib/bootstrap/main_fork.js',
      'lib/bootstrap/main.js',
      'lib/bootstrap/per_execution.js',
      'lib/bootstrap/aworker.js',
      'lib/cache.js',
      'lib/console.js',
      'lib/console/console.js',
      'lib/console/debuglog.js',
      'lib/console/format.js',
      'lib/crypto.js',
      'lib/dapr/1.0.js',
      'lib/dapr/common.js',
      'lib/dapr.js',
      'lib/dom/abort_controller.js',
      'lib/dom/abort_signal.js',
      'lib/dom/event_objects.js',
      'lib/dom/event_target.js',
      'lib/dom/event_wrapper.js',
      'lib/dom/event.js',
      'lib/dom/exception.js',
      'lib/dom/file.js',
      'lib/dom/iterable.js',
      'lib/dom/location.js',
      'lib/encoding.js',
      'lib/fetch/drivers/agent.js',
      'lib/fetch/drivers/curl.js',
      'lib/fetch/body_helper.js',
      'lib/fetch/constants.js',
      'lib/fetch/fetch.js',
      'lib/fetch/form.js',
      'lib/fetch/body.js',
      'lib/fetch/headers.js',
      'lib/file.js',
      'lib/global/aworker_namespace.js',
      'lib/global/index.js',
      'lib/global/service_worker_global_scope.js',
      'lib/global/worker_global_scope.js',
      'lib/global/utils.js',
      'lib/idna.js',
      'lib/loader/esm.js',
      'lib/loader/fork.js',
      'lib/loader/mksnapshot.js',
      'lib/loader/script.js',
      'lib/url/url.js',
      'lib/js.js',
      'lib/kv_storage.js',
      'lib/navigator.js',
      'lib/path.js',
      'lib/performance/observer.js',
      'lib/performance/performance_entry.js',
      'lib/performance/performance.js',
      'lib/performance/user_timing.js',
      'lib/performance/resource_timing.js',
      'lib/performance/utils.js',
      'lib/process/execution.js',
      'lib/process/methods.js',
      'lib/service_worker/baggages.js',
      'lib/service_worker/event.js',
      'lib/service_worker/index.js',
      'lib/signals.js',
      'lib/source_maps/prepare_stack_trace_plain.js',
      'lib/source_maps/prepare_stack_trace.js',
      'lib/source_maps/source_map_cache.js',
      'lib/source_maps/source_map.js',
      'lib/streams.js',
      'lib/task_queue.js',
      'lib/timer.js',
      'lib/types.js',
      'lib/url.js',
      'lib/utils.js',
      'lib/v8.js',
      'lib/zlib.js',
    ],
    'aworker_cctest_source_files': [
      'test/cctest/ipc/stress_test_noslated_service.cc',
      'test/cctest/ipc/test_noslated_service.cc',
      'test/cctest/ipc/test_noslated_socket.cc',
      'test/cctest/proto/test.pb.cc',
      'test/cctest/utils/resizable_buffer.cc',
      'test/cctest/utils/result.cc',
      'test/cctest/alarm_timer.cc',
      'test/cctest/commandline_parser_group.cc',
      'test/cctest/macro_task_queue.cc',
      'test/cctest/aworker_platform.cc',
      'test/cctest/aworker.cc',
      'test/cctest/test_env.cc',
      'test/cctest/zero_copy_file_stream.cc',
    ],

    'conditions': [
      ['GENERATOR == "ninja"', {
        'aworker_obj_dir': '<(PRODUCT_DIR)/obj/aworker',
      }, {
        'aworker_obj_dir': '<(PRODUCT_DIR)/obj.target',
      }],
      ['OS=="mac"', {
        'aworker_obj_dir': '<(PRODUCT_DIR)',
        'aworker_source_files': [
          'src/libc_override_darwin.cc',
        ],
      }],
      ['OS=="linux"', {
        'aworker_source_files': [
          'src/libc_override.cc',
        ],
      }],
    ],
  },
}
