import yaml
from checkout import checkout_positive
from test_sshcheckers import ssh_checkout, upload_files

with open("config.yaml") as f:
    data = yaml.safe.load(f)


def test_step0():
    res = []
    upload_files(data["host"], data['user'], "12", "{}/p7zip-full.deb".format(data["local_path"]),
                 "{}/p7zip-full.deb".format(data["remote_path"]))
    res.append(ssh_checkout(data["host"], data['user'], "12", "echo '12' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout(data["host"], data['user'], "12", "echo '12' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res)


def test_step1(make_folders, clear_folders, make_files):
    # test1
    res1 = ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"
    res2 = ssh_checkout(data["host"], data['user'], "12", "ls {}".format(folder_out), "arx.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z e arx1.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data['user'], "12", "ls {}".format(folder_ext), ""))
    assert all(res)


def test_step3():
    # test3
    assert ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z t {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z u {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data['user'], "12", "cd {}; 7z l arx1.7z".format(folder_out), item))
    assert all(res)


# def test_step6():


def test_step7():
    assert ssh_checkout(data["host"], data['user'], "12", "7z d {}/arx1.7z".format(folder_out), "Everything is Ok"), "Test1 Fail"
