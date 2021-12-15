# The Brain Imaging Data Structure

[tooltips]{Hello!}

[tooltips]{If files belonging to an entity-linked file collection are acquired at different echo times, the `_echo-<index>` key/value pair MUST be used to distinguish individual files. This entity represents the `EchoTime` metadata field. Please note that the `<index>` denotes the number/index (in the form of a nonnegative integer), not the `EchoTime` value which needs to be stored in the field `EchoTime` of the separate JSON file.}

{{MACROS___make_tooltip("tooltips", "echo", "entities")}}

This resource defines the Brain Imaging Data Structure (BIDS) specification, including the core specification as well as many modality-specific extensions.

To get started, [check out the introduction](01-introduction.md). If you'd like
more information on how to adapt your own datasets to match the BIDS
specification, we recommend exploring the [BIDS Starter Kit](https://bids-standard.github.io/bids-starter-kit/)

For an overview of the BIDS ecosystem, visit the [BIDS homepage](https://bids.neuroimaging.io).  The entire specification can also be [downloaded as PDF](https://doi.org/10.5281/zenodo.3686061).
