import yaml
from checkout import checkout_negative
from test_sshcheckers import ssh_checkout_negative

with open("config.yaml") as f:
    data = yaml.safe.load(f)

def test_step0():
    res = []
    upload_files(data["host"], data['user'], "12", "{}/p7zip-full.deb".format(data["local_path"]),
                 "{}/p7zip-full.deb".format(data["remote_path"]))
    res.append(ssh_checkout_negative(data["host"], data['user'], "12", "echo '12' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout_negative(data["host"], data['user'], "12", "echo '12' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res)

def test_step1():
    # test1
    assert ssh_checkout_negative(data["host"], data['user'], "12", "cd {}; 7z e badarx.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert ssh_checkout_negative(data["host"], data['user'], "12", "cd {}; 7z t badarx.7z".format(data["folder_out"], "ERROR"), "Test5 Fail")
