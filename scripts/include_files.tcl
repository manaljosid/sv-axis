set sv_axis_library_dir [file dirname [file normalize [info script]]]
set sv_axis_library_dir ${sv_axis_library_dir}/..

add_files $sv_axis_library_dir/lib/verilog-axis/rtl
add_files $sv_axis_library_dir/syn