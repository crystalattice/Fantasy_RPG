from dataclasses import dataclass


@dataclass()
class Mount:
    """Basic information for character mounts, war dogs, etc."""
    def __init__(self, mount_name="", mount_type="", mount_hp=0, mount_armour="", mount_ac=0,):
        self._mount_name: str = mount_name
        self._mount_type: str = mount_type
        self._mount_hp: int = mount_hp  # Hit points of mount
        self._mount_armour: str = mount_armour
        self._mount_ac: int = mount_ac  # Armour class of mount


# assert c.mount_name == ''
# assert c.mount_type == ''
# assert c.mount_hp == 0
# assert c.mount_armour == ''
# assert c.mount_ac == 0