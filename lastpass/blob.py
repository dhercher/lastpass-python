# coding: utf-8
class Blob(object):
    def __init__(self, bytes, key_iteration_count):
        self.bytes = bytes
        self.key_iteration_count = key_iteration_count

    def encryption_key(self, username, password):
        from . import fetcher
        return fetcher.make_key(username, password, self.key_iteration_count)

    def __eq__(self, other):
        return self.bytes == other.bytes and self.key_iteration_count == other.key_iteration_count

    def store_local_blob(self, blob_filename):
        if blob_filename is None:
            return self
        f = open(blob_filename, 'w')
        f.write(str(self.key_iteration_count)+'\n')
        f.write(self.bytes)
        f.close()
        return self


class LocalBlob(Blob):
    def __init__(self, blob_filename):
        self.load_local_blob(blob_filename)

    def load_local_blob(self, blob_filename):
        f = open(blob_filename, 'r')
        self.key_iteration_count = int(f.readline().strip())
        self.bytes = f.read()
