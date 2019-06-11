#!/usr//bin/python

from bcc import BPF

program  = """
    int hello(void *ctx) {
        bpf_trace_printk("Greetings!\\n");
        return 0;
    }
"""

b = BPF(text=program)
b.attach_kprobe(event="__x64_sys_clone", fn_name="hello")
b.trace_print()
