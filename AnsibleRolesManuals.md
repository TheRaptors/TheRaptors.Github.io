# Ansible Roles Manuals

* **1. 收集OS日志**
    * 角色名：one_click_collect
    * 主机组：all
    * 常用：⭐
    * 调用方式：待完善

* **2. 更新OS安全配置**
    * 角色名：update_sys_safe_config
    * 主机组：all
    * 常用：⭐
    * 调用方式：待完善

* **3.更新OS环境**
    * 角色名：update_sys_env
    * 主机组：all
    * 常用：⭐⭐⭐⭐⭐
    * 调用方式：待完善

* **4.更新hosts配置，限制SSH源IP**
    * 角色名：update_hosts
    * 主机组：all
    * 常用：⭐⭐⭐⭐⭐
    * 调用方式：待完善

* **5.硬件监控**
    * 角色名：monitor_hardware
    * 主机组：all
    * 常用：⭐⭐⭐⭐
    * 调用方式：待完善

* **6.游戏进程监控**
    * 角色名：monitor_zone_svr
    * 主机组：world_group
    * 常用：⭐⭐⭐⭐
    * 依赖：monitor_hardware
    * 调用方式：待完善
    
* **7.游戏进程开机启动**
    * 角色名：boot_startup_zone_svr
    * 主机组：world_group,world_group_test
    * 常用：⭐⭐⭐⭐
    * 调用方式：待完善

* **8.关闭日志服&删除日志服数据库/表(已合服)**
    * 角色名：close_log_server
    * 主机组：log_group
    * 常用：⭐⭐⭐⭐
    * 调用方式：ansible-playbook -i hosts_temp ./playbooks/close_log_server.yaml --limit log_group_SvrID --list-hosts --list-tags
    * Tips：务必注意，合服后会注释log_group_SvrID，需创建临时inventory文件hosts_temp，格式如下：
      >[log_group]</br>
      log_group_SvrID1 ansible_ssh_host=IP</br>
      log_group_SvrID2 ansible_ssh_host=IP</br>

* **9.更新tbus配置**
    * 角色名：update_tbus_conf
    * 主机组：world_group_test
    * 常用：⭐⭐⭐⭐
    * 调用方式：ansible-playbook ./playbooks/update_tbus_conf.yaml --limit world_group_SvrID --list-hosts --list-tags

* **xxx**
    * 角色名：
    * 常用：
    *

* **xxx**
    * 角色名：
    * 常用：
    *

* **xxx**
    * 角色名：
    * 常用：
    *

* **xxx**
    * 角色名：
    * 常用：
    *