require 'minitest'
require 'minitest/autorun'
require 'minitest/reporters'
require "minitest/skip_dsl"

Minitest::Reporters.use! Minitest::Reporters::SpecReporter.new

require_relative '../lib/min_heap'
require_relative '../lib/heap_sort'
