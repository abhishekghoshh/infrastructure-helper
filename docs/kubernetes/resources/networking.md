

## Kubernetes Networking: eBPF in Action

### What is eBPF?
eBPF stands for extended Berkeley Packet Filter. It's a way to run small programs inside the Linux kernel — the core of your operating system. Back in the 1990s, BPF was just for filtering network packets. Now, eBPF does way more, like watching system activity or changing how traffic moves, all without messing up your system.

Think of it as a helper built into Linux. You write a program, load it into the kernel, and it runs when something specific happens — like a network packet arriving. The kernel makes sure your code is safe so it won't crash anything. It's a powerful way to control what's going on under the hood.


### Medium

- [Kubernetes Networking: eBPF in Action](https://medium.com/@hmquan08011996/kubernetes-networking-ebpf-in-action-f0df2592dade)