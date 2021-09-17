nan = None;  NAN = None
nan = 0
reports = []
class ValErr:
    def __init__(self, value, error, antisym):
        self.value, self.error, self.antisym = value, error, antisym

    def __repr__(self):
        if self.antisym == 0.:
            return "%g +- %g" % (self.value, self.error)
        else:
            return "%g +- %g ~ %g" % (self.value, self.error, self.antisym)

class Report:
    def __init__(self, chamberId, postal_address, name):
        self.chamberId, self.postal_address, self.name = chamberId, postal_address, name
        self.status = "NOFIT"
        self.fittype = None
        self.CovMatrix = None

    def add_parameters(self, deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz, loglikelihood, numsegments, sumofweights, redchi2):
        self.status = "PASS"
        self.deltax, self.deltay, self.deltaz, self.deltaphix, self.deltaphiy, self.deltaphiz = deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz
        self.loglikelihood, self.numsegments, self.sumofweights, self.redchi2 = loglikelihood, numsegments, sumofweights, redchi2

    def add_stats(self, median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz):
        self.median_x, self.median_y, self.median_dxdz, self.median_dydz, self.mean30_x, self.mean30_y, self.mean20_dxdz, self.mean50_dydz, self.mean15_x, self.mean15_y, self.mean10_dxdz, self.mean25_dydz, self.wmean30_x, self.wmean30_y, self.wmean20_dxdz, self.wmean50_dydz, self.wmean15_x, self.wmean15_y, self.wmean10_dxdz, self.wmean25_dydz, self.stdev30_x, self.stdev30_y, self.stdev20_dxdz, self.stdev50_dydz, self.stdev15_x, self.stdev15_y, self.stdev10_dxdz, self.stdev25_dydz = median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz

    def __repr__(self):
        return "<Report %s %s %s>" % (self.postal_address[0], " ".join(map(str, self.postal_address[1:])), self.status)

reports.append(Report(574914560, ("DT", -2, 1, 1), "MBwhAst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017672, ("CSC", 1, 1, 1, 1), "MEp11_01"))
reports[-1].posNum = 819
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0361703, 0.00644702, 0), \
                           ValErr(-0.218671, 0.157326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.33269e-05, 0.000169328, 0), \
                           239.008, 819, 819, -nan)
reports[-1].sigmaresid = ValErr(0.180728, 0.0044655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0425848, None, 0.000516866, None, 0.0357239, None, 0.000415575, None, 0.0357239, None, 0.000415575, None, 0.0378898, None, 0.000568736, None, 0.0378898, None, 0.000568736, None, 0.180948, None, 0.00716801, None, 0.180948, None, 0.00716801, None)
reports[-1].CovMatrix = ['4.15641e-05','-1.18223e-05','-2.19617e-07','5.83211e-09','0','0','0','0','0','-1.18223e-05','0.0247515','2.11968e-06','1.92869e-07','0','0','0','0','0','-2.19617e-07','2.11968e-06','2.86718e-08','2.0937e-10','0','0','0','0','0','5.83211e-09','1.92869e-07','2.0937e-10','1.99408e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 96222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0455549, 0.000558286, 0), \
                           ValErr(0.013238, 0.0139545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.803e-05, 1.51695e-05, 0), \
                           33235.9, 96222, 96222, -nan)
reports[-1].sigmaresid = ValErr(0.171299, 0.000390482, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0464634, None, -0.000679842, None, -0.0459823, None, -0.000659492, None, -0.0459823, None, -0.000659492, None, -0.0446984, None, -0.000689191, None, -0.0446984, None, -0.000689191, None, 0.171323, None, 0.0039478, None, 0.171323, None, 0.0039478, None)
reports[-1].CovMatrix = ['3.11684e-07','5.26808e-08','-1.24117e-09','5.43436e-11','0','0','0','0','0','5.26808e-08','0.000194727','5.73568e-09','1.6113e-09','0','0','0','0','0','-1.24117e-09','5.73568e-09','2.30115e-10','1.51473e-12','0','0','0','0','0','5.43436e-11','1.6113e-09','1.51473e-12','1.52476e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 90830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0329953, 0.000591293, 0), \
                           ValErr(-0.0362334, 0.0141544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62184e-05, 1.57387e-05, 0), \
                           31124.8, 90830, 90830, -nan)
reports[-1].sigmaresid = ValErr(0.171768, 0.000403008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0329383, None, 0.000322541, None, -0.0333158, None, 0.000283408, None, -0.0333158, None, 0.000283408, None, -0.0319679, None, 0.000290681, None, -0.0319679, None, 0.000290681, None, 0.171777, None, 0.00382281, None, 0.171777, None, 0.00382281, None)
reports[-1].CovMatrix = ['3.49627e-07','-3.97718e-07','-2.44858e-09','4.86707e-11','0','0','0','0','0','-3.97718e-07','0.000200348','5.37932e-09','1.58775e-09','0','0','0','0','0','-2.44858e-09','5.37932e-09','2.47707e-10','1.42625e-12','0','0','0','0','0','4.86707e-11','1.58775e-09','1.42625e-12','1.62415e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 90944
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00996257, 0.000588046, 0), \
                           ValErr(-0.0672951, 0.0149166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132063, 1.63997e-05, 0), \
                           28836.6, 90944, 90944, -nan)
reports[-1].sigmaresid = ValErr(0.17622, 0.000413194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0101488, None, -4.85375e-05, None, -0.0101237, None, -5.57612e-05, None, -0.0101237, None, -5.57612e-05, None, -0.00971367, None, -6.71984e-05, None, -0.00971367, None, -6.71984e-05, None, 0.176296, None, 0.00387217, None, 0.176296, None, 0.00387217, None)
reports[-1].CovMatrix = ['3.45798e-07','6.73221e-07','-7.01011e-10','6.72072e-11','0','0','0','0','0','6.73221e-07','0.000222504','2.68095e-08','2.0266e-09','0','0','0','0','0','-7.01011e-10','2.68095e-08','2.6895e-10','1.94946e-12','0','0','0','0','0','6.72072e-11','2.0266e-09','1.94946e-12','1.70729e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 100628
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0157354, 0.000550775, 0), \
                           ValErr(-0.0531781, 0.0138058, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.42538e-05, 1.47868e-05, 0), \
                           33823.3, 100628, 100628, -nan)
reports[-1].sigmaresid = ValErr(0.172897, 0.0003854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0151206, None, -0.000525, None, 0.0155423, None, -0.000516841, None, 0.0155423, None, -0.000516841, None, 0.0149919, None, -0.000526152, None, 0.0149919, None, -0.000526152, None, 0.172914, None, 0.00389809, None, 0.172914, None, 0.00389809, None)
reports[-1].CovMatrix = ['3.03353e-07','-3.63136e-08','-1.17176e-09','5.17126e-11','0','0','0','0','0','-3.63136e-08','0.000190599','4.02505e-10','1.5023e-09','0','0','0','0','0','-1.17176e-09','4.02505e-10','2.1865e-10','1.40404e-12','0','0','0','0','0','5.17126e-11','1.5023e-09','1.40404e-12','1.48534e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 92746
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0425137, 0.00056843, 0), \
                           ValErr(-0.0160189, 0.0141523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.66305e-05, 1.54485e-05, 0), \
                           32008.5, 92746, 92746, -nan)
reports[-1].sigmaresid = ValErr(0.171348, 0.000397848, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0432796, None, -4.7935e-05, None, 0.0428587, None, -7.41173e-05, None, 0.0428587, None, -7.41173e-05, None, 0.0418911, None, -3.20322e-05, None, 0.0418911, None, -3.20322e-05, None, 0.171367, None, 0.00385407, None, 0.171367, None, 0.00385407, None)
reports[-1].CovMatrix = ['3.23113e-07','-5.09176e-08','-1.249e-09','5.57252e-11','0','0','0','0','0','-5.09176e-08','0.000200288','8.85129e-10','1.61098e-09','0','0','0','0','0','-1.249e-09','8.85129e-10','2.38658e-10','1.53518e-12','0','0','0','0','0','5.57252e-11','1.61098e-09','1.53518e-12','1.58283e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 89766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0535856, 0.000577311, 0), \
                           ValErr(-0.0481075, 0.0147306, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.3132e-05, 1.55602e-05, 0), \
                           31022.7, 89766, 89766, -nan)
reports[-1].sigmaresid = ValErr(0.171266, 0.000404203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0532363, None, -0.000524579, None, 0.0531404, None, -0.00050803, None, 0.0531404, None, -0.00050803, None, 0.0538339, None, -0.00050244, None, 0.0538339, None, -0.00050244, None, 0.171297, None, 0.00383572, None, 0.171297, None, 0.00383572, None)
reports[-1].CovMatrix = ['3.33288e-07','-4.52095e-07','-1.17454e-09','5.50278e-11','0','0','0','0','0','-4.52095e-07','0.00021699','5.86374e-09','1.68364e-09','0','0','0','0','0','-1.17454e-09','5.86374e-09','2.42121e-10','1.60625e-12','0','0','0','0','0','5.50278e-11','1.68364e-09','1.60625e-12','1.6338e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 92347
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0704762, 0.000566186, 0), \
                           ValErr(-0.00229509, 0.0141096, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.95503e-05, 1.52884e-05, 0), \
                           33003.3, 92347, 92347, -nan)
reports[-1].sigmaresid = ValErr(0.169259, 0.000393843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0693646, None, 2.2251e-05, None, 0.0699486, None, 2.2387e-05, None, 0.0699486, None, 2.2387e-05, None, 0.0691214, None, -1.00521e-05, None, 0.0691214, None, -1.00521e-05, None, 0.169284, None, 0.00394868, None, 0.169284, None, 0.00394868, None)
reports[-1].CovMatrix = ['3.20566e-07','-1.35538e-07','-1.54914e-09','5.24454e-11','0','0','0','0','0','-1.35538e-07','0.000199081','2.49784e-09','1.61132e-09','0','0','0','0','0','-1.54914e-09','2.49784e-09','2.33734e-10','1.45599e-12','0','0','0','0','0','5.24454e-11','1.61132e-09','1.45599e-12','1.55112e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 83579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0781769, 0.00064928, 0), \
                           ValErr(0.0270079, 0.0155166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41142e-05, 2.02989e-05, 0), \
                           22728.6, 83579, 83579, -nan)
reports[-1].sigmaresid = ValErr(0.184357, 0.000452745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0777914, None, -0.000252199, None, 0.0780781, None, -0.000233111, None, 0.0780781, None, -0.000233111, None, 0.0784465, None, -0.000188272, None, 0.0784465, None, -0.000188272, None, 0.184362, None, 0.00390598, None, 0.184362, None, 0.00390598, None)
reports[-1].CovMatrix = ['4.21565e-07','-1.45803e-07','1.8642e-09','3.05796e-09','0','0','0','0','0','-1.45803e-07','0.000240764','-1.39912e-08','1.5299e-08','0','0','0','0','0','1.8642e-09','-1.39912e-08','4.12045e-10','-1.86317e-11','0','0','0','0','0','3.05796e-09','1.5299e-08','-1.86317e-11','2.04978e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 92960
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0754933, 0.000574112, 0), \
                           ValErr(-0.0122541, 0.014784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.01118e-05, 1.53503e-05, 0), \
                           33310.8, 92960, 92960, -nan)
reports[-1].sigmaresid = ValErr(0.169099, 0.000392649, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0753512, None, 0.000241829, None, 0.0750318, None, 0.000220579, None, 0.0750318, None, 0.000220579, None, 0.0740941, None, 0.000225002, None, 0.0740941, None, 0.000225002, None, 0.169109, None, 0.00369189, None, 0.169109, None, 0.00369189, None)
reports[-1].CovMatrix = ['3.29604e-07','-1.94333e-07','-2.16386e-09','2.23671e-10','0','0','0','0','0','-1.94333e-07','0.000218566','7.74042e-10','5.26561e-09','0','0','0','0','0','-2.16386e-09','7.74042e-10','2.35631e-10','-2.09142e-11','0','0','0','0','0','2.23671e-10','5.26561e-09','-2.09142e-11','1.54174e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 101212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0610249, 0.000544944, 0), \
                           ValErr(-0.0135073, 0.0136491, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.20327e-07, 1.45063e-05, 0), \
                           35238.4, 101212, 101212, -nan)
reports[-1].sigmaresid = ValErr(0.170827, 0.000379687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0609249, None, -0.00100743, None, 0.0610304, None, -0.000951307, None, 0.0610304, None, -0.000951307, None, 0.0608241, None, -0.0010207, None, 0.0608241, None, -0.0010207, None, 0.170828, None, 0.00401742, None, 0.170828, None, 0.00401742, None)
reports[-1].CovMatrix = ['2.96964e-07','4.80424e-09','-1.3483e-09','5.01605e-11','0','0','0','0','0','4.80424e-09','0.000186297','1.03533e-09','1.4883e-09','0','0','0','0','0','-1.3483e-09','1.03533e-09','2.10432e-10','1.3447e-12','0','0','0','0','0','5.01605e-11','1.4883e-09','1.3447e-12','1.44162e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 97333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0485637, 0.000558536, 0), \
                           ValErr(0.0290684, 0.0141309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.57319e-05, 1.46806e-05, 0), \
                           34444.2, 97333, 97333, -nan)
reports[-1].sigmaresid = ValErr(0.169854, 0.000384972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0481241, None, 0.00104239, None, 0.0483918, None, 0.000995571, None, 0.0483918, None, 0.000995571, None, 0.048941, None, 0.00101477, None, 0.048941, None, 0.00101477, None, 0.169858, None, 0.00379155, None, 0.169858, None, 0.00379155, None)
reports[-1].CovMatrix = ['3.11963e-07','2.87931e-07','-1.80844e-09','5.20186e-11','0','0','0','0','0','2.87931e-07','0.000199682','-1.46431e-09','1.62667e-09','0','0','0','0','0','-1.80844e-09','-1.46431e-09','2.15519e-10','1.2955e-12','0','0','0','0','0','5.20186e-11','1.62667e-09','1.2955e-12','1.48204e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 108500
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0264371, 0.000530201, 0), \
                           ValErr(-0.0038528, 0.0132545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.06727e-06, 1.40657e-05, 0), \
                           37375.7, 108500, 108500, -nan)
reports[-1].sigmaresid = ValErr(0.171458, 0.000368069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0258751, None, 0.000857248, None, 0.0264143, None, 0.00083342, None, 0.0264143, None, 0.00083342, None, 0.0260233, None, 0.000852883, None, 0.0260233, None, 0.000852883, None, 0.171459, None, 0.00376285, None, 0.171459, None, 0.00376285, None)
reports[-1].CovMatrix = ['2.81113e-07','-2.50402e-08','-1.41786e-09','4.67953e-11','0','0','0','0','0','-2.50402e-08','0.000175682','2.39811e-10','1.39454e-09','0','0','0','0','0','-1.41786e-09','2.39811e-10','1.97843e-10','1.1901e-12','0','0','0','0','0','4.67953e-11','1.39454e-09','1.1901e-12','1.35474e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 101629
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0039326, 0.00054541, 0), \
                           ValErr(0.0392346, 0.0136549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.64126e-05, 1.4336e-05, 0), \
                           36186.1, 101629, 101629, -nan)
reports[-1].sigmaresid = ValErr(0.169484, 0.000375927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.003017, None, 0.000185354, None, 0.00329754, None, 0.00018308, None, 0.00329754, None, 0.00018308, None, 0.00431179, None, 0.000165232, None, 0.00431179, None, 0.000165232, None, 0.169514, None, 0.0037423, None, 0.169514, None, 0.0037423, None)
reports[-1].CovMatrix = ['2.97472e-07','-7.06209e-08','-1.74446e-09','4.71139e-11','0','0','0','0','0','-7.06209e-08','0.000186456','7.45039e-10','1.47762e-09','0','0','0','0','0','-1.74446e-09','7.45039e-10','2.05522e-10','1.26666e-12','0','0','0','0','0','4.71139e-11','1.47762e-09','1.26666e-12','1.41321e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 87265
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00547617, 0.000601724, 0), \
                           ValErr(0.0242253, 0.0143688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.47896e-05, 1.70484e-05, 0), \
                           27049.4, 87265, 87265, -nan)
reports[-1].sigmaresid = ValErr(0.177478, 0.000424824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00547393, None, 0.00352311, None, -0.00550324, None, 0.00335639, None, -0.00550324, None, 0.00335639, None, -0.00436504, None, 0.00347923, None, -0.00436504, None, 0.00347923, None, 0.177483, None, 0.00395819, None, 0.177483, None, 0.00395819, None)
reports[-1].CovMatrix = ['3.62072e-07','4.26234e-07','2.70512e-10','7.4568e-11','0','0','0','0','0','4.26234e-07','0.000206463','3.01857e-09','1.71991e-09','0','0','0','0','0','2.70512e-10','3.01857e-09','2.90649e-10','2.02217e-12','0','0','0','0','0','7.4568e-11','1.71991e-09','2.02217e-12','1.80475e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 100762
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0277836, 0.000546646, 0), \
                           ValErr(0.0470332, 0.0136644, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00013401, 1.45756e-05, 0), \
                           35556.9, 100762, 100762, -nan)
reports[-1].sigmaresid = ValErr(0.170023, 0.000378744, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0295528, None, 0.000115603, None, -0.0288015, None, 0.000147937, None, -0.0288015, None, 0.000147937, None, -0.0287686, None, 8.50939e-05, None, -0.0287686, None, 8.50939e-05, None, 0.170106, None, 0.00390826, None, 0.170106, None, 0.00390826, None)
reports[-1].CovMatrix = ['2.98822e-07','3.1976e-08','-1.59076e-09','4.91399e-11','0','0','0','0','0','3.1976e-08','0.000186717','3.16251e-09','1.5414e-09','0','0','0','0','0','-1.59076e-09','3.16251e-09','2.12448e-10','1.30823e-12','0','0','0','0','0','4.91399e-11','1.5414e-09','1.30823e-12','1.43447e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 103126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0553065, 0.000542023, 0), \
                           ValErr(0.0511412, 0.0136077, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.46419e-05, 1.43475e-05, 0), \
                           36659, 103126, 103126, -nan)
reports[-1].sigmaresid = ValErr(0.169582, 0.000373406, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0556404, None, 0.000281271, None, -0.055855, None, 0.000314221, None, -0.055855, None, 0.000314221, None, -0.0539432, None, 0.000250431, None, -0.0539432, None, 0.000250431, None, 0.169611, None, 0.00380073, None, 0.169611, None, 0.00380073, None)
reports[-1].CovMatrix = ['2.93789e-07','-1.05454e-08','-1.75277e-09','4.67443e-11','0','0','0','0','0','-1.05454e-08','0.000185171','4.45622e-10','1.4693e-09','0','0','0','0','0','-1.75277e-09','4.45622e-10','2.05849e-10','1.23693e-12','0','0','0','0','0','4.67443e-11','1.4693e-09','1.23693e-12','1.39432e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 106994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0488785, 0.000475824, 0), \
                           ValErr(0.0170899, 0.0119034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.30775e-05, 1.26285e-05, 0), \
                           48824.4, 106994, 106994, -nan)
reports[-1].sigmaresid = ValErr(0.153314, 0.000331427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0495632, None, -0.00300478, None, -0.0492926, None, -0.00283219, None, -0.0492926, None, -0.00283219, None, -0.0499226, None, -0.00295385, None, -0.0499226, None, -0.00295385, None, 0.153333, None, 0.00399662, None, 0.153333, None, 0.00399662, None)
reports[-1].CovMatrix = ['2.26408e-07','4.85064e-08','-1.03412e-09','4.34946e-11','0','0','0','0','0','4.85064e-08','0.000141691','-4.13677e-10','1.29857e-09','0','0','0','0','0','-1.03412e-09','-4.13677e-10','1.59479e-10','1.16242e-12','0','0','0','0','0','4.34946e-11','1.29857e-09','1.16242e-12','1.09844e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 103466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.037263, 0.000486055, 0), \
                           ValErr(-0.0337542, 0.012161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.67516e-05, 1.28666e-05, 0), \
                           46590.2, 103466, 103466, -nan)
reports[-1].sigmaresid = ValErr(0.154242, 0.000338763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0375162, None, 0.00121699, None, -0.0374265, None, 0.00116758, None, -0.0374265, None, 0.00116758, None, -0.0382831, None, 0.00115681, None, -0.0382831, None, 0.00115681, None, 0.154251, None, 0.00392998, None, 0.154251, None, 0.00392998, None)
reports[-1].CovMatrix = ['2.3625e-07','1.32826e-08','-1.03076e-09','2.60812e-10','0','0','0','0','0','1.32826e-08','0.000147889','2.83556e-10','-3.1189e-10','0','0','0','0','0','-1.03076e-09','2.83556e-10','1.65549e-10','-5.17403e-12','0','0','0','0','0','2.60812e-10','-3.1189e-10','-5.17403e-12','1.14761e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 95793
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.019174, 0.000504192, 0), \
                           ValErr(-0.0282483, 0.0121724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.09309e-05, 1.31196e-05, 0), \
                           44079.1, 95793, 95793, -nan)
reports[-1].sigmaresid = ValErr(0.152729, 0.000354727, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0199573, None, -0.00346882, None, -0.0197381, None, -0.00330703, None, -0.0197381, None, -0.00330703, None, -0.0203598, None, -0.00349062, None, -0.0203598, None, -0.00349062, None, 0.152765, None, 0.00395668, None, 0.152765, None, 0.00395668, None)
reports[-1].CovMatrix = ['2.54209e-07','2.29595e-07','-1.28125e-09','1.21764e-09','0','0','0','0','0','2.29595e-07','0.000148167','-2.96431e-09','3.74728e-08','0','0','0','0','0','-1.28125e-09','-2.96431e-09','1.72123e-10','-8.10968e-11','0','0','0','0','0','1.21764e-09','3.74728e-08','-8.10968e-11','1.25831e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 102363
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00536482, 0.000489163, 0), \
                           ValErr(-0.0786147, 0.0122296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.9406e-05, 1.29665e-05, 0), \
                           46117, 102363, 102363, -nan)
reports[-1].sigmaresid = ValErr(0.154206, 0.000340812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524291, None, -7.25839e-06, None, 0.00549067, None, -3.25848e-05, None, 0.00549067, None, -3.25848e-05, None, 0.00561017, None, -7.57841e-05, None, 0.00561017, None, -7.57841e-05, None, 0.154239, None, 0.00401179, None, 0.154239, None, 0.00401179, None)
reports[-1].CovMatrix = ['2.3928e-07','-1.14102e-09','-1.08279e-09','4.57588e-11','0','0','0','0','0','-1.14102e-09','0.000149562','3.94534e-10','1.37065e-09','0','0','0','0','0','-1.08279e-09','3.94534e-10','1.6813e-10','1.21867e-12','0','0','0','0','0','4.57588e-11','1.37065e-09','1.21867e-12','1.16153e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 101743
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0257593, 0.000494199, 0), \
                           ValErr(-0.0608461, 0.0123485, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.77452e-05, 1.30652e-05, 0), \
                           44673.9, 101743, 101743, -nan)
reports[-1].sigmaresid = ValErr(0.155981, 0.000345819, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0261251, None, -0.00045114, None, 0.0255368, None, -0.000417735, None, 0.0255368, None, -0.000417735, None, 0.0257502, None, -0.000449458, None, 0.0257502, None, -0.000449458, None, 0.156006, None, 0.00395027, None, 0.156006, None, 0.00395027, None)
reports[-1].CovMatrix = ['2.44233e-07','-2.96401e-08','-9.48233e-10','-9.94782e-11','0','0','0','0','0','-2.96401e-08','0.000152484','-8.22876e-10','2.46311e-10','0','0','0','0','0','-9.48233e-10','-8.22876e-10','1.70701e-10','1.30753e-12','0','0','0','0','0','-9.94782e-11','2.46311e-10','1.30753e-12','1.19591e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 98266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0462683, 0.000494161, 0), \
                           ValErr(-0.0249386, 0.0123872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.3306e-05, 1.31785e-05, 0), \
                           45309.4, 98266, 98266, -nan)
reports[-1].sigmaresid = ValErr(0.152586, 0.000344189, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0455501, None, -0.000229677, None, 0.0461808, None, -0.000271398, None, 0.0461808, None, -0.000271398, None, 0.0464872, None, -0.000372773, None, 0.0464872, None, -0.000372773, None, 0.15259, None, 0.00398462, None, 0.15259, None, 0.00398462, None)
reports[-1].CovMatrix = ['2.44195e-07','-1.14454e-08','-1.12295e-09','4.61985e-11','0','0','0','0','0','-1.14454e-08','0.000153444','-2.6439e-10','1.41081e-09','0','0','0','0','0','-1.12295e-09','-2.6439e-10','1.73673e-10','1.26975e-12','0','0','0','0','0','4.61985e-11','1.41081e-09','1.26975e-12','1.18466e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 98756
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0580945, 0.000493547, 0), \
                           ValErr(-0.00555177, 0.0125408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.27796e-05, 1.31116e-05, 0), \
                           45458.4, 98756, 98756, -nan)
reports[-1].sigmaresid = ValErr(0.152705, 0.000343603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0586001, None, 6.43537e-05, None, 0.0583783, None, 8.67538e-05, None, 0.0583783, None, 8.67538e-05, None, 0.0590036, None, 6.69215e-05, None, 0.0590036, None, 6.69215e-05, None, 0.152713, None, 0.00387079, None, 0.152713, None, 0.00387079, None)
reports[-1].CovMatrix = ['2.43589e-07','1.6214e-07','-1.12174e-09','4.90753e-11','0','0','0','0','0','1.6214e-07','0.000157272','-1.74755e-09','1.46657e-09','0','0','0','0','0','-1.12174e-09','-1.74755e-09','1.71914e-10','1.23066e-12','0','0','0','0','0','4.90753e-11','1.46657e-09','1.23066e-12','1.18063e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 96896
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0676637, 0.000502725, 0), \
                           ValErr(0.0152815, 0.0126572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2709e-05, 1.34843e-05, 0), \
                           43794.8, 96896, 96896, -nan)
reports[-1].sigmaresid = ValErr(0.153983, 0.000349787, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0668109, None, 0.000209669, None, 0.067508, None, 0.000206697, None, 0.067508, None, 0.000206697, None, 0.0682108, None, 0.000215365, None, 0.0682108, None, 0.000215365, None, 0.153986, None, 0.00387841, None, 0.153986, None, 0.00387841, None)
reports[-1].CovMatrix = ['2.52732e-07','9.01193e-08','-1.20661e-09','4.79377e-11','0','0','0','0','0','9.01193e-08','0.000160205','-4.33226e-09','1.43064e-09','0','0','0','0','0','-1.20661e-09','-4.33226e-09','1.81827e-10','1.25062e-12','0','0','0','0','0','4.79377e-11','1.43064e-09','1.25062e-12','1.22351e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 103052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0742121, 0.00048236, 0), \
                           ValErr(0.0176577, 0.0120631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.24955e-05, 1.28306e-05, 0), \
                           47642.4, 103052, 103052, -nan)
reports[-1].sigmaresid = ValErr(0.152399, 0.000335691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0735746, None, 0.000578316, None, 0.0740606, None, 0.000572161, None, 0.0740606, None, 0.000572161, None, 0.0737993, None, 0.000566574, None, 0.0737993, None, 0.000566574, None, 0.152403, None, 0.0039078, None, 0.152403, None, 0.0039078, None)
reports[-1].CovMatrix = ['2.32671e-07','2.29948e-08','-1.09576e-09','4.51978e-11','0','0','0','0','0','2.29948e-08','0.000145517','-1.25697e-09','1.33832e-09','0','0','0','0','0','-1.09576e-09','-1.25697e-09','1.64626e-10','1.18451e-12','0','0','0','0','0','4.51978e-11','1.33832e-09','1.18451e-12','1.12688e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 93455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0676456, 0.000518149, 0), \
                           ValErr(-0.0242874, 0.0133312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000115733, 1.42799e-05, 0), \
                           40351.3, 93455, 93455, -nan)
reports[-1].sigmaresid = ValErr(0.157125, 0.000363437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0680826, None, 0.00215812, None, 0.0680276, None, 0.0020676, None, 0.0680276, None, 0.0020676, None, 0.0669471, None, 0.00209299, None, 0.0669471, None, 0.00209299, None, 0.157181, None, 0.0038044, None, 0.157181, None, 0.0038044, None)
reports[-1].CovMatrix = ['2.68479e-07','-4.55792e-07','-7.26077e-10','5.05896e-11','0','0','0','0','0','-4.55792e-07','0.00017772','-2.58233e-08','1.24283e-09','0','0','0','0','0','-7.26077e-10','-2.58233e-08','2.03916e-10','1.30371e-12','0','0','0','0','0','5.05896e-11','1.24283e-09','1.30371e-12','1.32087e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 104442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0572704, 0.000481913, 0), \
                           ValErr(0.0222705, 0.0120798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.59785e-05, 1.27299e-05, 0), \
                           47868.9, 104442, 104442, -nan)
reports[-1].sigmaresid = ValErr(0.153007, 0.000334779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.057301, None, -0.00515119, None, 0.0573852, None, -0.00491701, None, 0.0573852, None, -0.00491701, None, 0.0578857, None, -0.00506027, None, 0.0578857, None, -0.00506027, None, 0.153011, None, 0.00399552, None, 0.153011, None, 0.00399552, None)
reports[-1].CovMatrix = ['2.32241e-07','-5.77738e-09','-1.14457e-09','4.43426e-11','0','0','0','0','0','-5.77738e-09','0.000145922','-1.05644e-09','1.33508e-09','0','0','0','0','0','-1.14457e-09','-1.05644e-09','1.6205e-10','1.13577e-12','0','0','0','0','0','4.43426e-11','1.33508e-09','1.13577e-12','1.12077e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 104190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.043161, 0.000483692, 0), \
                           ValErr(0.0310029, 0.0121259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.14349e-05, 1.25662e-05, 0), \
                           48139.3, 104190, 104190, -nan)
reports[-1].sigmaresid = ValErr(0.152442, 0.000333303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.042273, None, 0.000886382, None, 0.0429002, None, 0.00090978, None, 0.0429002, None, 0.00090978, None, 0.0430576, None, 0.000947295, None, 0.0430576, None, 0.000947295, None, 0.152451, None, 0.00384126, None, 0.152451, None, 0.00384126, None)
reports[-1].CovMatrix = ['2.33958e-07','-3.02496e-09','-1.31925e-09','-3.34459e-10','0','0','0','0','0','-3.02496e-09','0.000147036','1.96628e-10','-5.45182e-11','0','0','0','0','0','-1.31925e-09','1.96628e-10','1.57909e-10','6.49317e-12','0','0','0','0','0','-3.34459e-10','-5.45182e-11','6.49317e-12','1.11091e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 109373
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0184101, 0.000472983, 0), \
                           ValErr(0.034265, 0.0118585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.17566e-05, 1.25065e-05, 0), \
                           50355.1, 109373, 109373, -nan)
reports[-1].sigmaresid = ValErr(0.152691, 0.000330605, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0176949, None, 1.57063e-05, None, 0.0179272, None, 1.85372e-05, None, 0.0179272, None, 1.85372e-05, None, 0.018327, None, -1.11369e-05, None, 0.018327, None, -1.11369e-05, None, 0.152714, None, 0.00390692, None, 0.152714, None, 0.00390692, None)
reports[-1].CovMatrix = ['2.23713e-07','-9.08428e-09','-1.22402e-09','-9.91101e-10','0','0','0','0','0','-9.08428e-09','0.000140624','-2.13414e-10','2.15652e-09','0','0','0','0','0','-1.22402e-09','-2.13414e-10','1.56412e-10','6.69966e-11','0','0','0','0','0','-9.91101e-10','2.15652e-09','6.69966e-11','1.093e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 103782
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000359889, 0.000490455, 0), \
                           ValErr(-0.00245429, 0.0172456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.99378e-05, 1.2859e-05, 0), \
                           47173.8, 103782, 103782, -nan)
reports[-1].sigmaresid = ValErr(0.153587, 0.00033745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156465, None, 0.000130903, None, -0.000648683, None, 0.000148063, None, -0.000648683, None, 0.000148063, None, -0.000853632, None, 0.000150409, None, -0.000853632, None, 0.000150409, None, 0.153595, None, 0.003906, None, 0.153595, None, 0.003906, None)
reports[-1].CovMatrix = ['2.40546e-07','-8.44801e-07','-1.23146e-09','1.03257e-09','0','0','0','0','0','-8.44801e-07','0.000297412','5.44911e-09','-1.83895e-07','0','0','0','0','0','-1.23146e-09','5.44911e-09','1.65355e-10','-9.26018e-12','0','0','0','0','0','1.03257e-09','-1.83895e-07','-9.26018e-12','1.13872e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 106318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0199239, 0.000477886, 0), \
                           ValErr(0.0412244, 0.0119297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.8154e-05, 1.26232e-05, 0), \
                           49382.8, 106318, 106318, -nan)
reports[-1].sigmaresid = ValErr(0.152069, 0.000337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0212224, None, 0.000698465, None, -0.0205368, None, 0.000658208, None, -0.0205368, None, 0.000658208, None, -0.01934, None, 0.00061501, None, -0.01934, None, 0.00061501, None, 0.152105, None, 0.00388983, None, 0.152105, None, 0.00388983, None)
reports[-1].CovMatrix = ['2.28375e-07','1.69811e-09','-1.24997e-09','1.95413e-09','0','0','0','0','0','1.69811e-09','0.000142318','2.98391e-10','-2.81961e-08','0','0','0','0','0','-1.24997e-09','2.98391e-10','1.59345e-10','-8.89037e-11','0','0','0','0','0','1.95413e-09','-2.81961e-08','-8.89037e-11','1.13569e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 62958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.039959, 0.000633341, 0), \
                           ValErr(0.0498581, 0.0153409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.28791e-05, 1.43509e-05, 0), \
                           26571.4, 62958, 62958, -nan)
reports[-1].sigmaresid = ValErr(0.15866, 0.000447123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0401716, None, -0.000387002, None, -0.0398018, None, -0.00042797, None, -0.0398018, None, -0.00042797, None, -0.0404773, None, -0.000432515, None, -0.0404773, None, -0.000432515, None, 0.158686, None, 0.00404746, None, 0.158686, None, 0.00404746, None)
reports[-1].CovMatrix = ['4.01121e-07','-3.0162e-07','4.18937e-10','9.0266e-11','0','0','0','0','0','-3.0162e-07','0.000235344','7.90828e-09','2.16992e-09','0','0','0','0','0','4.18937e-10','7.90828e-09','2.05948e-10','2.17061e-12','0','0','0','0','0','9.0266e-11','2.16992e-09','2.17061e-12','1.99919e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 106547
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0465212, 0.000474014, 0), \
                           ValErr(-0.0133279, 0.0118824, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.43802e-05, 1.25364e-05, 0), \
                           49762.1, 106547, 106547, -nan)
reports[-1].sigmaresid = ValErr(0.15168, 0.000328581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0469662, None, 0.000220381, None, -0.0468513, None, 0.000230521, None, -0.0468513, None, 0.000230521, None, -0.0482336, None, 0.000215845, None, -0.0482336, None, 0.000215845, None, 0.15169, None, 0.0038438, None, 0.15169, None, 0.0038438, None)
reports[-1].CovMatrix = ['2.2469e-07','1.00667e-08','-1.17321e-09','4.19252e-11','0','0','0','0','0','1.00667e-08','0.000141192','-3.86994e-10','1.30107e-09','0','0','0','0','0','-1.17321e-09','-3.86994e-10','1.5716e-10','1.11996e-12','0','0','0','0','0','4.19252e-11','1.30107e-09','1.11996e-12','1.07966e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 103952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0530765, 0.000490761, 0), \
                           ValErr(-0.0242005, 0.0153009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.33598e-05, 1.29547e-05, 0), \
                           48971, 103952, 103952, -nan)
reports[-1].sigmaresid = ValErr(0.151067, 0.000331966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0540859, None, -0.000646556, None, -0.0535034, None, -0.000572976, None, -0.0535034, None, -0.000572976, None, -0.05345, None, -0.000594921, None, -0.05345, None, -0.000594921, None, 0.151083, None, 0.00388412, None, 0.151083, None, 0.00388412, None)
reports[-1].CovMatrix = ['2.40847e-07','9.78299e-07','-1.56244e-09','-1.76855e-09','0','0','0','0','0','9.78299e-07','0.000234116','-2.8501e-08','-1.5912e-07','0','0','0','0','0','-1.56244e-09','-2.8501e-08','1.67825e-10','4.65711e-11','0','0','0','0','0','-1.76855e-09','-1.5912e-07','4.65711e-11','1.10202e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 38509
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0391368, 0.00285455, 0), \
                           ValErr(0.0556164, 0.0683498, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000187961, 5.49558e-05, 0), \
                           -26519, 38509, 38509, -nan)
reports[-1].sigmaresid = ValErr(0.481767, 0.00173596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0420939, None, 0.00072157, None, -0.0422268, None, 0.000691813, None, -0.0422268, None, 0.000691813, None, -0.0440527, None, 0.000730788, None, -0.0440527, None, 0.000730788, None, 0.481845, None, 0.00507052, None, 0.481845, None, 0.00507052, None)
reports[-1].CovMatrix = ['8.14848e-06','-6.39374e-05','-6.30563e-08','7.4405e-10','0','0','0','0','0','-6.39374e-05','0.00467169','1.27171e-07','3.47704e-08','0','0','0','0','0','-6.30563e-08','1.27171e-07','3.02014e-09','2.5818e-11','0','0','0','0','0','7.4405e-10','3.47704e-08','2.5818e-11','3.01357e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 49584
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0348813, 0.00248835, 0), \
                           ValErr(-0.134074, 0.0555421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.22102e-05, 5.09624e-05, 0), \
                           -31515.8, 49584, 49584, -nan)
reports[-1].sigmaresid = ValErr(0.45688, 0.00145083, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0375306, None, 6.6667e-05, None, -0.0346818, None, 8.73485e-05, None, -0.0346818, None, 8.73485e-05, None, -0.0345727, None, 9.30145e-05, None, -0.0345727, None, 9.30145e-05, None, 0.456908, None, 0.00451154, None, 0.456908, None, 0.00451154, None)
reports[-1].CovMatrix = ['6.19189e-06','-8.05022e-06','-7.169e-08','6.58496e-10','0','0','0','0','0','-8.05022e-06','0.00308492','1.78115e-07','3.16166e-08','0','0','0','0','0','-7.169e-08','1.78115e-07','2.59716e-09','1.6967e-11','0','0','0','0','0','6.58496e-10','3.16166e-08','1.6967e-11','2.10491e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 42977
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0238913, 0.00284879, 0), \
                           ValErr(0.0172706, 0.0602883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.19234e-05, 5.72427e-05, 0), \
                           -26896.6, 42977, 42977, -nan)
reports[-1].sigmaresid = ValErr(0.45244, 0.00154322, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0186934, None, 9.94934e-05, None, -0.0228788, None, 8.96197e-05, None, -0.0228788, None, 8.96197e-05, None, -0.0206468, None, 0.000109917, None, -0.0206468, None, 0.000109917, None, 0.452442, None, 0.00433802, None, 0.452442, None, 0.00433802, None)
reports[-1].CovMatrix = ['8.11562e-06','7.89572e-06','-1.048e-07','8.68546e-10','0','0','0','0','0','7.89572e-06','0.00363468','-1.95711e-07','3.55609e-08','0','0','0','0','0','-1.048e-07','-1.95711e-07','3.27672e-09','1.39882e-11','0','0','0','0','0','8.68546e-10','3.55609e-08','1.39882e-11','2.38153e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 53605
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0136011, 0.00230696, 0), \
                           ValErr(-0.136409, 0.0547222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000103136, 4.70381e-05, 0), \
                           -36748.3, 53605, 53605, -nan)
reports[-1].sigmaresid = ValErr(0.480274, 0.00146681, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0080869, None, 0.000129213, None, -0.0114805, None, 0.00015703, None, -0.0114805, None, 0.00015703, None, -0.0107932, None, 0.000114828, None, -0.0107932, None, 0.000114828, None, 0.480323, None, 0.00451242, None, 0.480323, None, 0.00451242, None)
reports[-1].CovMatrix = ['5.32207e-06','-2.59131e-06','-4.74543e-08','8.24494e-10','0','0','0','0','0','-2.59131e-06','0.00299452','2.96215e-08','3.21978e-08','0','0','0','0','0','-4.74543e-08','2.96215e-08','2.21258e-09','1.85431e-11','0','0','0','0','0','8.24494e-10','3.21978e-08','1.85431e-11','2.15152e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 47730
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0113004, 0.00257343, 0), \
                           ValErr(0.0608209, 0.057564, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000126601, 5.14319e-05, 0), \
                           -31508.5, 47730, 47730, -nan)
reports[-1].sigmaresid = ValErr(0.468229, 0.00151547, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0134523, None, -0.00089219, None, 0.0147505, None, -0.000832138, None, 0.0147505, None, -0.000832138, None, 0.0144337, None, -0.000905354, None, 0.0144337, None, -0.000905354, None, 0.468266, None, 0.00466781, None, 0.468266, None, 0.00466781, None)
reports[-1].CovMatrix = ['6.62253e-06','7.44474e-06','-7.32246e-08','8.96498e-10','0','0','0','0','0','7.44474e-06','0.00331362','-1.70354e-07','3.42793e-08','0','0','0','0','0','-7.32246e-08','-1.70354e-07','2.64524e-09','1.43032e-11','0','0','0','0','0','8.96498e-10','3.42793e-08','1.43032e-11','2.29664e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 48199
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0308608, 0.00251659, 0), \
                           ValErr(0.00942042, 0.0568608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.80233e-06, 5.07405e-05, 0), \
                           -32026.5, 48199, 48199, -nan)
reports[-1].sigmaresid = ValErr(0.470257, 0.00151461, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0332188, None, -0.000923676, None, 0.0306894, None, -0.00087932, None, 0.0306894, None, -0.00087932, None, 0.030025, None, -0.000901841, None, 0.030025, None, -0.000901841, None, 0.470258, None, 0.00441498, None, 0.470258, None, 0.00441498, None)
reports[-1].CovMatrix = ['6.33323e-06','-2.32763e-06','-6.701e-08','8.08039e-10','0','0','0','0','0','-2.32763e-06','0.00323315','1.91134e-08','3.39215e-08','0','0','0','0','0','-6.701e-08','1.91134e-08','2.5746e-09','1.77551e-11','0','0','0','0','0','8.08039e-10','3.39215e-08','1.77551e-11','2.29405e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 45568
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0620848, 0.00249313, 0), \
                           ValErr(-0.30513, 0.0662916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.90551e-05, 5.0593e-05, 0), \
                           -30158.8, 45568, 45568, -nan)
reports[-1].sigmaresid = ValErr(0.469026, 0.00155364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0588315, None, -0.00110249, None, 0.0586274, None, -0.00104718, None, 0.0586274, None, -0.00104718, None, 0.0529537, None, -0.00106414, None, 0.0529537, None, -0.00106414, None, 0.469145, None, 0.00442048, None, 0.469145, None, 0.00442048, None)
reports[-1].CovMatrix = ['6.21572e-06','-2.74362e-05','-5.5612e-08','7.20319e-10','0','0','0','0','0','-2.74362e-05','0.00439458','-3.11186e-08','3.36502e-08','0','0','0','0','0','-5.5612e-08','-3.11186e-08','2.55965e-09','1.90944e-11','0','0','0','0','0','7.20319e-10','3.36502e-08','1.90944e-11','2.41381e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 56204
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0693977, 0.00218063, 0), \
                           ValErr(0.181014, 0.0531185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000111515, 4.49087e-05, 0), \
                           -38336.1, 56204, 56204, -nan)
reports[-1].sigmaresid = ValErr(0.478619, 0.00142755, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0665811, None, -0.00175036, None, 0.0674657, None, -0.00165403, None, 0.0674657, None, -0.00165403, None, 0.0683487, None, -0.00175759, None, 0.0683487, None, -0.00175759, None, 0.478695, None, 0.00453136, None, 0.478695, None, 0.00453136, None)
reports[-1].CovMatrix = ['4.75517e-06','-1.99503e-06','-3.69855e-08','8.22867e-10','0','0','0','0','0','-1.99503e-06','0.00282158','1.31182e-08','3.03437e-08','0','0','0','0','0','-3.69855e-08','1.31182e-08','2.01679e-09','1.74513e-11','0','0','0','0','0','8.22867e-10','3.03437e-08','1.74513e-11','2.0379e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 50452
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0973501, 0.00234773, 0), \
                           ValErr(0.11513, 0.0552107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000137243, 4.76523e-05, 0), \
                           -32699.8, 50452, 50452, -nan)
reports[-1].sigmaresid = ValErr(0.462641, 0.00145643, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0946886, None, -0.000187422, None, 0.094135, None, -0.00015006, None, 0.094135, None, -0.00015006, None, 0.0945606, None, -0.000201418, None, 0.0945606, None, -0.000201418, None, 0.4627, None, 0.00465309, None, 0.4627, None, 0.00465309, None)
reports[-1].CovMatrix = ['5.51184e-06','-4.60049e-07','-5.36854e-08','7.88948e-10','0','0','0','0','0','-4.60049e-07','0.00304822','-1.39812e-08','3.14801e-08','0','0','0','0','0','-5.36854e-08','-1.39812e-08','2.27074e-09','1.61295e-11','0','0','0','0','0','7.88948e-10','3.14801e-08','1.61295e-11','2.12119e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 58738
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0830778, 0.00216227, 0), \
                           ValErr(0.227477, 0.0533499, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.50349e-05, 4.42883e-05, 0), \
                           -41157.8, 58738, 58738, -nan)
reports[-1].sigmaresid = ValErr(0.487611, 0.00142265, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0839549, None, -0.000523766, None, 0.0851311, None, -0.000496744, None, 0.0851311, None, -0.000496744, None, 0.0850066, None, -0.000498885, None, 0.0850066, None, -0.000498885, None, 0.4877, None, 0.00449464, None, 0.4877, None, 0.00449464, None)
reports[-1].CovMatrix = ['4.6754e-06','-8.34901e-06','-3.45954e-08','7.73465e-10','0','0','0','0','0','-8.34901e-06','0.00284621','7.53721e-08','2.99237e-08','0','0','0','0','0','-3.45954e-08','7.53721e-08','1.96145e-09','1.83813e-11','0','0','0','0','0','7.73465e-10','2.99237e-08','1.83813e-11','2.02394e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 27500
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0513879, 0.00321181, 0), \
                           ValErr(-0.00104484, 0.074296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.36153e-05, 6.38435e-05, 0), \
                           -18197.3, 27500, 27500, -nan)
reports[-1].sigmaresid = ValErr(0.468969, 0.00199969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0538438, None, 9.47679e-05, None, 0.0521431, None, 0.000159433, None, 0.0521431, None, 0.000159433, None, 0.0544938, None, 0.000155451, None, 0.0544938, None, 0.000155451, None, 0.468971, None, 0.00474331, None, 0.468971, None, 0.00474331, None)
reports[-1].CovMatrix = ['1.03157e-05','4.09368e-05','-9.09916e-08','2.06895e-09','0','0','0','0','0','4.09368e-05','0.00551989','-5.12298e-08','7.06845e-08','0','0','0','0','0','-9.09916e-08','-5.12298e-08','4.076e-09','3.0659e-11','0','0','0','0','0','2.06895e-09','7.06845e-08','3.0659e-11','3.99875e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 52485
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0258635, 0.00231516, 0), \
                           ValErr(0.0572775, 0.0545107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000305721, 4.65454e-05, 0), \
                           -35396.4, 52485, 52485, -nan)
reports[-1].sigmaresid = ValErr(0.474958, 0.00146596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0364838, None, -0.00030578, None, 0.0326481, None, -0.000305551, None, 0.0326481, None, -0.000305551, None, 0.0329201, None, -0.000308328, None, 0.0329201, None, -0.000308328, None, 0.475158, None, 0.00448205, None, 0.475158, None, 0.00448205, None)
reports[-1].CovMatrix = ['5.35998e-06','-7.21149e-07','-4.79587e-08','8.35165e-10','0','0','0','0','0','-7.21149e-07','0.00297141','-6.42814e-09','3.17363e-08','0','0','0','0','0','-4.79587e-08','-6.42814e-09','2.16648e-09','1.68757e-11','0','0','0','0','0','8.35165e-10','3.17363e-08','1.68757e-11','2.14904e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 50839
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.024534, 0.00243437, 0), \
                           ValErr(0.0205205, 0.0559253, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.25904e-05, 4.94304e-05, 0), \
                           -33610.6, 50839, 50839, -nan)
reports[-1].sigmaresid = ValErr(0.468686, 0.00146983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0249654, None, -0.000213314, None, 0.0266346, None, -0.000147369, None, 0.0266346, None, -0.000147369, None, 0.0283063, None, -0.000231369, None, 0.0283063, None, -0.000231369, None, 0.468701, None, 0.00469071, None, 0.468701, None, 0.00469071, None)
reports[-1].CovMatrix = ['5.92614e-06','4.54594e-06','-6.26001e-08','8.43618e-10','0','0','0','0','0','4.54594e-06','0.00312764','-9.40409e-08','3.26416e-08','0','0','0','0','0','-6.26001e-08','-9.40409e-08','2.44336e-09','1.50245e-11','0','0','0','0','0','8.43618e-10','3.26416e-08','1.50245e-11','2.16041e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 43950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00217293, 0.00261269, 0), \
                           ValErr(0.00225751, 0.0607061, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.18187e-05, 5.04869e-05, 0), \
                           -29267.2, 43950, 43950, -nan)
reports[-1].sigmaresid = ValErr(0.470943, 0.00158845, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00415472, None, 0.000259039, None, 0.00401756, None, 0.000240925, None, 0.00401756, None, 0.000240925, None, 0.00219419, None, 0.000251027, None, 0.00219419, None, 0.000251027, None, 0.470954, None, 0.0044495, None, 0.470954, None, 0.0044495, None)
reports[-1].CovMatrix = ['6.82612e-06','1.96384e-05','-6.66793e-08','1.15329e-09','0','0','0','0','0','1.96384e-05','0.00368523','-3.16159e-07','3.95803e-08','0','0','0','0','0','-6.66793e-08','-3.16159e-07','2.54892e-09','1.48968e-11','0','0','0','0','0','1.15329e-09','3.95803e-08','1.48968e-11','2.52319e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 53066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.013258, 0.00231583, 0), \
                           ValErr(0.144756, 0.0556021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.17756e-05, 4.74105e-05, 0), \
                           -36116.9, 53066, 53066, -nan)
reports[-1].sigmaresid = ValErr(0.477909, 0.00146697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118093, None, -5.24052e-05, None, -0.0120545, None, 4.33306e-06, None, -0.0120545, None, 4.33306e-06, None, -0.0137035, None, -8.94738e-06, None, -0.0137035, None, -8.94738e-06, None, 0.477942, None, 0.0046695, None, 0.477942, None, 0.0046695, None)
reports[-1].CovMatrix = ['5.36306e-06','-1.17148e-05','-4.84596e-08','7.2693e-10','0','0','0','0','0','-1.17148e-05','0.00309159','2.36255e-07','3.28417e-08','0','0','0','0','0','-4.84596e-08','2.36255e-07','2.24776e-09','2.01389e-11','0','0','0','0','0','7.2693e-10','3.28417e-08','2.01389e-11','2.15201e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 42703
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00552565, 0.00259522, 0), \
                           ValErr(-0.0201507, 0.0679364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.19762e-05, 5.09983e-05, 0), \
                           -27969.4, 42703, 42703, -nan)
reports[-1].sigmaresid = ValErr(0.465817, 0.00159394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000819526, None, -0.00034573, None, -0.00395721, None, -0.000320846, None, -0.00395721, None, -0.000320846, None, -0.00729951, None, -0.000319047, None, -0.00729951, None, -0.000319047, None, 0.465828, None, 0.00449184, None, 0.465828, None, 0.00449184, None)
reports[-1].CovMatrix = ['6.73518e-06','-3.05217e-05','-6.15179e-08','7.30661e-10','0','0','0','0','0','-3.05217e-05','0.00461535','9.72187e-09','3.53034e-08','0','0','0','0','0','-6.15179e-08','9.72187e-09','2.60083e-09','1.93289e-11','0','0','0','0','0','7.30661e-10','3.53034e-08','1.93289e-11','2.54064e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 55840
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0235474, 0.0022209, 0), \
                           ValErr(0.0902089, 0.054027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.40393e-05, 4.51977e-05, 0), \
                           -38528.6, 55840, 55840, -nan)
reports[-1].sigmaresid = ValErr(0.482411, 0.00144354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0237411, None, -0.000298534, None, -0.0238997, None, -0.000275311, None, -0.0238997, None, -0.000275311, None, -0.024511, None, -0.000311206, None, -0.024511, None, -0.000311206, None, 0.482425, None, 0.00447814, None, 0.482425, None, 0.00447814, None)
reports[-1].CovMatrix = ['4.93239e-06','-4.07541e-06','-3.94099e-08','8.14456e-10','0','0','0','0','0','-4.07541e-06','0.00291892','2.40695e-08','3.08763e-08','0','0','0','0','0','-3.94099e-08','2.40695e-08','2.04283e-09','1.79756e-11','0','0','0','0','0','8.14456e-10','3.08763e-08','1.79756e-11','2.0838e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 40390
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0260933, 0.00275114, 0), \
                           ValErr(-0.0846583, 0.0597582, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000200429, 5.2077e-05, 0), \
                           -24554, 40390, 40390, -nan)
reports[-1].sigmaresid = ValErr(0.444406, 0.00156361, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0368829, None, -0.00083158, None, -0.0324991, None, -0.000790673, None, -0.0324991, None, -0.000790673, None, -0.0350562, None, -0.000814927, None, -0.0350562, None, -0.000814927, None, 0.444497, None, 0.00446124, None, 0.444497, None, 0.00446124, None)
reports[-1].CovMatrix = ['7.56875e-06','-7.51059e-06','-8.51175e-08','7.52752e-10','0','0','0','0','0','-7.51059e-06','0.00357105','7.37608e-08','3.46073e-08','0','0','0','0','0','-8.51175e-08','7.37608e-08','2.71202e-09','1.63142e-11','0','0','0','0','0','7.52752e-10','3.46073e-08','1.63142e-11','2.44487e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 45036
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0404804, 0.00246593, 0), \
                           ValErr(0.0478209, 0.056071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.51034e-05, 4.85905e-05, 0), \
                           -27666, 45036, 45036, -nan)
reports[-1].sigmaresid = ValErr(0.447253, 0.00149025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0398137, None, 0.000782409, None, -0.0419465, None, 0.000762201, None, -0.0419465, None, 0.000762201, None, -0.04168, None, 0.00081341, None, -0.04168, None, 0.00081341, None, 0.447263, None, 0.00445196, None, 0.447263, None, 0.00445196, None)
reports[-1].CovMatrix = ['6.08079e-06','-3.22054e-07','-6.22042e-08','7.87861e-10','0','0','0','0','0','-3.22054e-07','0.00314396','4.73441e-08','3.25264e-08','0','0','0','0','0','-6.22042e-08','4.73441e-08','2.36104e-09','1.60508e-11','0','0','0','0','0','7.87861e-10','3.25264e-08','1.60508e-11','2.22084e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 37294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0303553, 0.0037427, 0), \
                           ValErr(0.0385853, 0.0593284, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000107318, 7.09364e-05, 0), \
                           -20057, 37294, 37294, -nan)
reports[-1].sigmaresid = ValErr(0.414315, 0.00151704, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0364816, None, -4.51709e-05, None, -0.0349739, None, -2.79995e-05, None, -0.0349739, None, -2.79995e-05, None, -0.0322791, None, -1.87478e-05, None, -0.0322791, None, -1.87478e-05, None, 0.41433, None, 0.00460746, None, 0.41433, None, 0.00460746, None)
reports[-1].CovMatrix = ['1.40078e-05','-6.43604e-06','-2.17535e-07','5.80059e-10','0','0','0','0','0','-6.43604e-06','0.00351986','1.08816e-07','3.20532e-08','0','0','0','0','0','-2.17535e-07','1.08816e-07','5.03197e-09','1.3017e-11','0','0','0','0','0','5.80059e-10','3.20532e-08','1.3017e-11','2.3014e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 49677
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.023609, 0.00232119, 0), \
                           ValErr(0.0149593, 0.0537553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.84872e-05, 4.75376e-05, 0), \
                           -30386.1, 49677, 49677, -nan)
reports[-1].sigmaresid = ValErr(0.446077, 0.0014152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0227588, None, 0.000291876, None, -0.0219631, None, 0.000282856, None, -0.0219631, None, 0.000282856, None, -0.0211031, None, 0.000308287, None, -0.0211031, None, 0.000308287, None, 0.446087, None, 0.00430875, None, 0.446087, None, 0.00430875, None)
reports[-1].CovMatrix = ['5.38793e-06','9.4755e-06','-5.56355e-08','8.17079e-10','0','0','0','0','0','9.4755e-06','0.00288964','-1.3965e-07','2.99365e-08','0','0','0','0','0','-5.56355e-08','-1.3965e-07','2.25982e-09','1.33368e-11','0','0','0','0','0','8.17079e-10','2.99365e-08','1.33368e-11','2.00278e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 49012
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00159112, 0.00229253, 0), \
                           ValErr(-0.155145, 0.0535656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000131832, 4.4801e-05, 0), \
                           -29410, 49012, 49012, -nan)
reports[-1].sigmaresid = ValErr(0.440925, 0.00140831, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00531776, None, -0.000183105, None, 0.00480277, None, -0.000189214, None, 0.00480277, None, -0.000189214, None, 0.00436748, None, -0.00017917, None, 0.00436748, None, -0.00017917, None, 0.441005, None, 0.00440552, None, 0.441005, None, 0.00440552, None)
reports[-1].CovMatrix = ['5.25571e-06','-4.63581e-06','-5.08299e-08','6.61921e-10','0','0','0','0','0','-4.63581e-06','0.00286927','9.39187e-08','2.85663e-08','0','0','0','0','0','-5.08299e-08','9.39187e-08','2.00713e-09','1.48087e-11','0','0','0','0','0','6.61921e-10','2.85663e-08','1.48087e-11','1.98334e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 51274
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0310225, 0.00232308, 0), \
                           ValErr(-0.0457927, 0.0543798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.17032e-05, 4.71362e-05, 0), \
                           -33334.9, 51274, 51274, -nan)
reports[-1].sigmaresid = ValErr(0.463566, 0.0014476, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0287793, None, 3.4582e-05, None, 0.0308245, None, 6.25869e-05, None, 0.0308245, None, 6.25869e-05, None, 0.0266148, None, 7.7973e-05, None, 0.0266148, None, 7.7973e-05, None, 0.46357, None, 0.00465887, None, 0.46357, None, 0.00465887, None)
reports[-1].CovMatrix = ['5.39671e-06','5.84184e-06','-5.15985e-08','8.46767e-10','0','0','0','0','0','5.84184e-06','0.00295717','-5.11462e-08','3.18922e-08','0','0','0','0','0','-5.15985e-08','-5.11462e-08','2.22182e-09','1.54852e-11','0','0','0','0','0','8.46767e-10','3.18922e-08','1.54852e-11','2.09553e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 48608
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0488888, 0.00226251, 0), \
                           ValErr(-0.172954, 0.0527626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.65974e-05, 4.49024e-05, 0), \
                           -28823, 48608, 48608, -nan)
reports[-1].sigmaresid = ValErr(0.43781, 0.00140416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0498945, None, -0.00024503, None, 0.0503642, None, -0.00023424, None, 0.0503642, None, -0.00023424, None, 0.0514603, None, -0.000260472, None, 0.0514603, None, -0.000260472, None, 0.437869, None, 0.00446945, None, 0.437869, None, 0.00446945, None)
reports[-1].CovMatrix = ['5.11893e-06','-2.59342e-06','-4.86523e-08','6.84297e-10','0','0','0','0','0','-2.59342e-06','0.00278389','1.99953e-08','2.75279e-08','0','0','0','0','0','-4.86523e-08','1.99953e-08','2.01622e-09','1.42081e-11','0','0','0','0','0','6.84297e-10','2.75279e-08','1.42081e-11','1.97166e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 57767
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.065788, 0.00207982, 0), \
                           ValErr(0.0490833, 0.0499919, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.34588e-05, 4.31936e-05, 0), \
                           -37483.7, 57767, 57767, -nan)
reports[-1].sigmaresid = ValErr(0.462985, 0.00136211, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0680345, None, -0.000149468, None, 0.0674793, None, -0.000126978, None, 0.0674793, None, -0.000126978, None, 0.0699188, None, -0.000138661, None, 0.0699188, None, -0.000138661, None, 0.463007, None, 0.00434916, None, 0.463007, None, 0.00434916, None)
reports[-1].CovMatrix = ['4.32565e-06','-2.55287e-07','-3.38715e-08','7.45915e-10','0','0','0','0','0','-2.55287e-07','0.00249919','2.97152e-08','2.71683e-08','0','0','0','0','0','-3.38715e-08','2.97152e-08','1.86569e-09','1.59455e-11','0','0','0','0','0','7.45915e-10','2.71683e-08','1.59455e-11','1.85534e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 51394
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.071734, 0.00220364, 0), \
                           ValErr(-0.0214562, 0.0520628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.54943e-05, 4.33349e-05, 0), \
                           -32373.2, 51394, 51394, -nan)
reports[-1].sigmaresid = ValErr(0.454282, 0.00141695, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0685227, None, -7.95156e-05, None, 0.069704, None, 5.81907e-06, None, 0.069704, None, 5.81907e-06, None, 0.0703824, None, 3.32663e-05, None, 0.0703824, None, 3.32663e-05, None, 0.454305, None, 0.00486864, None, 0.454305, None, 0.00486864, None)
reports[-1].CovMatrix = ['4.85603e-06','-1.75082e-06','-3.97119e-08','7.58404e-10','0','0','0','0','0','-1.75082e-06','0.00271054','1.51461e-08','2.83072e-08','0','0','0','0','0','-3.97119e-08','1.51461e-08','1.87792e-09','1.53179e-11','0','0','0','0','0','7.58404e-10','2.83072e-08','1.53179e-11','2.00775e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 50355
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0948893, 0.00223926, 0), \
                           ValErr(-0.0627102, 0.0534521, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000104446, 4.50146e-05, 0), \
                           -31927.8, 50355, 50355, -nan)
reports[-1].sigmaresid = ValErr(0.456172, 0.00143745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0920646, None, -0.000845829, None, 0.0928071, None, -0.000831507, None, 0.0928071, None, -0.000831507, None, 0.0932225, None, -0.000900926, None, 0.0932225, None, -0.000900926, None, 0.456204, None, 0.00461864, None, 0.456204, None, 0.00461864, None)
reports[-1].CovMatrix = ['5.01429e-06','5.23428e-06','-4.21427e-08','8.54263e-10','0','0','0','0','0','5.23428e-06','0.00285713','-6.47469e-08','3.01481e-08','0','0','0','0','0','-4.21427e-08','-6.47469e-08','2.02632e-09','1.55051e-11','0','0','0','0','0','8.54263e-10','3.01481e-08','1.55051e-11','2.06625e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 32871
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0635235, 0.00276597, 0), \
                           ValErr(-0.0314994, 0.0561835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.68698e-05, 5.27079e-05, 0), \
                           -20731, 32871, 32871, -nan)
reports[-1].sigmaresid = ValErr(0.454634, 0.00177313, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0639948, None, 0.000619315, None, 0.0639755, None, 0.000654224, None, 0.0639755, None, 0.000654224, None, 0.0644631, None, 0.000757993, None, 0.0644631, None, 0.000757993, None, 0.454637, None, 0.00492226, None, 0.454637, None, 0.00492226, None)
reports[-1].CovMatrix = ['7.65058e-06','9.48655e-06','-6.1041e-08','1.33237e-09','0','0','0','0','0','9.48655e-06','0.00315659','-5.7696e-08','4.0456e-08','0','0','0','0','0','-6.1041e-08','-5.7696e-08','2.77812e-09','2.24863e-11','0','0','0','0','0','1.33237e-09','4.0456e-08','2.24863e-11','3.14398e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 50894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0377969, 0.00228332, 0), \
                           ValErr(0.0658185, 0.0544004, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.99781e-05, 4.50949e-05, 0), \
                           -33164.2, 50894, 50894, -nan)
reports[-1].sigmaresid = ValErr(0.464261, 0.00145517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0395232, None, 8.38257e-05, None, 0.0390811, None, 9.1299e-05, None, 0.0390811, None, 9.1299e-05, None, 0.0379103, None, 0.000100986, None, 0.0379103, None, 0.000100986, None, 0.464277, None, 0.0044889, None, 0.464277, None, 0.0044889, None)
reports[-1].CovMatrix = ['5.21355e-06','1.23596e-06','-4.45919e-08','8.25209e-10','0','0','0','0','0','1.23596e-06','0.0029594','8.18383e-09','3.17701e-08','0','0','0','0','0','-4.45919e-08','8.18383e-09','2.03355e-09','1.67339e-11','0','0','0','0','0','8.25209e-10','3.17701e-08','1.67339e-11','2.11752e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 53238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.034125, 0.00219404, 0), \
                           ValErr(0.0597403, 0.0524392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00017944, 4.43432e-05, 0), \
                           -33535.2, 53238, 53238, -nan)
reports[-1].sigmaresid = ValErr(0.454286, 0.0013922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.039221, None, 0.000135672, None, 0.0380469, None, 0.000147119, None, 0.0380469, None, 0.000147119, None, 0.0366005, None, 0.000172664, None, 0.0366005, None, 0.000172664, None, 0.454361, None, 0.00442604, None, 0.454361, None, 0.00442604, None)
reports[-1].CovMatrix = ['4.81382e-06','-1.02835e-06','-4.29316e-08','7.20144e-10','0','0','0','0','0','-1.02835e-06','0.00274987','4.1633e-08','2.87864e-08','0','0','0','0','0','-4.29316e-08','4.1633e-08','1.96632e-09','1.49384e-11','0','0','0','0','0','7.20144e-10','2.87864e-08','1.49384e-11','1.93823e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 44755
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00857014, 0.00247012, 0), \
                           ValErr(-0.00998244, 0.0545908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.99128e-05, 4.70261e-05, 0), \
                           -25913, 44755, 44755, -nan)
reports[-1].sigmaresid = ValErr(0.431736, 0.00144306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00843637, None, -0.000102983, None, 0.0102909, None, -8.00878e-05, None, 0.0102909, None, -8.00878e-05, None, 0.00980353, None, -9.7396e-05, None, 0.00980353, None, -9.7396e-05, None, 0.431743, None, 0.00447828, None, 0.431743, None, 0.00447828, None)
reports[-1].CovMatrix = ['6.10151e-06','-1.27948e-05','-6.50011e-08','5.86634e-10','0','0','0','0','0','-1.27948e-05','0.00298016','1.35483e-07','2.84929e-08','0','0','0','0','0','-6.50011e-08','1.35483e-07','2.21145e-09','1.44178e-11','0','0','0','0','0','5.86634e-10','2.84929e-08','1.44178e-11','2.08241e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 56250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00325153, 0.00217593, 0), \
                           ValErr(0.116436, 0.0516797, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.56916e-05, 4.45592e-05, 0), \
                           -37369, 56250, 56250, -nan)
reports[-1].sigmaresid = ValErr(0.470198, 0.00140186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00327353, None, -0.000170871, None, -0.00238149, None, -0.000157281, None, -0.00238149, None, -0.000157281, None, -0.00299472, None, -0.000158673, None, -0.00299472, None, -0.000158673, None, 0.470224, None, 0.00472232, None, 0.470224, None, 0.00472232, None)
reports[-1].CovMatrix = ['4.73465e-06','2.03755e-06','-3.99485e-08','8.04883e-10','0','0','0','0','0','2.03755e-06','0.00267079','-4.56151e-08','2.87997e-08','0','0','0','0','0','-3.99485e-08','-4.56151e-08','1.98552e-09','1.55497e-11','0','0','0','0','0','8.04883e-10','2.87997e-08','1.55497e-11','1.96521e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 37242
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0276893, 0.00270278, 0), \
                           ValErr(-0.168696, 0.0583878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.23192e-06, 4.92398e-05, 0), \
                           -20860.5, 37242, 37242, -nan)
reports[-1].sigmaresid = ValErr(0.423668, 0.00155236, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.025982, None, -0.000285626, None, -0.027624, None, -0.000225161, None, -0.027624, None, -0.000225161, None, -0.0267397, None, -0.000242835, None, -0.0267397, None, -0.000242835, None, 0.423715, None, 0.00447361, None, 0.423715, None, 0.00447361, None)
reports[-1].CovMatrix = ['7.305e-06','4.47655e-06','-7.76055e-08','8.1863e-10','0','0','0','0','0','4.47655e-06','0.00340914','-7.35805e-08','3.2893e-08','0','0','0','0','0','-7.76055e-08','-7.35805e-08','2.42456e-09','1.40978e-11','0','0','0','0','0','8.1863e-10','3.2893e-08','1.40978e-11','2.40984e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 51487
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0291768, 0.00223631, 0), \
                           ValErr(0.0311355, 0.0535054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.39875e-05, 4.54639e-05, 0), \
                           -33295.3, 51487, 51487, -nan)
reports[-1].sigmaresid = ValErr(0.461965, 0.00143961, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0308919, None, -0.000494651, None, -0.0295127, None, -0.000441207, None, -0.0295127, None, -0.000441207, None, -0.0313845, None, -0.000475658, None, -0.0313845, None, -0.000475658, None, 0.461967, None, 0.00446025, None, 0.461967, None, 0.00446025, None)
reports[-1].CovMatrix = ['5.0011e-06','5.94802e-06','-4.18661e-08','8.83178e-10','0','0','0','0','0','5.94802e-06','0.00286282','-5.5356e-08','3.11824e-08','0','0','0','0','0','-4.18661e-08','-5.5356e-08','2.06696e-09','1.61786e-11','0','0','0','0','0','8.83178e-10','3.11824e-08','1.61786e-11','2.07248e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 46873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0317201, 0.00233574, 0), \
                           ValErr(0.0165327, 0.0560636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000158338, 4.48681e-05, 0), \
                           -29992, 46873, 46873, -nan)
reports[-1].sigmaresid = ValErr(0.458826, 0.00149855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0323243, None, 2.91932e-05, None, -0.0351886, None, 5.05704e-05, None, -0.0351886, None, 5.05704e-05, None, -0.0347715, None, 3.53043e-05, None, -0.0347715, None, 3.53043e-05, None, 0.458888, None, 0.00449053, None, 0.458888, None, 0.00449053, None)
reports[-1].CovMatrix = ['5.45567e-06','2.07311e-07','-4.406e-08','8.80481e-10','0','0','0','0','0','2.07311e-07','0.00314313','8.13765e-09','3.29995e-08','0','0','0','0','0','-4.406e-08','8.13765e-09','2.01314e-09','1.70955e-11','0','0','0','0','0','8.80481e-10','3.29995e-08','1.70955e-11','2.24565e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 44229
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.032872, 0.00243115, 0), \
                           ValErr(0.135359, 0.0575845, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.43647e-05, 4.68229e-05, 0), \
                           -28054.9, 44229, 44229, -nan)
reports[-1].sigmaresid = ValErr(0.456288, 0.00153416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0352113, None, -0.000717044, None, -0.0348905, None, -0.000706451, None, -0.0348905, None, -0.000706451, None, -0.0308886, None, -0.000779828, None, -0.0308886, None, -0.000779828, None, 0.456331, None, 0.00436685, None, 0.456331, None, 0.00436685, None)
reports[-1].CovMatrix = ['5.91051e-06','7.03088e-06','-5.10451e-08','9.79587e-10','0','0','0','0','0','7.03088e-06','0.00331597','-1.7033e-09','3.65766e-08','0','0','0','0','0','-5.10451e-08','-1.7033e-09','2.19239e-09','1.7619e-11','0','0','0','0','0','9.79587e-10','3.65766e-08','1.7619e-11','2.35364e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 10889
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000198495, 0.0122877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000470942, 0.000276515, 0), \
                           -18120.7, 10889, 10889, -nan)
reports[-1].sigmaresid = ValErr(1.27787, 0.00865918, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00547908, None, 0.000303321, None, 0.0019238, None, 0.000327982, None, 0.0019238, None, 0.000327982, None, -0.0071273, None, 0.0005934, None, -0.0071273, None, 0.0005934, None, 1.27804, None, 0.00739291, None, 1.27804, None, 0.00739291, None)
reports[-1].CovMatrix = ['0.000150989','2.80079e-07','7.26962e-08','0','0','0','0','0','0','2.80079e-07','7.64607e-08','1.63425e-09','0','0','0','0','0','0','7.26962e-08','1.63425e-09','7.49815e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 11825
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0363006, 0.0124426, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000176728, 0.000296162, 0), \
                           -20071.3, 11825, 11825, -nan)
reports[-1].sigmaresid = ValErr(1.32104, 0.00859011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0272599, None, 0.000380662, None, 0.0379061, None, 0.00040161, None, 0.0379061, None, 0.00040161, None, 0.0305898, None, 0.000485735, None, 0.0305898, None, 0.000485735, None, 1.32106, None, 0.00779101, None, 1.32106, None, 0.00779101, None)
reports[-1].CovMatrix = ['0.000154817','7.96692e-07','8.4723e-08','0','0','0','0','0','0','7.96692e-07','8.7712e-08','2.02841e-09','0','0','0','0','0','0','8.4723e-08','2.02841e-09','7.37901e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 11901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0131428, 0.0125395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000543867, 0.000299966, 0), \
                           -20164.5, 11901, 11901, -nan)
reports[-1].sigmaresid = ValErr(1.31708, 0.00853697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0118163, None, 0.001735, None, 0.0070008, None, 0.001625, None, 0.0070008, None, 0.001625, None, 0.00358519, None, 0.0017773, None, 0.00358519, None, 0.0017773, None, 1.31726, None, 0.00706009, None, 1.31726, None, 0.00706009, None)
reports[-1].CovMatrix = ['0.000157238','1.01628e-06','8.96171e-08','0','0','0','0','0','0','1.01628e-06','8.99798e-08','2.14763e-09','0','0','0','0','0','0','8.96171e-08','2.14763e-09','7.28799e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 5811
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00882751, 0.020306, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000329092, 0.0004751, 0), \
                           -10188.7, 5811, 5811, -nan)
reports[-1].sigmaresid = ValErr(1.3971, 0.0129595, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143864, None, 0.000398832, None, -0.00276785, None, 0.000468743, None, -0.00276785, None, 0.000468743, None, -0.00849328, None, 0.000429559, None, -0.00849328, None, 0.000429559, None, 1.39716, None, 0.00730361, None, 1.39716, None, 0.00730361, None)
reports[-1].CovMatrix = ['0.000412335','4.15374e-06','2.68315e-07','0','0','0','0','0','0','4.15374e-06','2.2572e-07','6.2941e-09','0','0','0','0','0','0','2.68315e-07','6.2941e-09','0.000167949','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 5657
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00373016, 0.0205758, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000318949, 0.000464911, 0), \
                           -9941.56, 5657, 5657, -nan)
reports[-1].sigmaresid = ValErr(1.40277, 0.013188, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00174051, None, 0.00175254, None, 0.00224093, None, 0.00176038, None, 0.00224093, None, 0.00176038, None, -0.0279465, None, 0.00198719, None, -0.0279465, None, 0.00198719, None, 1.40283, None, 0.00822749, None, 1.40283, None, 0.00822749, None)
reports[-1].CovMatrix = ['0.000423363','4.04005e-06','2.73051e-07','0','0','0','0','0','0','4.04005e-06','2.16142e-07','6.22667e-09','0','0','0','0','0','0','2.73051e-07','6.22667e-09','0.000173924','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 10250
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0629675, 0.0130725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000624278, 0.000300541, 0), \
                           -17198.7, 10250, 10250, -nan)
reports[-1].sigmaresid = ValErr(1.29561, 0.00904887, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0556061, None, 0.000683314, None, 0.0685113, None, 0.000686446, None, 0.0685113, None, 0.000686446, None, 0.0625015, None, 0.000737431, None, 0.0625015, None, 0.000737431, None, 1.29588, None, 0.00761861, None, 1.29588, None, 0.00761861, None)
reports[-1].CovMatrix = ['0.000170891','8.0224e-07','9.22474e-08','0','0','0','0','0','0','8.0224e-07','9.03251e-08','2.13327e-09','0','0','0','0','0','0','9.22474e-08','2.13327e-09','8.18822e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 17189
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0441082, 0.0097272, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000996183, 0.000226057, 0), \
                           -28561.9, 17189, 17189, -nan)
reports[-1].sigmaresid = ValErr(1.27469, 0.00687484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0388229, None, 0.00265746, None, 0.0427781, None, 0.00258884, None, 0.0427781, None, 0.00258884, None, 0.0509664, None, 0.00269878, None, 0.0509664, None, 0.00269878, None, 1.27541, None, 0.00747677, None, 1.27541, None, 0.00747677, None)
reports[-1].CovMatrix = ['9.46184e-05','6.8352e-08','4.32128e-08','0','0','0','0','0','0','6.8352e-08','5.11017e-08','1.01099e-09','0','0','0','0','0','0','4.32128e-08','1.01099e-09','4.72635e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 20069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0139507, 0.00884986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000187355, 0.000206702, 0), \
                           -32986.3, 20069, 20069, -nan)
reports[-1].sigmaresid = ValErr(1.25195, 0.00624897, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0057612, None, -0.00215074, None, 0.0143431, None, -0.00206201, None, 0.0143431, None, -0.00206201, None, 0.0160209, None, -0.00209861, None, 0.0160209, None, -0.00209861, None, 1.25198, None, 0.00715442, None, 1.25198, None, 0.00715442, None)
reports[-1].CovMatrix = ['7.832e-05','-9.69701e-08','3.48441e-08','0','0','0','0','0','0','-9.69701e-08','4.27259e-08','7.67973e-10','0','0','0','0','0','0','3.48441e-08','7.67973e-10','3.90497e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 17060
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.05266, 0.00981235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143471, 0.000222488, 0), \
                           -28406.5, 17060, 17060, -nan)
reports[-1].sigmaresid = ValErr(1.2791, 0.00692471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0599739, None, 0.00115241, None, 0.0530596, None, 0.00122654, None, 0.0530596, None, 0.00122654, None, 0.0481129, None, 0.00136432, None, 0.0481129, None, 0.00136432, None, 1.27912, None, 0.0076355, None, 1.27912, None, 0.0076355, None)
reports[-1].CovMatrix = ['9.62822e-05','-1.36993e-07','3.99876e-08','0','0','0','0','0','0','-1.36993e-07','4.95011e-08','9.08937e-10','0','0','0','0','0','0','3.99876e-08','9.08937e-10','4.79517e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 12263
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.028299, 0.0113951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000178425, 0.000239235, 0), \
                           -19783.7, 12263, 12263, -nan)
reports[-1].sigmaresid = ValErr(1.21451, 0.00775513, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0312855, None, -0.00246722, None, 0.0259928, None, -0.00225615, None, 0.0259928, None, -0.00225615, None, 0.00550354, None, -0.00219667, None, 0.00550354, None, -0.00219667, None, 1.21454, None, 0.00703101, None, 1.21454, None, 0.00703101, None)
reports[-1].CovMatrix = ['0.000129848','-7.39841e-07','4.14952e-08','0','0','0','0','0','0','-7.39841e-07','5.72334e-08','8.65157e-10','0','0','0','0','0','0','4.14952e-08','8.65157e-10','6.01421e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 4024
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0525788, 0.0195998, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.83781e-05, 0.000397186, 0), \
                           -6559.74, 4024, 4024, -nan)
reports[-1].sigmaresid = ValErr(1.23518, 0.0137685, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0613222, None, -0.00086669, None, 0.0529646, None, -0.000800461, None, 0.0529646, None, -0.000800461, None, 0.0384865, None, -0.000634301, None, 0.0384865, None, -0.000634301, None, 1.23518, None, 0.00680532, None, 1.23518, None, 0.00680532, None)
reports[-1].CovMatrix = ['0.000384154','-8.89179e-07','1.49837e-07','0','0','0','0','0','0','-8.89179e-07','1.57757e-07','3.02917e-09','0','0','0','0','0','0','1.49837e-07','3.02917e-09','0.000189571','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 6965
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0957717, 0.0151882, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000202123, 0.000331494, 0), \
                           -11477, 6965, 6965, -nan)
reports[-1].sigmaresid = ValErr(1.25719, 0.0106518, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0841298, None, -0.00207919, None, 0.096954, None, -0.00208121, None, 0.096954, None, -0.00208121, None, 0.063078, None, -0.00199744, None, 0.063078, None, -0.00199744, None, 1.25722, None, 0.00663761, None, 1.25722, None, 0.00663761, None)
reports[-1].CovMatrix = ['0.000230681','-6.42609e-07','8.93621e-08','0','0','0','0','0','0','-6.42609e-07','1.09889e-07','1.8991e-09','0','0','0','0','0','0','8.93621e-08','1.8991e-09','0.000113461','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 19513
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0972892, 0.00919578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00040972, 0.000208318, 0), \
                           -32325, 19513, 19513, -nan)
reports[-1].sigmaresid = ValErr(1.26826, 0.00641988, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.109934, None, 0.000236168, None, 0.100158, None, 0.000295049, None, 0.100158, None, 0.000295049, None, 0.102548, None, 0.000245961, None, 0.102548, None, 0.000245961, None, 1.26839, None, 0.00687206, None, 1.26839, None, 0.00687206, None)
reports[-1].CovMatrix = ['8.45624e-05','-3.04145e-07','3.19328e-08','0','0','0','0','0','0','-3.04145e-07','4.33966e-08','6.92289e-10','0','0','0','0','0','0','3.19328e-08','6.92289e-10','4.12149e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 22872
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0938448, 0.00839548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.0846e-05, 0.000187373, 0), \
                           -37457.8, 22872, 22872, -nan)
reports[-1].sigmaresid = ValErr(1.24455, 0.00581896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.097369, None, -0.00024687, None, 0.0942071, None, -9.97439e-05, None, 0.0942071, None, -9.97439e-05, None, 0.0979501, None, 5.22621e-05, None, 0.0979501, None, 5.22621e-05, None, 1.24455, None, 0.00732327, None, 1.24455, None, 0.00732327, None)
reports[-1].CovMatrix = ['7.04842e-05','-3.11491e-07','2.49618e-08','0','0','0','0','0','0','-3.11491e-07','3.51088e-08','5.5664e-10','0','0','0','0','0','0','2.49618e-08','5.5664e-10','3.38603e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 20384
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0353129, 0.00893646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000608083, 0.000199943, 0), \
                           -33516.2, 20384, 20384, -nan)
reports[-1].sigmaresid = ValErr(1.2527, 0.00620423, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0282921, None, -0.00205503, None, 0.0301553, None, -0.0019271, None, 0.0301553, None, -0.0019271, None, 0.0201506, None, -0.00181835, None, 0.0201506, None, -0.00181835, None, 1.25299, None, 0.00720878, None, 1.25299, None, 0.00720878, None)
reports[-1].CovMatrix = ['7.98604e-05','-3.39034e-07','2.86599e-08','0','0','0','0','0','0','-3.39034e-07','3.99772e-08','6.41671e-10','0','0','0','0','0','0','2.86599e-08','6.41671e-10','3.84925e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 15516
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0561118, 0.0102535, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000237861, 0.000234803, 0), \
                           -25663.3, 15516, 15516, -nan)
reports[-1].sigmaresid = ValErr(1.26498, 0.00718088, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0473024, None, -0.00120572, None, 0.0575455, None, -0.00107447, None, 0.0575455, None, -0.00107447, None, 0.0582307, None, -0.00104748, None, 0.0582307, None, -0.00104748, None, 1.26502, None, 0.00776227, None, 1.26502, None, 0.00776227, None)
reports[-1].CovMatrix = ['0.000105134','-3.32348e-07','4.02652e-08','0','0','0','0','0','0','-3.32348e-07','5.51326e-08','9.13721e-10','0','0','0','0','0','0','4.02652e-08','9.13721e-10','5.15651e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 21798
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.067707, 0.00870722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000504677, 0.000201996, 0), \
                           -36335.3, 21798, 21798, -nan)
reports[-1].sigmaresid = ValErr(1.28142, 0.00613718, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0626381, None, 0.000811961, None, 0.0659703, None, 0.000899565, None, 0.0659703, None, 0.000899565, None, 0.0617839, None, 0.00101158, None, 0.0617839, None, 0.00101158, None, 1.28161, None, 0.00724084, None, 1.28161, None, 0.00724084, None)
reports[-1].CovMatrix = ['7.58156e-05','-1.40752e-07','3.08189e-08','0','0','0','0','0','0','-1.40752e-07','4.08024e-08','7.21565e-10','0','0','0','0','0','0','3.08189e-08','7.21565e-10','3.76651e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 12341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0722262, 0.0120474, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00125613, 0.000253586, 0), \
                           -19845.6, 12341, 12341, -nan)
reports[-1].sigmaresid = ValErr(1.20824, 0.00769062, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0351877, None, -0.00102777, None, 0.0465583, None, -0.000774256, None, 0.0465583, None, -0.000774256, None, 0.0550173, None, -0.000777577, None, 0.0550173, None, -0.000777577, None, 1.20944, None, 0.00715199, None, 1.20944, None, 0.00715199, None)
reports[-1].CovMatrix = ['0.00014514','-1.31395e-06','3.65982e-08','0','0','0','0','0','0','-1.31395e-06','6.4306e-08','7.49457e-10','0','0','0','0','0','0','3.65982e-08','7.49457e-10','5.91458e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 17294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0468014, 0.00995955, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000443682, 0.000214555, 0), \
                           -28604.5, 17294, 17294, -nan)
reports[-1].sigmaresid = ValErr(1.265, 0.00680186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0440429, None, 0.000457935, None, 0.0414626, None, 0.000530633, None, 0.0414626, None, 0.000530633, None, 0.0454711, None, 0.000580292, None, 0.0454711, None, 0.000580292, None, 1.26516, None, 0.00752905, None, 1.26516, None, 0.00752905, None)
reports[-1].CovMatrix = ['9.91927e-05','-5.53778e-07','3.26886e-08','0','0','0','0','0','0','-5.53778e-07','4.60336e-08','7.03545e-10','0','0','0','0','0','0','3.26886e-08','7.03545e-10','4.62654e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 22765
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00646881, 0.00846015, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000534665, 0.000191001, 0), \
                           -37480.3, 22765, 22765, -nan)
reports[-1].sigmaresid = ValErr(1.25541, 0.00588352, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00350914, None, -0.000331369, None, -0.00218456, None, -0.000264417, None, -0.00218456, None, -0.000264417, None, -0.00822131, None, -0.000222966, None, -0.00822131, None, -0.000222966, None, 1.25563, None, 0.00723962, None, 1.25563, None, 0.00723962, None)
reports[-1].CovMatrix = ['7.15741e-05','-2.92324e-07','2.59479e-08','0','0','0','0','0','0','-2.92324e-07','3.64814e-08','5.86414e-10','0','0','0','0','0','0','2.59479e-08','5.86414e-10','3.46159e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 20339
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0238779, 0.00905497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000722655, 0.000212422, 0), \
                           -33999.7, 20339, 20339, -nan)
reports[-1].sigmaresid = ValErr(1.28752, 0.00638376, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0265134, None, -0.000108613, None, -0.0215199, None, 1.12737e-05, None, -0.0215199, None, 1.12737e-05, None, -0.0335234, None, 0.000125534, None, -0.0335234, None, 0.000125534, None, 1.28788, None, 0.00723224, None, 1.28788, None, 0.00723224, None)
reports[-1].CovMatrix = ['8.19925e-05','-1.48504e-07','3.4877e-08','0','0','0','0','0','0','-1.48504e-07','4.51229e-08','8.39149e-10','0','0','0','0','0','0','3.4877e-08','8.39149e-10','4.07525e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 16192
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0240253, 0.010138, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000256541, 0.000235412, 0), \
                           -27071.7, 16192, 16192, -nan)
reports[-1].sigmaresid = ValErr(1.28786, 0.00715661, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0169597, None, 0.0024425, None, 0.0233559, None, 0.00246601, None, 0.0233559, None, 0.00246601, None, 0.0116826, None, 0.00268824, None, 0.0116826, None, 0.00268824, None, 1.2879, None, 0.00784698, None, 1.2879, None, 0.00784698, None)
reports[-1].CovMatrix = ['0.000102778','1.3836e-07','5.07482e-08','0','0','0','0','0','0','1.3836e-07','5.54187e-08','1.10502e-09','0','0','0','0','0','0','5.07482e-08','1.10502e-09','5.12171e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 13408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0480255, 0.0110979, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000939034, 0.000240158, 0), \
                           -22323.3, 13408, 13408, -nan)
reports[-1].sigmaresid = ValErr(1.27889, 0.00780979, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0350199, None, -0.000799428, None, 0.0437378, None, -0.000600004, None, 0.0437378, None, -0.000600004, None, 0.04162, None, -0.000555083, None, 0.04162, None, -0.000555083, None, 1.27961, None, 0.0079392, None, 1.27961, None, 0.0079392, None)
reports[-1].CovMatrix = ['0.000123163','-2.60792e-07','5.32026e-08','0','0','0','0','0','0','-2.60792e-07','5.7676e-08','1.12153e-09','0','0','0','0','0','0','5.32026e-08','1.12153e-09','6.09929e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 12916
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0442442, 0.0112625, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000263657, 0.000246092, 0), \
                           -21506.4, 12916, 12916, -nan)
reports[-1].sigmaresid = ValErr(1.2791, 0.0079584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.02927, None, -0.000187718, None, -0.0446909, None, -8.68458e-05, None, -0.0446909, None, -8.68458e-05, None, -0.0301937, None, 1.36845e-05, None, -0.0301937, None, 1.36845e-05, None, 1.27916, None, 0.00747756, None, 1.27916, None, 0.00747756, None)
reports[-1].CovMatrix = ['0.000126843','1.01758e-07','5.89007e-08','0','0','0','0','0','0','1.01758e-07','6.05611e-08','1.2771e-09','0','0','0','0','0','0','5.89007e-08','1.2771e-09','6.33362e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 9799
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0228795, 0.015352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.94939e-05, 0.000366966, 0), \
                           -16954.7, 9799, 9799, -nan)
reports[-1].sigmaresid = ValErr(1.36521, 0.00975197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0365779, None, 0.0020713, None, 0.023251, None, 0.00201889, None, 0.023251, None, 0.00201889, None, 0.0297597, None, 0.00201599, None, 0.0297597, None, 0.00201599, None, 1.36522, None, 0.00808913, None, 1.36522, None, 0.00808913, None)
reports[-1].CovMatrix = ['0.000235685','2.47482e-06','1.53041e-07','0','0','0','0','0','0','2.47482e-06','1.34664e-07','3.73427e-09','0','0','0','0','0','0','1.53041e-07','3.73427e-09','9.51011e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 12768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0584427, 0.0112789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00025868, 0.000266818, 0), \
                           -21180.5, 12768, 12768, -nan)
reports[-1].sigmaresid = ValErr(1.27117, 0.00795477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0487888, None, 0.00161091, None, 0.05766, None, 0.00167767, None, 0.05766, None, 0.00167767, None, 0.0405171, None, 0.00181148, None, 0.0405171, None, 0.00181148, None, 1.27122, None, 0.00747899, None, 1.27122, None, 0.00747899, None)
reports[-1].CovMatrix = ['0.000127214','2.16323e-07','6.02528e-08','0','0','0','0','0','0','2.16323e-07','7.11917e-08','1.43232e-09','0','0','0','0','0','0','6.02528e-08','1.43232e-09','6.32785e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 11622
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0638773, 0.0118554, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000140156, 0.000264802, 0), \
                           -19340.3, 11622, 11622, -nan)
reports[-1].sigmaresid = ValErr(1.27787, 0.0083819, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0379261, None, -0.00117785, None, 0.0637455, None, -0.001117, None, 0.0637455, None, -0.001117, None, 0.0476574, None, -0.000993293, None, 0.0476574, None, -0.000993293, None, 1.27786, None, 0.00712902, None, 1.27786, None, 0.00712902, None)
reports[-1].CovMatrix = ['0.000140549','-5.53112e-08','6.38212e-08','0','0','0','0','0','0','-5.53112e-08','7.01202e-08','1.3378e-09','0','0','0','0','0','0','6.38212e-08','1.3378e-09','7.02564e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 22229
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0744487, 0.00851431, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.0348e-05, 0.000189567, 0), \
                           -36606, 22229, 22229, -nan)
reports[-1].sigmaresid = ValErr(1.25587, 0.00595622, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0731953, None, -0.000814999, None, -0.0741212, None, -0.000689512, None, -0.0741212, None, -0.000689512, None, -0.0532222, None, -0.000674358, None, -0.0532222, None, -0.000674358, None, 1.25587, None, 0.00715978, None, 1.25587, None, 0.00715978, None)
reports[-1].CovMatrix = ['7.24934e-05','-2.3528e-07','2.74819e-08','0','0','0','0','0','0','-2.3528e-07','3.59357e-08','6.19377e-10','0','0','0','0','0','0','2.74819e-08','6.19377e-10','3.54765e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 19673
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0990724, 0.00915272, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.71092e-05, 0.000206674, 0), \
                           -32727.3, 19673, 19673, -nan)
reports[-1].sigmaresid = ValErr(1.27714, 0.00643852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0976478, None, 0.00267588, None, -0.0989084, None, 0.00282174, None, -0.0989084, None, 0.00282174, None, -0.0981847, None, 0.00301217, None, -0.0981847, None, 0.00301217, None, 1.27714, None, 0.00775669, None, 1.27714, None, 0.00775669, None)
reports[-1].CovMatrix = ['8.37722e-05','-1.91938e-07','3.3601e-08','0','0','0','0','0','0','-1.91938e-07','4.27142e-08','7.74252e-10','0','0','0','0','0','0','3.3601e-08','7.74252e-10','4.14546e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 14167
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0446412, 0.0109556, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00036783, 0.00025266, 0), \
                           -23861.9, 14167, 14167, -nan)
reports[-1].sigmaresid = ValErr(1.30393, 0.00774635, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0593141, None, -0.000384029, None, -0.0444923, None, -0.000304151, None, -0.0444923, None, -0.000304151, None, -0.0571853, None, -0.000237067, None, -0.0571853, None, -0.000237067, None, 1.30404, None, 0.00729668, None, 1.30404, None, 0.00729668, None)
reports[-1].CovMatrix = ['0.000120026','-2.78173e-08','5.42356e-08','0','0','0','0','0','0','-2.78173e-08','6.38371e-08','1.24168e-09','0','0','0','0','0','0','5.42356e-08','1.24168e-09','6.0006e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 19411
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0114902, 0.00913157, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000161531, 0.000209515, 0), \
                           -32166.1, 19411, 19411, -nan)
reports[-1].sigmaresid = ValErr(1.26893, 0.0064402, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0168339, None, 0.000185128, None, -0.0109571, None, 0.000355953, None, -0.0109571, None, 0.000355953, None, -0.0110956, None, 0.000389862, None, -0.0110956, None, 0.000389862, None, 1.26894, None, 0.00797586, None, 1.26894, None, 0.00797586, None)
reports[-1].CovMatrix = ['8.33856e-05','-1.38007e-07','3.27985e-08','0','0','0','0','0','0','-1.38007e-07','4.38966e-08','7.61989e-10','0','0','0','0','0','0','3.27985e-08','7.61989e-10','4.14762e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 22047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0211798, 0.00857007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000310041, 0.000193347, 0), \
                           -36417.3, 22047, 22047, -nan)
reports[-1].sigmaresid = ValErr(1.26221, 0.00601092, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0218267, None, 0.00162028, None, -0.019435, None, 0.00173629, None, -0.019435, None, 0.00173629, None, -0.0190042, None, 0.00186676, None, -0.0190042, None, 0.00186676, None, 1.26228, None, 0.00758019, None, 1.26228, None, 0.00758019, None)
reports[-1].CovMatrix = ['7.34461e-05','-2.10353e-07','2.84262e-08','0','0','0','0','0','0','-2.10353e-07','3.7383e-08','6.40257e-10','0','0','0','0','0','0','2.84262e-08','6.40257e-10','3.61312e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 20081
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0215099, 0.00896245, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.0111e-05, 0.000200993, 0), \
                           -32964.5, 20081, 20081, -nan)
reports[-1].sigmaresid = ValErr(1.24936, 0.00623418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0272318, None, 0.00240001, None, 0.0222276, None, 0.0025227, None, 0.0222276, None, 0.0025227, None, 0.00150335, None, 0.00277586, None, 0.00150335, None, 0.00277586, None, 1.24937, None, 0.00771779, None, 1.24937, None, 0.00771779, None)
reports[-1].CovMatrix = ['8.03254e-05','-3.23773e-07','2.94192e-08','0','0','0','0','0','0','-3.23773e-07','4.03982e-08','6.50947e-10','0','0','0','0','0','0','2.94192e-08','6.50947e-10','3.8865e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 21956
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0149778, 0.0088243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00033251, 0.00020473, 0), \
                           -36966.4, 21956, 21956, -nan)
reports[-1].sigmaresid = ValErr(1.30306, 0.00621833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0305211, None, -0.00168032, None, -0.0161532, None, -0.00166997, None, -0.0161532, None, -0.00166997, None, -0.0109366, None, -0.00170422, None, -0.0109366, None, -0.00170422, None, 1.30314, None, 0.00712823, None, 1.30314, None, 0.00712823, None)
reports[-1].CovMatrix = ['7.78682e-05','-1.49419e-07','3.13412e-08','0','0','0','0','0','0','-1.49419e-07','4.19143e-08','7.53992e-10','0','0','0','0','0','0','3.13412e-08','7.53992e-10','3.86677e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 18720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0884903, 0.00972023, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000850761, 0.000233313, 0), \
                           -31875.4, 18720, 18720, -nan)
reports[-1].sigmaresid = ValErr(1.32818, 0.00686417, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.100498, None, 0.00109741, None, 0.090312, None, 0.00112419, None, 0.090312, None, 0.00112419, None, 0.079929, None, 0.00125542, None, 0.079929, None, 0.00125542, None, 1.32865, None, 0.00743243, None, 1.32865, None, 0.00743243, None)
reports[-1].CovMatrix = ['9.44829e-05','1.1643e-07','4.45909e-08','0','0','0','0','0','0','1.1643e-07','5.44348e-08','1.08121e-09','0','0','0','0','0','0','4.45909e-08','1.08121e-09','4.71168e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 10733
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.076142, 0.0125089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000491116, 0.000274933, 0), \
                           -17950.2, 10733, 10733, -nan)
reports[-1].sigmaresid = ValErr(1.28851, 0.00879453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0595398, None, -0.00145515, None, 0.0785284, None, -0.00138852, None, 0.0785284, None, -0.00138852, None, 0.0815639, None, -0.00144018, None, 0.0815639, None, -0.00144018, None, 1.28871, None, 0.00795122, None, 1.28871, None, 0.00795122, None)
reports[-1].CovMatrix = ['0.000156472','3.67219e-07','7.73029e-08','0','0','0','0','0','0','3.67219e-07','7.55882e-08','1.71449e-09','0','0','0','0','0','0','7.73029e-08','1.71449e-09','7.73439e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 819
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0361703, 0.00644702, 0), \
                           ValErr(-0.218422, 0.157141, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.33277e-05, 0.000169328, 0), \
                           239.008, 819, 819, -nan)
reports[-1].sigmaresid = ValErr(0.180728, 0.0044655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0425848, None, 0.000516866, None, 0.0357239, None, 0.000415575, None, 0.0357239, None, 0.000415575, None, 0.0378898, None, 0.000568736, None, 0.0378898, None, 0.000568736, None, 0.180948, None, 0.00716801, None, 0.180948, None, 0.00716801, None)
reports[-1].CovMatrix = ['4.15641e-05','-1.18077e-05','-2.19617e-07','5.83214e-09','0','0','0','0','0','-1.18077e-05','0.0246933','2.1172e-06','1.92641e-07','0','0','0','0','0','-2.19617e-07','2.1172e-06','2.86718e-08','2.09365e-10','0','0','0','0','0','5.83214e-09','1.92641e-07','2.09365e-10','1.99408e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 96222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0455549, 0.000558286, 0), \
                           ValErr(0.013239, 0.0139555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.803e-05, 1.51695e-05, 0), \
                           33235.9, 96222, 96222, -nan)
reports[-1].sigmaresid = ValErr(0.171299, 0.000390482, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0464634, None, -0.000679842, None, -0.0459823, None, -0.000659492, None, -0.0459823, None, -0.000659492, None, -0.0446984, None, -0.000689191, None, -0.0446984, None, -0.000689191, None, 0.171323, None, 0.0039478, None, 0.171323, None, 0.0039478, None)
reports[-1].CovMatrix = ['3.11684e-07','5.26847e-08','-1.24117e-09','5.4344e-11','0','0','0','0','0','5.26847e-08','0.000194755','5.7361e-09','1.61149e-09','0','0','0','0','0','-1.24117e-09','5.7361e-09','2.30115e-10','1.51485e-12','0','0','0','0','0','5.4344e-11','1.61149e-09','1.51485e-12','1.52476e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 90830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0329953, 0.000591293, 0), \
                           ValErr(-0.0362264, 0.0141517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62184e-05, 1.57387e-05, 0), \
                           31124.8, 90830, 90830, -nan)
reports[-1].sigmaresid = ValErr(0.171768, 0.000403008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0329383, None, 0.000322541, None, -0.0333158, None, 0.000283408, None, -0.0333158, None, 0.000283408, None, -0.0319679, None, 0.000290681, None, -0.0319679, None, 0.000290681, None, 0.171777, None, 0.00382281, None, 0.171777, None, 0.00382281, None)
reports[-1].CovMatrix = ['3.49627e-07','-3.97641e-07','-2.44858e-09','4.86593e-11','0','0','0','0','0','-3.97641e-07','0.00020027','5.37829e-09','1.58723e-09','0','0','0','0','0','-2.44858e-09','5.37829e-09','2.47707e-10','1.42622e-12','0','0','0','0','0','4.86593e-11','1.58723e-09','1.42622e-12','1.62415e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 90944
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00996257, 0.000588046, 0), \
                           ValErr(-0.067271, 0.0149112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132063, 1.63997e-05, 0), \
                           28836.6, 90944, 90944, -nan)
reports[-1].sigmaresid = ValErr(0.17622, 0.000413194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0101488, None, -4.85375e-05, None, -0.0101237, None, -5.57612e-05, None, -0.0101237, None, -5.57612e-05, None, -0.00971367, None, -6.71984e-05, None, -0.00971367, None, -6.71984e-05, None, 0.176296, None, 0.00387217, None, 0.176296, None, 0.00387217, None)
reports[-1].CovMatrix = ['3.45798e-07','6.72979e-07','-7.0101e-10','6.7204e-11','0','0','0','0','0','6.72979e-07','0.000222343','2.67999e-08','2.02617e-09','0','0','0','0','0','-7.0101e-10','2.67999e-08','2.6895e-10','1.94983e-12','0','0','0','0','0','6.7204e-11','2.02617e-09','1.94983e-12','1.70729e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 100628
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0157354, 0.000550775, 0), \
                           ValErr(-0.0531629, 0.0138018, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.42538e-05, 1.47868e-05, 0), \
                           33823.3, 100628, 100628, -nan)
reports[-1].sigmaresid = ValErr(0.172897, 0.0003854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0151206, None, -0.000525, None, 0.0155423, None, -0.000516841, None, 0.0155423, None, -0.000516841, None, 0.0149919, None, -0.000526152, None, 0.0149919, None, -0.000526152, None, 0.172914, None, 0.00389809, None, 0.172914, None, 0.00389809, None)
reports[-1].CovMatrix = ['3.03353e-07','-3.63032e-08','-1.17176e-09','5.17042e-11','0','0','0','0','0','-3.63032e-08','0.00019049','4.02392e-10','1.50177e-09','0','0','0','0','0','-1.17176e-09','4.02392e-10','2.1865e-10','1.40409e-12','0','0','0','0','0','5.17042e-11','1.50177e-09','1.40409e-12','1.48534e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 92746
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0425137, 0.00056843, 0), \
                           ValErr(-0.0160175, 0.0141511, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.66305e-05, 1.54485e-05, 0), \
                           32008.5, 92746, 92746, -nan)
reports[-1].sigmaresid = ValErr(0.171348, 0.000397848, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0432796, None, -4.7935e-05, None, 0.0428587, None, -7.41173e-05, None, 0.0428587, None, -7.41173e-05, None, 0.0418911, None, -3.20322e-05, None, 0.0418911, None, -3.20322e-05, None, 0.171367, None, 0.00385407, None, 0.171367, None, 0.00385407, None)
reports[-1].CovMatrix = ['3.23113e-07','-5.09126e-08','-1.249e-09','5.57286e-11','0','0','0','0','0','-5.09126e-08','0.000200253','8.85061e-10','1.61125e-09','0','0','0','0','0','-1.249e-09','8.85061e-10','2.38658e-10','1.53558e-12','0','0','0','0','0','5.57286e-11','1.61125e-09','1.53558e-12','1.58283e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 89766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0535856, 0.000577311, 0), \
                           ValErr(-0.0480952, 0.0147268, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.3132e-05, 1.55602e-05, 0), \
                           31022.7, 89766, 89766, -nan)
reports[-1].sigmaresid = ValErr(0.171266, 0.000404203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0532363, None, -0.000524579, None, 0.0531404, None, -0.00050803, None, 0.0531404, None, -0.00050803, None, 0.0538339, None, -0.00050244, None, 0.0538339, None, -0.00050244, None, 0.171297, None, 0.00383572, None, 0.171297, None, 0.00383572, None)
reports[-1].CovMatrix = ['3.33288e-07','-4.51977e-07','-1.17454e-09','5.50195e-11','0','0','0','0','0','-4.51977e-07','0.000216877','5.86218e-09','1.68259e-09','0','0','0','0','0','-1.17454e-09','5.86218e-09','2.42121e-10','1.60611e-12','0','0','0','0','0','5.50195e-11','1.68259e-09','1.60611e-12','1.6338e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 92347
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0704762, 0.000566186, 0), \
                           ValErr(-0.00229506, 0.0141094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.95503e-05, 1.52884e-05, 0), \
                           33003.3, 92347, 92347, -nan)
reports[-1].sigmaresid = ValErr(0.169259, 0.000393843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0693646, None, 2.2251e-05, None, 0.0699486, None, 2.2387e-05, None, 0.0699486, None, 2.2387e-05, None, 0.0691214, None, -1.00521e-05, None, 0.0691214, None, -1.00521e-05, None, 0.169284, None, 0.00394868, None, 0.169284, None, 0.00394868, None)
reports[-1].CovMatrix = ['3.20566e-07','-1.35535e-07','-1.54914e-09','5.24498e-11','0','0','0','0','0','-1.35535e-07','0.000199076','2.49782e-09','1.61158e-09','0','0','0','0','0','-1.54914e-09','2.49782e-09','2.33734e-10','1.45594e-12','0','0','0','0','0','5.24498e-11','1.61158e-09','1.45594e-12','1.55112e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 83579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0781769, 0.000649281, 0), \
                           ValErr(0.0270117, 0.0155188, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41142e-05, 2.02989e-05, 0), \
                           22728.6, 83579, 83579, -nan)
reports[-1].sigmaresid = ValErr(0.184357, 0.000452745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0777914, None, -0.000252199, None, 0.0780781, None, -0.000233111, None, 0.0780781, None, -0.000233111, None, 0.0784465, None, -0.000188272, None, 0.0784465, None, -0.000188272, None, 0.184362, None, 0.00390598, None, 0.184362, None, 0.00390598, None)
reports[-1].CovMatrix = ['4.21565e-07','-1.45823e-07','1.8642e-09','3.05792e-09','0','0','0','0','0','-1.45823e-07','0.000240835','-1.39932e-08','1.52993e-08','0','0','0','0','0','1.8642e-09','-1.39932e-08','4.12044e-10','-1.86244e-11','0','0','0','0','0','3.05792e-09','1.52993e-08','-1.86244e-11','2.04978e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 92960
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0754933, 0.000574112, 0), \
                           ValErr(-0.0122533, 0.014783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.01118e-05, 1.53503e-05, 0), \
                           33310.8, 92960, 92960, -nan)
reports[-1].sigmaresid = ValErr(0.169099, 0.000392649, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0753512, None, 0.000241829, None, 0.0750318, None, 0.000220579, None, 0.0750318, None, 0.000220579, None, 0.0740941, None, 0.000225002, None, 0.0740941, None, 0.000225002, None, 0.169109, None, 0.00369189, None, 0.169109, None, 0.00369189, None)
reports[-1].CovMatrix = ['3.29604e-07','-1.94321e-07','-2.16387e-09','2.23403e-10','0','0','0','0','0','-1.94321e-07','0.000218537','7.74081e-10','5.26822e-09','0','0','0','0','0','-2.16387e-09','7.74081e-10','2.35631e-10','-2.0912e-11','0','0','0','0','0','2.23403e-10','5.26822e-09','-2.0912e-11','1.54174e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 101212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0610249, 0.000544944, 0), \
                           ValErr(-0.0135063, 0.0136481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.20327e-07, 1.45063e-05, 0), \
                           35238.4, 101212, 101212, -nan)
reports[-1].sigmaresid = ValErr(0.170827, 0.000379687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0609249, None, -0.00100743, None, 0.0610304, None, -0.000951307, None, 0.0610304, None, -0.000951307, None, 0.0608241, None, -0.0010207, None, 0.0608241, None, -0.0010207, None, 0.170828, None, 0.00401742, None, 0.170828, None, 0.00401742, None)
reports[-1].CovMatrix = ['2.96964e-07','4.80438e-09','-1.3483e-09','5.01638e-11','0','0','0','0','0','4.80438e-09','0.00018627','1.03526e-09','1.48873e-09','0','0','0','0','0','-1.3483e-09','1.03526e-09','2.10432e-10','1.34454e-12','0','0','0','0','0','5.01638e-11','1.48873e-09','1.34454e-12','1.44162e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 97333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0485637, 0.000558536, 0), \
                           ValErr(0.029073, 0.0141331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.57319e-05, 1.46806e-05, 0), \
                           34444.2, 97333, 97333, -nan)
reports[-1].sigmaresid = ValErr(0.169854, 0.000384972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0481241, None, 0.00104239, None, 0.0483918, None, 0.000995571, None, 0.0483918, None, 0.000995571, None, 0.048941, None, 0.00101477, None, 0.048941, None, 0.00101477, None, 0.169858, None, 0.00379155, None, 0.169858, None, 0.00379155, None)
reports[-1].CovMatrix = ['3.11963e-07','2.87976e-07','-1.80844e-09','5.20273e-11','0','0','0','0','0','2.87976e-07','0.000199745','-1.46453e-09','1.62704e-09','0','0','0','0','0','-1.80844e-09','-1.46453e-09','2.15519e-10','1.29579e-12','0','0','0','0','0','5.20273e-11','1.62704e-09','1.29579e-12','1.48204e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 108500
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0264371, 0.000530201, 0), \
                           ValErr(-0.00385274, 0.0132543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.06727e-06, 1.40657e-05, 0), \
                           37375.7, 108500, 108500, -nan)
reports[-1].sigmaresid = ValErr(0.171458, 0.000368069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0258751, None, 0.000857248, None, 0.0264143, None, 0.00083342, None, 0.0264143, None, 0.00083342, None, 0.0260233, None, 0.000852883, None, 0.0260233, None, 0.000852883, None, 0.171459, None, 0.00376285, None, 0.171459, None, 0.00376285, None)
reports[-1].CovMatrix = ['2.81113e-07','-2.50399e-08','-1.41786e-09','4.67677e-11','0','0','0','0','0','-2.50399e-08','0.000175675','2.39811e-10','1.39425e-09','0','0','0','0','0','-1.41786e-09','2.39811e-10','1.97843e-10','1.1897e-12','0','0','0','0','0','4.67677e-11','1.39425e-09','1.1897e-12','1.35474e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 101629
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0039326, 0.00054541, 0), \
                           ValErr(0.0392428, 0.0136578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.64126e-05, 1.4336e-05, 0), \
                           36186.1, 101629, 101629, -nan)
reports[-1].sigmaresid = ValErr(0.169484, 0.000375927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.003017, None, 0.000185354, None, 0.00329754, None, 0.00018308, None, 0.00329754, None, 0.00018308, None, 0.00431179, None, 0.000165232, None, 0.00431179, None, 0.000165232, None, 0.169514, None, 0.0037423, None, 0.169514, None, 0.0037423, None)
reports[-1].CovMatrix = ['2.97472e-07','-7.06357e-08','-1.74446e-09','4.71096e-11','0','0','0','0','0','-7.06357e-08','0.000186535','7.45198e-10','1.4779e-09','0','0','0','0','0','-1.74446e-09','7.45198e-10','2.05522e-10','1.26678e-12','0','0','0','0','0','4.71096e-11','1.4779e-09','1.26678e-12','1.41321e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 87265
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00547617, 0.000601724, 0), \
                           ValErr(0.0242284, 0.0143707, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.47896e-05, 1.70484e-05, 0), \
                           27049.4, 87265, 87265, -nan)
reports[-1].sigmaresid = ValErr(0.177478, 0.000424824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00547393, None, 0.00352311, None, -0.00550324, None, 0.00335639, None, -0.00550324, None, 0.00335639, None, -0.00436504, None, 0.00347923, None, -0.00436504, None, 0.00347923, None, 0.177483, None, 0.00395819, None, 0.177483, None, 0.00395819, None)
reports[-1].CovMatrix = ['3.62072e-07','4.2629e-07','2.70513e-10','7.45838e-11','0','0','0','0','0','4.2629e-07','0.000206517','3.01896e-09','1.72017e-09','0','0','0','0','0','2.70513e-10','3.01896e-09','2.90649e-10','2.02214e-12','0','0','0','0','0','7.45838e-11','1.72017e-09','2.02214e-12','1.80475e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 100762
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0277836, 0.000546646, 0), \
                           ValErr(0.0470451, 0.0136679, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00013401, 1.45756e-05, 0), \
                           35556.9, 100762, 100762, -nan)
reports[-1].sigmaresid = ValErr(0.170023, 0.000378744, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0295528, None, 0.000115603, None, -0.0288015, None, 0.000147937, None, -0.0288015, None, 0.000147937, None, -0.0287686, None, 8.50939e-05, None, -0.0287686, None, 8.50939e-05, None, 0.170106, None, 0.00390826, None, 0.170106, None, 0.00390826, None)
reports[-1].CovMatrix = ['2.98822e-07','3.19834e-08','-1.59076e-09','4.91338e-11','0','0','0','0','0','3.19834e-08','0.000186812','3.1633e-09','1.54151e-09','0','0','0','0','0','-1.59076e-09','3.1633e-09','2.12448e-10','1.30828e-12','0','0','0','0','0','4.91338e-11','1.54151e-09','1.30828e-12','1.43447e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 103126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0553065, 0.000542023, 0), \
                           ValErr(0.0511553, 0.0136115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.46419e-05, 1.43475e-05, 0), \
                           36659, 103126, 103126, -nan)
reports[-1].sigmaresid = ValErr(0.169582, 0.000373407, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0556404, None, 0.000281271, None, -0.055855, None, 0.000314221, None, -0.055855, None, 0.000314221, None, -0.0539432, None, 0.000250431, None, -0.0539432, None, 0.000250431, None, 0.169611, None, 0.00380073, None, 0.169611, None, 0.00380073, None)
reports[-1].CovMatrix = ['2.93789e-07','-1.05481e-08','-1.75277e-09','4.67448e-11','0','0','0','0','0','-1.05481e-08','0.000185273','4.45735e-10','1.4694e-09','0','0','0','0','0','-1.75277e-09','4.45735e-10','2.0585e-10','1.23678e-12','0','0','0','0','0','4.67448e-11','1.4694e-09','1.23678e-12','1.39432e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 106994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0488785, 0.000475824, 0), \
                           ValErr(0.0170915, 0.0119045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.30775e-05, 1.26285e-05, 0), \
                           48824.4, 106994, 106994, -nan)
reports[-1].sigmaresid = ValErr(0.153314, 0.000331427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0495632, None, -0.00300478, None, -0.0492926, None, -0.00283219, None, -0.0492926, None, -0.00283219, None, -0.0499226, None, -0.00295385, None, -0.0499226, None, -0.00295385, None, 0.153333, None, 0.00399662, None, 0.153333, None, 0.00399662, None)
reports[-1].CovMatrix = ['2.26408e-07','4.85105e-08','-1.03412e-09','4.34865e-11','0','0','0','0','0','4.85105e-08','0.000141718','-4.13718e-10','1.29894e-09','0','0','0','0','0','-1.03412e-09','-4.13718e-10','1.59479e-10','1.16218e-12','0','0','0','0','0','4.34865e-11','1.29894e-09','1.16218e-12','1.09844e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 103466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.037263, 0.000486055, 0), \
                           ValErr(-0.0337481, 0.0121587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.67516e-05, 1.28666e-05, 0), \
                           46590.2, 103466, 103466, -nan)
reports[-1].sigmaresid = ValErr(0.154242, 0.000338763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0375162, None, 0.00121699, None, -0.0374265, None, 0.00116758, None, -0.0374265, None, 0.00116758, None, -0.0382831, None, 0.00115681, None, -0.0382831, None, 0.00115681, None, 0.154251, None, 0.00392998, None, 0.154251, None, 0.00392998, None)
reports[-1].CovMatrix = ['2.3625e-07','1.32684e-08','-1.03076e-09','2.60841e-10','0','0','0','0','0','1.32684e-08','0.000147835','2.83716e-10','-3.1039e-10','0','0','0','0','0','-1.03076e-09','2.83716e-10','1.65549e-10','-5.17453e-12','0','0','0','0','0','2.60841e-10','-3.1039e-10','-5.17453e-12','1.14761e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 95793
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.019174, 0.000504192, 0), \
                           ValErr(-0.028244, 0.0121705, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.09309e-05, 1.31196e-05, 0), \
                           44079.1, 95793, 95793, -nan)
reports[-1].sigmaresid = ValErr(0.152729, 0.000354727, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0199573, None, -0.00346882, None, -0.0197381, None, -0.00330703, None, -0.0197381, None, -0.00330703, None, -0.0203598, None, -0.00349062, None, -0.0203598, None, -0.00349062, None, 0.152765, None, 0.00395668, None, 0.152765, None, 0.00395668, None)
reports[-1].CovMatrix = ['2.54209e-07','2.29563e-07','-1.28125e-09','1.21761e-09','0','0','0','0','0','2.29563e-07','0.000148122','-2.96381e-09','3.74649e-08','0','0','0','0','0','-1.28125e-09','-2.96381e-09','1.72123e-10','-8.10971e-11','0','0','0','0','0','1.21761e-09','3.74649e-08','-8.10971e-11','1.25831e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 102363
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00536482, 0.000489163, 0), \
                           ValErr(-0.0785814, 0.0122244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.9406e-05, 1.29665e-05, 0), \
                           46117, 102363, 102363, -nan)
reports[-1].sigmaresid = ValErr(0.154206, 0.000340812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524291, None, -7.25839e-06, None, 0.00549067, None, -3.25848e-05, None, 0.00549067, None, -3.25848e-05, None, 0.00561017, None, -7.57841e-05, None, 0.00561017, None, -7.57841e-05, None, 0.154239, None, 0.00401179, None, 0.154239, None, 0.00401179, None)
reports[-1].CovMatrix = ['2.3928e-07','-1.14033e-09','-1.08278e-09','4.57658e-11','0','0','0','0','0','-1.14033e-09','0.000149435','3.94362e-10','1.37013e-09','0','0','0','0','0','-1.08278e-09','3.94362e-10','1.6813e-10','1.21862e-12','0','0','0','0','0','4.57658e-11','1.37013e-09','1.21862e-12','1.16153e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 101743
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0257593, 0.000494199, 0), \
                           ValErr(-0.0608262, 0.0123444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.77452e-05, 1.30652e-05, 0), \
                           44673.9, 101743, 101743, -nan)
reports[-1].sigmaresid = ValErr(0.155981, 0.000345819, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0261251, None, -0.00045114, None, 0.0255368, None, -0.000417735, None, 0.0255368, None, -0.000417735, None, 0.0257502, None, -0.000449458, None, 0.0257502, None, -0.000449458, None, 0.156006, None, 0.00395027, None, 0.156006, None, 0.00395027, None)
reports[-1].CovMatrix = ['2.44233e-07','-2.9628e-08','-9.48233e-10','-9.94922e-11','0','0','0','0','0','-2.9628e-08','0.000152384','-8.2272e-10','2.51155e-10','0','0','0','0','0','-9.48233e-10','-8.2272e-10','1.70701e-10','1.30827e-12','0','0','0','0','0','-9.94922e-11','2.51155e-10','1.30827e-12','1.19591e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 98266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0462683, 0.000494161, 0), \
                           ValErr(-0.0249353, 0.0123856, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.3306e-05, 1.31785e-05, 0), \
                           45309.4, 98266, 98266, -nan)
reports[-1].sigmaresid = ValErr(0.152586, 0.000344189, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0455501, None, -0.000229677, None, 0.0461808, None, -0.000271398, None, 0.0461808, None, -0.000271398, None, 0.0464872, None, -0.000372773, None, 0.0464872, None, -0.000372773, None, 0.15259, None, 0.00398462, None, 0.15259, None, 0.00398462, None)
reports[-1].CovMatrix = ['2.44195e-07','-1.14435e-08','-1.12295e-09','4.62121e-11','0','0','0','0','0','-1.14435e-08','0.000153402','-2.64346e-10','1.41098e-09','0','0','0','0','0','-1.12295e-09','-2.64346e-10','1.73673e-10','1.26998e-12','0','0','0','0','0','4.62121e-11','1.41098e-09','1.26998e-12','1.18466e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 98756
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0580945, 0.000493547, 0), \
                           ValErr(-0.00555162, 0.0125404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.27796e-05, 1.31116e-05, 0), \
                           45458.4, 98756, 98756, -nan)
reports[-1].sigmaresid = ValErr(0.152705, 0.000343603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0586001, None, 6.43537e-05, None, 0.0583783, None, 8.67538e-05, None, 0.0583783, None, 8.67538e-05, None, 0.0590036, None, 6.69215e-05, None, 0.0590036, None, 6.69215e-05, None, 0.152713, None, 0.00387079, None, 0.152713, None, 0.00387079, None)
reports[-1].CovMatrix = ['2.43589e-07','1.62135e-07','-1.12174e-09','4.90653e-11','0','0','0','0','0','1.62135e-07','0.000157263','-1.7475e-09','1.46641e-09','0','0','0','0','0','-1.12174e-09','-1.7475e-09','1.71914e-10','1.23079e-12','0','0','0','0','0','4.90653e-11','1.46641e-09','1.23079e-12','1.18063e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 96896
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0676637, 0.000502725, 0), \
                           ValErr(0.0152828, 0.0126583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2709e-05, 1.34843e-05, 0), \
                           43794.8, 96896, 96896, -nan)
reports[-1].sigmaresid = ValErr(0.153983, 0.000349787, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0668109, None, 0.000209669, None, 0.067508, None, 0.000206697, None, 0.067508, None, 0.000206697, None, 0.0682108, None, 0.000215365, None, 0.0682108, None, 0.000215365, None, 0.153986, None, 0.00387841, None, 0.153986, None, 0.00387841, None)
reports[-1].CovMatrix = ['2.52732e-07','9.01272e-08','-1.20661e-09','4.79406e-11','0','0','0','0','0','9.01272e-08','0.000160232','-4.33261e-09','1.43105e-09','0','0','0','0','0','-1.20661e-09','-4.33261e-09','1.81827e-10','1.25066e-12','0','0','0','0','0','4.79406e-11','1.43105e-09','1.25066e-12','1.22351e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 103052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0742121, 0.00048236, 0), \
                           ValErr(0.0176594, 0.0120642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.24955e-05, 1.28306e-05, 0), \
                           47642.4, 103052, 103052, -nan)
reports[-1].sigmaresid = ValErr(0.152399, 0.000335691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0735746, None, 0.000578316, None, 0.0740606, None, 0.000572161, None, 0.0740606, None, 0.000572161, None, 0.0737993, None, 0.000566574, None, 0.0737993, None, 0.000566574, None, 0.152403, None, 0.0039078, None, 0.152403, None, 0.0039078, None)
reports[-1].CovMatrix = ['2.32671e-07','2.29972e-08','-1.09576e-09','4.5195e-11','0','0','0','0','0','2.29972e-08','0.000145545','-1.25709e-09','1.33864e-09','0','0','0','0','0','-1.09576e-09','-1.25709e-09','1.64626e-10','1.18451e-12','0','0','0','0','0','4.5195e-11','1.33864e-09','1.18451e-12','1.12688e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 93455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0676456, 0.000518149, 0), \
                           ValErr(-0.0242843, 0.0133294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000115733, 1.42799e-05, 0), \
                           40351.3, 93455, 93455, -nan)
reports[-1].sigmaresid = ValErr(0.157125, 0.000363437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0680826, None, 0.00215812, None, 0.0680276, None, 0.0020676, None, 0.0680276, None, 0.0020676, None, 0.0669471, None, 0.00209299, None, 0.0669471, None, 0.00209299, None, 0.157181, None, 0.0038044, None, 0.157181, None, 0.0038044, None)
reports[-1].CovMatrix = ['2.68479e-07','-4.55734e-07','-7.26077e-10','5.05875e-11','0','0','0','0','0','-4.55734e-07','0.000177673','-2.582e-08','1.24243e-09','0','0','0','0','0','-7.26077e-10','-2.582e-08','2.03916e-10','1.30382e-12','0','0','0','0','0','5.05875e-11','1.24243e-09','1.30382e-12','1.32087e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 104442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0572704, 0.000481913, 0), \
                           ValErr(0.0222732, 0.0120813, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.59785e-05, 1.27299e-05, 0), \
                           47868.9, 104442, 104442, -nan)
reports[-1].sigmaresid = ValErr(0.153007, 0.000334779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.057301, None, -0.00515119, None, 0.0573852, None, -0.00491701, None, 0.0573852, None, -0.00491701, None, 0.0578857, None, -0.00506027, None, 0.0578857, None, -0.00506027, None, 0.153011, None, 0.00399552, None, 0.153011, None, 0.00399552, None)
reports[-1].CovMatrix = ['2.32241e-07','-5.77782e-09','-1.14457e-09','4.43518e-11','0','0','0','0','0','-5.77782e-09','0.000145957','-1.05657e-09','1.33554e-09','0','0','0','0','0','-1.14457e-09','-1.05657e-09','1.6205e-10','1.13584e-12','0','0','0','0','0','4.43518e-11','1.33554e-09','1.13584e-12','1.12077e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 104190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.043161, 0.000483692, 0), \
                           ValErr(0.0310081, 0.0121279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.14349e-05, 1.25662e-05, 0), \
                           48139.3, 104190, 104190, -nan)
reports[-1].sigmaresid = ValErr(0.152442, 0.000333303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.042273, None, 0.000886382, None, 0.0429002, None, 0.00090978, None, 0.0429002, None, 0.00090978, None, 0.0430576, None, 0.000947295, None, 0.0430576, None, 0.000947295, None, 0.152451, None, 0.00384126, None, 0.152451, None, 0.00384126, None)
reports[-1].CovMatrix = ['2.33958e-07','-3.02798e-09','-1.31925e-09','-3.34468e-10','0','0','0','0','0','-3.02798e-09','0.000147086','1.97061e-10','-5.00417e-11','0','0','0','0','0','-1.31925e-09','1.97061e-10','1.57909e-10','6.49385e-12','0','0','0','0','0','-3.34468e-10','-5.00417e-11','6.49385e-12','1.11091e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 109373
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0184101, 0.000472983, 0), \
                           ValErr(0.0342712, 0.0118607, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.17566e-05, 1.25065e-05, 0), \
                           50355.1, 109373, 109373, -nan)
reports[-1].sigmaresid = ValErr(0.152691, 0.000330605, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0176949, None, 1.57063e-05, None, 0.0179272, None, 1.85372e-05, None, 0.0179272, None, 1.85372e-05, None, 0.018327, None, -1.11369e-05, None, 0.018327, None, -1.11369e-05, None, 0.152714, None, 0.00390692, None, 0.152714, None, 0.00390692, None)
reports[-1].CovMatrix = ['2.23713e-07','-9.08104e-09','-1.22402e-09','-9.91092e-10','0','0','0','0','0','-9.08104e-09','0.000140676','-2.13734e-10','2.15697e-09','0','0','0','0','0','-1.22402e-09','-2.13734e-10','1.56413e-10','6.6996e-11','0','0','0','0','0','-9.91092e-10','2.15697e-09','6.6996e-11','1.093e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 103782
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000359889, 0.000490455, 0), \
                           ValErr(-0.00245427, 0.0172454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.99378e-05, 1.2859e-05, 0), \
                           47173.8, 103782, 103782, -nan)
reports[-1].sigmaresid = ValErr(0.153587, 0.00033745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156465, None, 0.000130903, None, -0.000648683, None, 0.000148063, None, -0.000648683, None, 0.000148063, None, -0.000853632, None, 0.000150409, None, -0.000853632, None, 0.000150409, None, 0.153595, None, 0.003906, None, 0.153595, None, 0.003906, None)
reports[-1].CovMatrix = ['2.40546e-07','-8.44784e-07','-1.23145e-09','1.03253e-09','0','0','0','0','0','-8.44784e-07','0.000297404','5.44875e-09','-1.83878e-07','0','0','0','0','0','-1.23145e-09','5.44875e-09','1.65355e-10','-9.26384e-12','0','0','0','0','0','1.03253e-09','-1.83878e-07','-9.26384e-12','1.13873e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 106318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0199239, 0.000477886, 0), \
                           ValErr(0.0412336, 0.0119324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.8154e-05, 1.26232e-05, 0), \
                           49382.8, 106318, 106318, -nan)
reports[-1].sigmaresid = ValErr(0.152069, 0.000337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0212224, None, 0.000698465, None, -0.0205368, None, 0.000658208, None, -0.0205368, None, 0.000658208, None, -0.01934, None, 0.00061501, None, -0.01934, None, 0.00061501, None, 0.152105, None, 0.00388983, None, 0.152105, None, 0.00388983, None)
reports[-1].CovMatrix = ['2.28375e-07','1.69618e-09','-1.24997e-09','1.95413e-09','0','0','0','0','0','1.69618e-09','0.000142381','2.98382e-10','-2.82035e-08','0','0','0','0','0','-1.24997e-09','2.98382e-10','1.59345e-10','-8.89042e-11','0','0','0','0','0','1.95413e-09','-2.82035e-08','-8.89042e-11','1.13569e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 62958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.039959, 0.000633341, 0), \
                           ValErr(0.0498714, 0.015345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.28791e-05, 1.43509e-05, 0), \
                           26571.4, 62958, 62958, -nan)
reports[-1].sigmaresid = ValErr(0.15866, 0.000447123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0401716, None, -0.000387002, None, -0.0398018, None, -0.00042797, None, -0.0398018, None, -0.00042797, None, -0.0404773, None, -0.000432515, None, -0.0404773, None, -0.000432515, None, 0.158686, None, 0.00404746, None, 0.158686, None, 0.00404746, None)
reports[-1].CovMatrix = ['4.01121e-07','-3.01702e-07','4.18937e-10','9.0284e-11','0','0','0','0','0','-3.01702e-07','0.00023547','7.91038e-09','2.1709e-09','0','0','0','0','0','4.18937e-10','7.91038e-09','2.05948e-10','2.17095e-12','0','0','0','0','0','9.0284e-11','2.1709e-09','2.17095e-12','1.99919e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 106547
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0465212, 0.000474014, 0), \
                           ValErr(-0.013327, 0.0118816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.43802e-05, 1.25364e-05, 0), \
                           49762.1, 106547, 106547, -nan)
reports[-1].sigmaresid = ValErr(0.15168, 0.000328581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0469662, None, 0.000220381, None, -0.0468513, None, 0.000230521, None, -0.0468513, None, 0.000230521, None, -0.0482336, None, 0.000215845, None, -0.0482336, None, 0.000215845, None, 0.15169, None, 0.0038438, None, 0.15169, None, 0.0038438, None)
reports[-1].CovMatrix = ['2.2469e-07','1.00658e-08','-1.17321e-09','4.19201e-11','0','0','0','0','0','1.00658e-08','0.000141171','-3.86964e-10','1.3009e-09','0','0','0','0','0','-1.17321e-09','-3.86964e-10','1.5716e-10','1.12001e-12','0','0','0','0','0','4.19201e-11','1.3009e-09','1.12001e-12','1.07966e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 103952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0530765, 0.000490762, 0), \
                           ValErr(-0.0241974, 0.0152988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.33598e-05, 1.29547e-05, 0), \
                           48971, 103952, 103952, -nan)
reports[-1].sigmaresid = ValErr(0.151067, 0.000331966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0540859, None, -0.000646556, None, -0.0535034, None, -0.000572976, None, -0.0535034, None, -0.000572976, None, -0.05345, None, -0.000594921, None, -0.05345, None, -0.000594921, None, 0.151083, None, 0.00388412, None, 0.151083, None, 0.00388412, None)
reports[-1].CovMatrix = ['2.40847e-07','9.78177e-07','-1.56246e-09','-1.76868e-09','0','0','0','0','0','9.78177e-07','0.000234054','-2.84975e-08','-1.59106e-07','0','0','0','0','0','-1.56246e-09','-2.84975e-08','1.67825e-10','4.65734e-11','0','0','0','0','0','-1.76868e-09','-1.59106e-07','4.65734e-11','1.10202e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 185770
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0589698, 0.000878534, 0), \
                           ValErr(0.0373204, 0.0101327, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.43314e-05, 1.72249e-05, 0), \
                           -81614.3, 185770, 185770, -nan)
reports[-1].sigmaresid = ValErr(0.375458, 0.000615969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0592606, None, 0.000241688, None, -0.0591997, None, 0.000301094, None, -0.0591997, None, 0.000301094, None, -0.0582455, None, 0.000252352, None, -0.0582455, None, 0.000252352, None, 0.375474, None, 0.00760828, None, 0.375474, None, 0.00760828, None)
reports[-1].CovMatrix = ['7.71823e-07','1.99848e-07','-1.93439e-09','1.57951e-10','0','0','0','0','0','1.99848e-07','0.000102671','-5.34622e-10','2.08932e-09','0','0','0','0','0','-1.93439e-09','-5.34622e-10','2.96699e-10','3.02041e-12','0','0','0','0','0','1.57951e-10','2.08932e-09','3.02041e-12','3.79418e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 103285
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0355171, 0.00118338, 0), \
                           ValErr(-0.0280849, 0.0124551, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.40151e-05, 2.37675e-05, 0), \
                           -45922.6, 103285, 103285, -nan)
reports[-1].sigmaresid = ValErr(0.37745, 0.000830473, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0362437, None, -0.00026219, None, -0.0356344, None, -0.000420854, None, -0.0356344, None, -0.000420854, None, -0.0377058, None, -0.000239836, None, -0.0377058, None, -0.000239836, None, 0.377459, None, 0.00791336, None, 0.377459, None, 0.00791336, None)
reports[-1].CovMatrix = ['1.40039e-06','-1.74685e-07','-3.42928e-09','2.79168e-10','0','0','0','0','0','-1.74685e-07','0.000155131','-4.96453e-10','3.29476e-09','0','0','0','0','0','-3.42928e-09','-4.96453e-10','5.64893e-10','5.68322e-12','0','0','0','0','0','2.79168e-10','3.29476e-09','5.68322e-12','6.89685e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 190461
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.018051, 0.000867161, 0), \
                           ValErr(-0.0250061, 0.0100055, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.47644e-05, 1.74735e-05, 0), \
                           -84221.6, 190461, 190461, -nan)
reports[-1].sigmaresid = ValErr(0.376537, 0.000610084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0181923, None, -0.000310512, None, 0.017968, None, -0.000313498, None, 0.017968, None, -0.000313498, None, 0.0173799, None, -0.000376518, None, 0.0173799, None, -0.000376518, None, 0.376544, None, 0.00767923, None, 0.376544, None, 0.00767923, None)
reports[-1].CovMatrix = ['7.51968e-07','-3.95577e-08','-1.5182e-09','1.547e-10','0','0','0','0','0','-3.95577e-08','0.000100111','2.55031e-10','1.96399e-09','0','0','0','0','0','-1.5182e-09','2.55031e-10','3.05322e-10','3.12818e-12','0','0','0','0','0','1.547e-10','1.96399e-09','3.12818e-12','3.72202e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 172115
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0607825, 0.000903632, 0), \
                           ValErr(-0.0466758, 0.0102114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.23276e-05, 1.8322e-05, 0), \
                           -74302.7, 172115, 172115, -nan)
reports[-1].sigmaresid = ValErr(0.372606, 0.000635075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0612231, None, -0.000851586, None, 0.0607037, None, -0.00090436, None, 0.0607037, None, -0.00090436, None, 0.0602189, None, -0.00101735, None, 0.0602189, None, -0.00101735, None, 0.37263, None, 0.0079737, None, 0.37263, None, 0.0079737, None)
reports[-1].CovMatrix = ['8.16551e-07','8.60513e-08','-1.81604e-09','1.66886e-10','0','0','0','0','0','8.60513e-08','0.000104272','1.51387e-09','2.12394e-09','0','0','0','0','0','-1.81604e-09','1.51387e-09','3.35697e-10','3.36662e-12','0','0','0','0','0','1.66886e-10','2.12394e-09','3.36662e-12','4.03321e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 183918
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0856449, 0.000875627, 0), \
                           ValErr(0.0300015, 0.0101056, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.30509e-05, 1.7708e-05, 0), \
                           -79586.6, 183918, 183918, -nan)
reports[-1].sigmaresid = ValErr(0.372988, 0.000614989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0857119, None, -1.49832e-05, None, 0.0858417, None, -2.37061e-05, None, 0.0858417, None, -2.37061e-05, None, 0.0868286, None, -3.89143e-05, None, 0.0868286, None, -3.89143e-05, None, 0.373003, None, 0.00752774, None, 0.373003, None, 0.00752774, None)
reports[-1].CovMatrix = ['7.66723e-07','1.66148e-07','-1.77553e-09','1.57429e-10','0','0','0','0','0','1.66148e-07','0.000102122','-1.34133e-09','2.01522e-09','0','0','0','0','0','-1.77553e-09','-1.34133e-09','3.13573e-10','3.08988e-12','0','0','0','0','0','1.57429e-10','2.01522e-09','3.08988e-12','3.78212e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 192929
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0704865, 0.000855304, 0), \
                           ValErr(-0.00785393, 0.00986084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.78787e-05, 1.71496e-05, 0), \
                           -83142.9, 192929, 192929, -nan)
reports[-1].sigmaresid = ValErr(0.372325, 0.000599389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0716082, None, 7.22461e-05, None, 0.0707411, None, -6.19023e-05, None, 0.0707411, None, -6.19023e-05, None, 0.0703241, None, -0.000130392, None, 0.0703241, None, -0.000130392, None, 0.37233, None, 0.0077788, None, 0.37233, None, 0.0077788, None)
reports[-1].CovMatrix = ['7.31545e-07','3.79435e-08','-1.95525e-09','1.44521e-10','0','0','0','0','0','3.79435e-08','9.72361e-05','-4.43091e-10','1.88071e-09','0','0','0','0','0','-1.95525e-09','-4.43091e-10','2.94107e-10','2.86708e-12','0','0','0','0','0','1.44521e-10','1.88071e-09','2.86708e-12','3.59267e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 204097
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0243849, 0.000834805, 0), \
                           ValErr(0.031679, 0.00965914, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.37291e-05, 1.67318e-05, 0), \
                           -87952.3, 204097, 204097, -nan)
reports[-1].sigmaresid = ValErr(0.372319, 0.000583106, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0243639, None, 1.27714e-05, None, 0.0242091, None, -7.60407e-05, None, 0.0242091, None, -7.60407e-05, None, 0.0247204, None, -0.000128825, None, 0.0247204, None, -0.000128825, None, 0.37233, None, 0.00765768, None, 0.37233, None, 0.00765768, None)
reports[-1].CovMatrix = ['6.969e-07','-3.55561e-08','-2.17659e-09','3.4059e-11','0','0','0','0','0','-3.55561e-08','9.3299e-05','8.40952e-10','9.17268e-10','0','0','0','0','0','-2.17659e-09','8.40952e-10','2.79955e-10','1.80031e-11','0','0','0','0','0','3.4059e-11','9.17268e-10','1.80031e-11','3.40013e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 186181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0106767, 0.000874382, 0), \
                           ValErr(0.0785323, 0.0101559, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.12327e-06, 1.77914e-05, 0), \
                           -81762.8, 186181, 186181, -nan)
reports[-1].sigmaresid = ValErr(0.375393, 0.000615182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0103326, None, -0.00018567, None, -0.0111223, None, -0.000188524, None, -0.0111223, None, -0.000188524, None, -0.0111, None, -0.00027344, None, -0.0111, None, -0.00027344, None, 0.375454, None, 0.00773157, None, 0.375454, None, 0.00773157, None)
reports[-1].CovMatrix = ['7.64544e-07','5.38883e-07','-1.16594e-09','1.75061e-10','0','0','0','0','0','5.38883e-07','0.000103142','1.29173e-08','2.32332e-09','0','0','0','0','0','-1.16594e-09','1.29173e-08','3.16535e-10','3.54565e-12','0','0','0','0','0','1.75061e-10','2.32332e-09','3.54565e-12','3.78449e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 196223
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0488652, 0.000847693, 0), \
                           ValErr(0.0147386, 0.00981975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.84493e-05, 1.7023e-05, 0), \
                           -84188.5, 196223, 196223, -nan)
reports[-1].sigmaresid = ValErr(0.371616, 0.000593205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.048, None, 0.000501987, None, -0.0490888, None, 0.000551081, None, -0.0490888, None, 0.000551081, None, -0.0485486, None, 0.00053122, None, -0.0485486, None, 0.00053122, None, 0.371621, None, 0.00751764, None, 0.371621, None, 0.00751764, None)
reports[-1].CovMatrix = ['7.18583e-07','1.40754e-07','-2.05615e-09','1.41852e-10','0','0','0','0','0','1.40754e-07','9.64274e-05','2.16551e-10','1.89406e-09','0','0','0','0','0','-2.05615e-09','2.16551e-10','2.89784e-10','2.80693e-12','0','0','0','0','0','1.41852e-10','1.89406e-09','2.80693e-12','3.51892e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 190471
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0525095, 0.000827523, 0), \
                           ValErr(-0.012894, 0.00953182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.12101e-05, 1.66919e-05, 0), \
                           -74986.6, 190471, 190471, -nan)
reports[-1].sigmaresid = ValErr(0.358707, 0.000581179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0518862, None, 0.00112171, None, -0.0523221, None, 0.00122763, None, -0.0523221, None, 0.00122763, None, -0.0530664, None, 0.00126625, None, -0.0530664, None, 0.00126625, None, 0.358712, None, 0.00796405, None, 0.358712, None, 0.00796405, None)
reports[-1].CovMatrix = ['6.84794e-07','5.58175e-08','-1.60287e-09','1.31635e-10','0','0','0','0','0','5.58175e-08','9.08555e-05','-2.46848e-10','1.6962e-09','0','0','0','0','0','-1.60287e-09','-2.46848e-10','2.78619e-10','2.66149e-12','0','0','0','0','0','1.31635e-10','1.6962e-09','2.66149e-12','3.37769e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 188196
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00858381, 0.000830625, 0), \
                           ValErr(-0.089605, 0.00959018, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.07913e-06, 1.67151e-05, 0), \
                           -73554.6, 188196, 188196, -nan)
reports[-1].sigmaresid = ValErr(0.357685, 0.000583014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0086841, None, 0.000554079, None, -0.00855197, None, 0.000610723, None, -0.00855197, None, 0.000610723, None, -0.00897734, None, 0.000606723, None, -0.00897734, None, 0.000606723, None, 0.35777, None, 0.00783931, None, 0.35777, None, 0.00783931, None)
reports[-1].CovMatrix = ['6.89937e-07','2.42815e-08','-1.68117e-09','1.30738e-10','0','0','0','0','0','2.42815e-08','9.19715e-05','-7.6568e-10','1.69941e-09','0','0','0','0','0','-1.68117e-09','-7.6568e-10','2.79396e-10','2.66281e-12','0','0','0','0','0','1.30738e-10','1.69941e-09','2.66281e-12','3.39906e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 179377
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0458543, 0.000846446, 0), \
                           ValErr(-0.021631, 0.00972856, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.08629e-05, 1.72837e-05, 0), \
                           -69853.2, 179377, 179377, -nan)
reports[-1].sigmaresid = ValErr(0.357179, 0.00059633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.045414, None, -0.000813575, None, 0.0460297, None, -0.00084197, None, 0.0460297, None, -0.00084197, None, 0.0457699, None, -0.000926683, None, 0.0457699, None, -0.000926683, None, 0.35719, None, 0.0078984, None, 0.35719, None, 0.0078984, None)
reports[-1].CovMatrix = ['7.16471e-07','1.65863e-08','-1.25179e-09','1.42151e-10','0','0','0','0','0','1.65863e-08','9.4645e-05','6.0494e-10','1.77987e-09','0','0','0','0','0','-1.25179e-09','6.0494e-10','2.98725e-10','2.85962e-12','0','0','0','0','0','1.42151e-10','1.77987e-09','2.85962e-12','3.55609e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 180983
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0699958, 0.000844533, 0), \
                           ValErr(0.0204715, 0.00973922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.58539e-05, 1.71041e-05, 0), \
                           -70320.3, 180983, 180983, -nan)
reports[-1].sigmaresid = ValErr(0.356866, 0.000593159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0707894, None, 0.000326559, None, 0.0701978, None, 0.000403043, None, 0.0701978, None, 0.000403043, None, 0.0699448, None, 0.000379254, None, 0.0699448, None, 0.000379254, None, 0.356876, None, 0.0078906, None, 0.356876, None, 0.0078906, None)
reports[-1].CovMatrix = ['7.13236e-07','1.18399e-08','-1.67214e-09','1.37735e-10','0','0','0','0','0','1.18399e-08','9.48524e-05','-3.4676e-10','1.76665e-09','0','0','0','0','0','-1.67214e-09','-3.4676e-10','2.92551e-10','2.69999e-12','0','0','0','0','0','1.37735e-10','1.76665e-09','2.69999e-12','3.51837e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 186015
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.081239, 0.000839362, 0), \
                           ValErr(0.0187546, 0.00963647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.26518e-05, 1.6847e-05, 0), \
                           -71002.2, 186015, 186015, -nan)
reports[-1].sigmaresid = ValErr(0.354432, 0.000583233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0815314, None, -0.00116814, None, 0.0815354, None, -0.00126363, None, 0.0815354, None, -0.00126363, None, 0.0829405, None, -0.00135028, None, 0.0829405, None, -0.00135028, None, 0.354443, None, 0.00799299, None, 0.354443, None, 0.00799299, None)
reports[-1].CovMatrix = ['7.04529e-07','1.42811e-07','-2.2917e-09','-5.56833e-09','0','0','0','0','0','1.42811e-07','9.28616e-05','-3.2822e-09','-2.7966e-08','0','0','0','0','0','-2.2917e-09','-3.2822e-09','2.83821e-10','1.12042e-10','0','0','0','0','0','-5.56833e-09','-2.7966e-08','1.12042e-10','3.40161e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 192551
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0558828, 0.000815839, 0), \
                           ValErr(-0.00538642, 0.00949371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.92915e-05, 1.62826e-05, 0), \
                           -72737.9, 192551, 192551, -nan)
reports[-1].sigmaresid = ValErr(0.353038, 0.000568895, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0565098, None, -5.50544e-05, None, 0.0560499, None, -9.31696e-05, None, 0.0560499, None, -9.31696e-05, None, 0.0554192, None, -0.000141957, None, 0.0554192, None, -0.000141957, None, 0.35304, None, 0.00783732, None, 0.35304, None, 0.00783732, None)
reports[-1].CovMatrix = ['6.65592e-07','1.34084e-07','-2.19137e-09','1.20905e-10','0','0','0','0','0','1.34084e-07','9.01306e-05','-2.51306e-10','1.64966e-09','0','0','0','0','0','-2.19137e-09','-2.51306e-10','2.65122e-10','2.33285e-12','0','0','0','0','0','1.20905e-10','1.64966e-09','2.33285e-12','3.23642e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 194706
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00180834, 0.000808612, 0), \
                           ValErr(-0.00511476, 0.00934523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.60357e-05, 1.61517e-05, 0), \
                           -72837.6, 194706, 194706, -nan)
reports[-1].sigmaresid = ValErr(0.351745, 0.000563668, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218481, None, 0.000590544, None, 0.00194568, None, 0.000656504, None, 0.00194568, None, 0.000656504, None, 0.00220069, None, 0.000662703, None, 0.00220069, None, 0.000662703, None, 0.351746, None, 0.00791908, None, 0.351746, None, 0.00791908, None)
reports[-1].CovMatrix = ['6.53853e-07','4.39294e-08','-2.19016e-09','1.15433e-10','0','0','0','0','0','4.39294e-08','8.73333e-05','4.31783e-11','1.58527e-09','0','0','0','0','0','-2.19016e-09','4.31783e-11','2.60877e-10','2.30122e-12','0','0','0','0','0','1.15433e-10','1.58527e-09','2.30122e-12','3.17722e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 193459
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0307063, 0.000813257, 0), \
                           ValErr(0.0422445, 0.00940588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.89258e-05, 1.62712e-05, 0), \
                           -73060.9, 193459, 193459, -nan)
reports[-1].sigmaresid = ValErr(0.353001, 0.000567501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0330025, None, 0.000722356, None, -0.0314945, None, 0.000761601, None, -0.0314945, None, 0.000761601, None, -0.0315811, None, 0.000772911, None, -0.0315811, None, 0.000772911, None, 0.353054, None, 0.00775061, None, 0.353054, None, 0.00775061, None)
reports[-1].CovMatrix = ['6.61388e-07','-2.25863e-08','-2.13804e-09','1.17538e-10','0','0','0','0','0','-2.25863e-08','8.84705e-05','-3.33295e-11','1.59498e-09','0','0','0','0','0','-2.13804e-09','-3.33295e-11','2.64753e-10','2.36237e-12','0','0','0','0','0','1.17538e-10','1.59498e-09','2.36237e-12','3.22057e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 195291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0601945, 0.000809127, 0), \
                           ValErr(-0.0137607, 0.00935431, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.8145e-05, 1.6232e-05, 0), \
                           -73824.9, 195291, 195291, -nan)
reports[-1].sigmaresid = ValErr(0.353131, 0.00056504, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.060614, None, -0.000118422, None, -0.0604945, None, -9.65142e-05, None, -0.0604945, None, -9.65142e-05, None, -0.0587948, None, -0.000156524, None, -0.0587948, None, -0.000156524, None, 0.353139, None, 0.00780322, None, 0.353139, None, 0.00780322, None)
reports[-1].CovMatrix = ['6.54686e-07','-7.75643e-09','-2.06223e-09','1.16093e-10','0','0','0','0','0','-7.75643e-09','8.75031e-05','-5.26932e-10','1.58622e-09','0','0','0','0','0','-2.06223e-09','-5.26932e-10','2.63478e-10','2.36316e-12','0','0','0','0','0','1.16093e-10','1.58622e-09','2.36316e-12','3.1927e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 53069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0306207, 0.00457469, 0), \
                           ValErr(0.248654, 0.10004, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.29496e-05, 4.81491e-05, 0), \
                           -64959.8, 53069, 53069, -nan)
reports[-1].sigmaresid = ValErr(0.822938, 0.00252599, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0360906, None, 0.000374352, None, -0.0329807, None, 0.000618413, None, -0.0329807, None, 0.000618413, None, -0.0386946, None, 0.000691847, None, -0.0386946, None, 0.000691847, None, 0.822992, None, 0.00701514, None, 0.822992, None, 0.00701514, None)
reports[-1].CovMatrix = ['2.09278e-05','-9.29232e-06','-1.37549e-07','2.86687e-09','0','0','0','0','0','-9.29232e-06','0.010008','2.95489e-08','1.34062e-07','0','0','0','0','0','-1.37549e-07','2.95489e-08','2.31833e-09','3.19774e-11','0','0','0','0','0','2.86687e-09','1.34062e-07','3.19774e-11','6.38063e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 41463
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0473038, 0.00597311, 0), \
                           ValErr(-0.13544, 0.108214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00021951, 5.6931e-05, 0), \
                           -46791.3, 41463, 41463, -nan)
reports[-1].sigmaresid = ValErr(0.747941, 0.00257655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0254572, None, 0.000313462, None, -0.0295906, None, 0.000356471, None, -0.0295906, None, 0.000356471, None, -0.0304267, None, 0.000372162, None, -0.0304267, None, 0.000372162, None, 0.748101, None, 0.00642096, None, 0.748101, None, 0.00642096, None)
reports[-1].CovMatrix = ['3.56781e-05','-8.74462e-05','-2.67718e-07','1.57386e-07','0','0','0','0','0','-8.74462e-05','0.0117103','7.05971e-07','-1.73779e-06','0','0','0','0','0','-2.67718e-07','7.05971e-07','3.24114e-09','-1.55203e-09','0','0','0','0','0','1.57386e-07','-1.73779e-06','-1.55203e-09','6.63863e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 30933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0215941, 0.0084198, 0), \
                           ValErr(0.457293, 0.139674, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.34481e-05, 7.7335e-05, 0), \
                           -33619.6, 30933, 30933, -nan)
reports[-1].sigmaresid = ValErr(0.717426, 0.00288438, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.031477, None, 0.000355298, None, -0.0324909, None, 0.000350004, None, -0.0324909, None, 0.000350004, None, -0.0374556, None, 0.000311163, None, -0.0374556, None, 0.000311163, None, 0.717555, None, 0.00613251, None, 0.717555, None, 0.00613251, None)
reports[-1].CovMatrix = ['7.0893e-05','0.000244172','-5.64867e-07','6.32627e-09','0','0','0','0','0','0.000244172','0.0195088','-1.18839e-06','2.53577e-07','0','0','0','0','0','-5.64867e-07','-1.18839e-06','5.98071e-09','1.45917e-11','0','0','0','0','0','6.32627e-09','2.53577e-07','1.45917e-11','8.31963e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 56623
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0135014, 0.00423358, 0), \
                           ValErr(-0.109293, 0.0960988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000159876, 4.39361e-05, 0), \
                           -70707.1, 56623, 56623, -nan)
reports[-1].sigmaresid = ValErr(0.843493, 0.00250651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0248234, None, -0.000228829, None, -0.0219025, None, -0.000137283, None, -0.0219025, None, -0.000137283, None, -0.0202948, None, -0.000165898, None, -0.0202948, None, -0.000165898, None, 0.843604, None, 0.0068512, None, 0.843604, None, 0.0068512, None)
reports[-1].CovMatrix = ['1.79232e-05','9.25467e-06','-1.01698e-07','3.22401e-09','0','0','0','0','0','9.25467e-06','0.00923498','-1.46233e-07','1.2944e-07','0','0','0','0','0','-1.01698e-07','-1.46233e-07','1.93038e-09','3.08425e-11','0','0','0','0','0','3.22401e-09','1.2944e-07','3.08425e-11','6.28262e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 48049
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0148416, 0.00459595, 0), \
                           ValErr(0.16254, 0.101481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.85032e-05, 4.47919e-05, 0), \
                           -59591.1, 48049, 48049, -nan)
reports[-1].sigmaresid = ValErr(0.836337, 0.00269789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0171176, None, 2.06898e-05, None, 0.0179633, None, -0.000142057, None, 0.0179633, None, -0.000142057, None, 0.0292631, None, -0.000255871, None, 0.0292631, None, -0.000255871, None, 0.836375, None, 0.00719516, None, 0.836375, None, 0.00719516, None)
reports[-1].CovMatrix = ['2.11228e-05','1.91015e-05','-1.14612e-07','3.8924e-09','0','0','0','0','0','1.91015e-05','0.0102984','-9.46892e-08','1.52537e-07','0','0','0','0','0','-1.14612e-07','-9.46892e-08','2.00631e-09','3.34984e-11','0','0','0','0','0','3.8924e-09','1.52537e-07','3.34984e-11','7.27863e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 46263
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00735537, 0.00503512, 0), \
                           ValErr(0.292115, 0.106312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000189796, 5.04924e-05, 0), \
                           -56070.4, 46263, 46263, -nan)
reports[-1].sigmaresid = ValErr(0.813063, 0.00267296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0224081, None, 0.000184065, None, 0.0200149, None, 0.000123964, None, 0.0200149, None, 0.000123964, None, 0.0165395, None, 0.000102553, None, 0.0165395, None, 0.000102553, None, 0.813251, None, 0.00697998, None, 0.813251, None, 0.00697998, None)
reports[-1].CovMatrix = ['2.53524e-05','-1.04149e-05','-1.67917e-07','3.12961e-09','0','0','0','0','0','-1.04149e-05','0.0113023','6.31667e-08','1.51245e-07','0','0','0','0','0','-1.67917e-07','6.31667e-08','2.54948e-09','3.36612e-11','0','0','0','0','0','3.12961e-09','1.51245e-07','3.36612e-11','7.14471e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 57784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0418139, 0.00405432, 0), \
                           ValErr(-0.410216, 0.0992108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.45209e-05, 4.18115e-05, 0), \
                           -73606.2, 57784, 57784, -nan)
reports[-1].sigmaresid = ValErr(0.864918, 0.00254423, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0460615, None, -0.000162821, None, 0.0463368, None, -0.000244125, None, 0.0463368, None, -0.000244125, None, 0.0430999, None, -0.000240383, None, 0.0430999, None, -0.000240383, None, 0.865071, None, 0.00736497, None, 0.865071, None, 0.00736497, None)
reports[-1].CovMatrix = ['1.64375e-05','2.47071e-05','-7.77284e-08','3.82084e-09','0','0','0','0','0','2.47071e-05','0.00984278','-1.36158e-07','1.44272e-07','0','0','0','0','0','-7.77284e-08','-1.36158e-07','1.7482e-09','3.39734e-11','0','0','0','0','0','3.82084e-09','1.44272e-07','3.39734e-11','6.47312e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 58973
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0490412, 0.00403437, 0), \
                           ValErr(0.129433, 0.104661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.66555e-05, 4.21642e-05, 0), \
                           -75404.8, 58973, 58973, -nan)
reports[-1].sigmaresid = ValErr(0.869095, 0.00253062, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0501599, None, -0.000351081, None, 0.0525689, None, -0.000367398, None, 0.0525689, None, -0.000367398, None, 0.0444371, None, -0.000359717, None, 0.0444371, None, -0.000359717, None, 0.869122, None, 0.00713584, None, 0.869122, None, 0.00713584, None)
reports[-1].CovMatrix = ['1.62762e-05','-7.26085e-05','-7.36989e-08','2.65047e-09','0','0','0','0','0','-7.26085e-05','0.010954','1.29738e-07','1.25807e-07','0','0','0','0','0','-7.36989e-08','1.29738e-07','1.77782e-09','3.86266e-11','0','0','0','0','0','2.65047e-09','1.25807e-07','3.86266e-11','6.40404e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 59206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0828211, 0.00396875, 0), \
                           ValErr(-0.0223858, 0.0961419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000116527, 4.01664e-05, 0), \
                           -75234.7, 59206, 59206, -nan)
reports[-1].sigmaresid = ValErr(0.86225, 0.00249469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0864416, None, -0.0011077, None, 0.0879343, None, -0.00112435, None, 0.0879343, None, -0.00112435, None, 0.0905347, None, -0.00118879, None, 0.0905347, None, -0.00118879, None, 0.862309, None, 0.00707906, None, 0.862309, None, 0.00707906, None)
reports[-1].CovMatrix = ['1.5751e-05','-3.73453e-06','-7.26179e-08','8.05445e-09','0','0','0','0','0','-3.73453e-06','0.00924327','1.26764e-07','1.32667e-06','0','0','0','0','0','-7.26179e-08','1.26764e-07','1.61334e-09','-1.52073e-09','0','0','0','0','0','8.05445e-09','1.32667e-06','-1.52073e-09','6.22346e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 62781
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0748055, 0.00398813, 0), \
                           ValErr(0.305831, 0.106282, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000100542, 4.15727e-05, 0), \
                           -81690.9, 62781, 62781, -nan)
reports[-1].sigmaresid = ValErr(0.888934, 0.00250866, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.076197, None, 0.000290675, None, 0.081087, None, 0.000107168, None, 0.081087, None, 0.000107168, None, 0.0912271, None, 0.0001281, None, 0.0912271, None, 0.0001281, None, 0.889031, None, 0.0073547, None, 0.889031, None, 0.0073547, None)
reports[-1].CovMatrix = ['1.59052e-05','-8.89449e-05','-6.75462e-08','2.56733e-09','0','0','0','0','0','-8.89449e-05','0.0112959','3.56973e-08','1.20153e-07','0','0','0','0','0','-6.75462e-08','3.56973e-08','1.72829e-09','3.82519e-11','0','0','0','0','0','2.56733e-09','1.20153e-07','3.82519e-11','6.29337e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 51638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0421137, 0.00414565, 0), \
                           ValErr(-0.620126, 0.100597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.38465e-06, 4.35973e-05, 0), \
                           -66392.5, 51638, 51638, -nan)
reports[-1].sigmaresid = ValErr(0.875282, 0.00272364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0444107, None, 0.000354423, None, 0.0424024, None, 0.000513158, None, 0.0424024, None, 0.000513158, None, 0.0388659, None, 0.000494394, None, 0.0388659, None, 0.000494394, None, 0.875604, None, 0.00769232, None, 0.875604, None, 0.00769232, None)
reports[-1].CovMatrix = ['1.71865e-05','-7.04741e-07','-6.68191e-08','4.22273e-09','0','0','0','0','0','-7.04741e-07','0.0101198','1.15221e-07','1.56125e-07','0','0','0','0','0','-6.68191e-08','1.15221e-07','1.90072e-09','4.65923e-11','0','0','0','0','0','4.22273e-09','1.56125e-07','4.65923e-11','7.41819e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 56660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0284546, 0.00420904, 0), \
                           ValErr(-0.0863009, 0.0965674, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.96706e-05, 4.40605e-05, 0), \
                           -71481.5, 56660, 56660, -nan)
reports[-1].sigmaresid = ValErr(0.854405, 0.00253811, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0280075, None, -4.554e-05, None, 0.0274336, None, -1.16346e-05, None, 0.0274336, None, -1.16346e-05, None, 0.0295152, None, -5.11801e-05, None, 0.0295152, None, -5.11801e-05, None, 0.854411, None, 0.00699938, None, 0.854411, None, 0.00699938, None)
reports[-1].CovMatrix = ['1.7716e-05','-2.39999e-06','-9.68335e-08','3.24813e-09','0','0','0','0','0','-2.39999e-06','0.00932527','-3.75593e-08','1.31845e-07','0','0','0','0','0','-9.68335e-08','-3.75593e-08','1.94133e-09','3.37981e-11','0','0','0','0','0','3.24813e-09','1.31845e-07','3.37981e-11','6.44202e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 43585
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0118903, 0.00557585, 0), \
                           ValErr(0.0937257, 0.108619, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000180436, 5.51269e-05, 0), \
                           -51338, 43585, 43585, -nan)
reports[-1].sigmaresid = ValErr(0.785797, 0.0026615, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00163168, None, 0.000600859, None, 0.00135084, None, 0.000546407, None, 0.00135084, None, 0.000546407, None, -0.00352089, None, 0.00054695, None, -0.00352089, None, 0.00054695, None, 0.785905, None, 0.00640955, None, 0.785905, None, 0.00640955, None)
reports[-1].CovMatrix = ['3.10902e-05','5.42519e-05','-2.26541e-07','3.77879e-09','0','0','0','0','0','5.42519e-05','0.011798','-4.5445e-07','1.56965e-07','0','0','0','0','0','-2.26541e-07','-4.5445e-07','3.03898e-09','2.41933e-11','0','0','0','0','0','3.77879e-09','1.56965e-07','2.41933e-11','7.0836e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 45408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104773, 0.00475713, 0), \
                           ValErr(0.257677, 0.11094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.3824e-05, 4.89387e-05, 0), \
                           -57694.2, 45408, 45408, -nan)
reports[-1].sigmaresid = ValErr(0.862115, 0.00286078, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00145705, None, 0.000159437, None, -0.0010755, None, 5.09021e-06, None, -0.0010755, None, 5.09021e-06, None, -0.00278781, None, -1.7841e-05, None, -0.00278781, None, -1.7841e-05, None, 0.862171, None, 0.00714858, None, 0.862171, None, 0.00714858, None)
reports[-1].CovMatrix = ['2.26302e-05','7.60452e-05','-1.19826e-07','5.31732e-09','0','0','0','0','0','7.60452e-05','0.0123076','-3.7693e-07','1.91436e-07','0','0','0','0','0','-1.19826e-07','-3.7693e-07','2.395e-09','3.9068e-11','0','0','0','0','0','5.31732e-09','1.91436e-07','3.9068e-11','8.18404e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 60385
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0524492, 0.00389664, 0), \
                           ValErr(-0.0454691, 0.0950171, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000182633, 4.12297e-05, 0), \
                           -78144.2, 60385, 60385, -nan)
reports[-1].sigmaresid = ValErr(0.882645, 0.00241842, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0402758, None, -0.000342302, None, -0.0454179, None, -0.000291793, None, -0.0454179, None, -0.000291793, None, -0.0463851, None, -0.000359919, None, -0.0463851, None, -0.000359919, None, 0.882785, None, 0.00726072, None, 0.882785, None, 0.00726072, None)
reports[-1].CovMatrix = ['1.51838e-05','-4.57104e-05','-6.59893e-08','-5.43099e-07','0','0','0','0','0','-4.57104e-05','0.00902825','1.6017e-07','-1.57888e-05','0','0','0','0','0','-6.59893e-08','1.6017e-07','1.69989e-09','1.84945e-09','0','0','0','0','0','-5.43099e-07','-1.57888e-05','1.84945e-09','5.84875e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 54846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0048405, 0.00417396, 0), \
                           ValErr(0.0377737, 0.104342, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000114439, 4.34816e-05, 0), \
                           -71294.1, 54846, 54846, -nan)
reports[-1].sigmaresid = ValErr(0.887771, 0.00268049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.016657, None, 7.19524e-05, None, -0.009413, None, 1.88794e-05, None, -0.009413, None, 1.88794e-05, None, -0.0120584, None, 3.1136e-05, None, -0.0120584, None, 3.1136e-05, None, 0.887827, None, 0.00718824, None, 0.887827, None, 0.00718824, None)
reports[-1].CovMatrix = ['1.7422e-05','4.46383e-07','-7.58693e-08','3.98609e-09','0','0','0','0','0','4.46383e-07','0.0108872','-2.34615e-07','1.4721e-07','0','0','0','0','0','-7.58693e-08','-2.34615e-07','1.89065e-09','3.82688e-11','0','0','0','0','0','3.98609e-09','1.4721e-07','3.82688e-11','7.18502e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 63656
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0178056, 0.00385014, 0), \
                           ValErr(0.0660809, 0.093448, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.15171e-05, 4.06143e-05, 0), \
                           -81779.4, 63656, 63656, -nan)
reports[-1].sigmaresid = ValErr(0.874389, 0.00244878, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0215935, None, -0.000700325, None, -0.01992, None, -0.000489165, None, -0.01992, None, -0.000489165, None, -0.0201837, None, -0.000507116, None, -0.0201837, None, -0.000507116, None, 0.874403, None, 0.00717197, None, 0.874403, None, 0.00717197, None)
reports[-1].CovMatrix = ['1.48236e-05','4.25511e-06','-6.82175e-08','4.80434e-09','0','0','0','0','0','4.25511e-06','0.00873253','-1.62027e-07','-4.46521e-08','0','0','0','0','0','-6.82175e-08','-1.62027e-07','1.64952e-09','-3.35056e-12','0','0','0','0','0','4.80434e-09','-4.46521e-08','-3.35056e-12','5.9965e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 37943
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00385379, 0.00503212, 0), \
                           ValErr(-0.51624, 0.115636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000252083, 4.82835e-05, 0), \
                           -46046, 37943, 37943, -nan)
reports[-1].sigmaresid = ValErr(0.814336, 0.00295612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0185664, None, 0.000183495, None, -0.0117494, None, 0.000229225, None, -0.0117494, None, 0.000229225, None, -0.00519482, None, 0.00023143, None, -0.00519482, None, 0.00023143, None, 0.814817, None, 0.00656357, None, 0.814817, None, 0.00656357, None)
reports[-1].CovMatrix = ['2.53223e-05','-4.55171e-05','-1.34708e-07','3.67271e-09','0','0','0','0','0','-4.55171e-05','0.0133718','2.93707e-07','1.78504e-07','0','0','0','0','0','-1.34708e-07','2.93707e-07','2.33129e-09','4.50172e-11','0','0','0','0','0','3.67271e-09','1.78504e-07','4.50172e-11','8.73868e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 38683
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0383176, 0.00539851, 0), \
                           ValErr(0.0744762, 0.112426, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.54829e-05, 5.381e-05, 0), \
                           -45964.2, 38683, 38683, -nan)
reports[-1].sigmaresid = ValErr(0.793974, 0.00264689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0339896, None, 0.00167096, None, -0.0359347, None, 0.00157431, None, -0.0359347, None, 0.00157431, None, -0.0430704, None, 0.00170002, None, -0.0430704, None, 0.00170002, None, 0.793977, None, 0.00732283, None, 0.793977, None, 0.00732283, None)
reports[-1].CovMatrix = ['2.91439e-05','-2.37255e-05','-1.92909e-07','4.36645e-07','0','0','0','0','0','-2.37255e-05','0.0126397','2.88671e-07','3.0485e-05','0','0','0','0','0','-1.92909e-07','2.88671e-07','2.89551e-09','-5.58408e-09','0','0','0','0','0','4.36645e-07','3.0485e-05','-5.58408e-09','7.00602e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 25022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0369715, 0.00934642, 0), \
                           ValErr(0.434799, 0.131793, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.1312e-05, 7.88169e-05, 0), \
                           -26465.5, 25022, 25022, -nan)
reports[-1].sigmaresid = ValErr(0.696805, 0.00311484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.040081, None, 0.00128963, None, -0.0376287, None, 0.00125905, None, -0.0376287, None, 0.00125905, None, -0.0413384, None, 0.00129114, None, -0.0413384, None, 0.00129114, None, 0.696958, None, 0.00661092, None, 0.696958, None, 0.00661092, None)
reports[-1].CovMatrix = ['8.73556e-05','-6.82676e-05','-6.49587e-07','2.78926e-09','0','0','0','0','0','-6.82676e-05','0.0173695','4.5315e-07','2.01e-07','0','0','0','0','0','-6.49587e-07','4.5315e-07','6.21211e-09','3.66425e-11','0','0','0','0','0','2.78926e-09','2.01e-07','3.66425e-11','9.70223e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 41709
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0392778, 0.00564554, 0), \
                           ValErr(0.00749621, 0.109125, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.20456e-05, 5.6181e-05, 0), \
                           -48141.4, 41709, 41709, -nan)
reports[-1].sigmaresid = ValErr(0.76742, 0.00265706, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0338879, None, 0.000454021, None, -0.0354822, None, 0.00041057, None, -0.0354822, None, 0.00041057, None, -0.036497, None, 0.000422733, None, -0.036497, None, 0.000422733, None, 0.76743, None, 0.00717482, None, 0.76743, None, 0.00717482, None)
reports[-1].CovMatrix = ['3.18721e-05','0.000105545','-2.35302e-07','4.51213e-09','0','0','0','0','0','0.000105545','0.0119082','-7.49578e-07','1.577e-07','0','0','0','0','0','-2.35302e-07','-7.49578e-07','3.15631e-09','1.89551e-11','0','0','0','0','0','4.51213e-09','1.577e-07','1.89551e-11','7.05998e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 51982
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.005247, 0.00414588, 0), \
                           ValErr(-0.0672233, 0.102315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.93387e-05, 4.13834e-05, 0), \
                           -65150, 51982, 51982, -nan)
reports[-1].sigmaresid = ValErr(0.847371, 0.00259867, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00289661, None, -0.000307639, None, -0.00315409, None, -0.000631844, None, -0.00315409, None, -0.000631844, None, -0.00850061, None, -0.000735649, None, -0.00850061, None, -0.000735649, None, 0.847384, None, 0.00847041, None, 0.847384, None, 0.00847041, None)
reports[-1].CovMatrix = ['1.71883e-05','-1.37944e-05','-7.61871e-08','-3.08671e-08','0','0','0','0','0','-1.37944e-05','0.0104684','8.48789e-08','-4.82011e-06','0','0','0','0','0','-7.61871e-08','8.48789e-08','1.71258e-09','2.15735e-09','0','0','0','0','0','-3.08671e-08','-4.82011e-06','2.15735e-09','6.75307e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 56475
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0188385, 0.00414472, 0), \
                           ValErr(-0.0809643, 0.0978462, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.42146e-05, 4.31987e-05, 0), \
                           -71137.8, 56475, 56475, -nan)
reports[-1].sigmaresid = ValErr(0.852739, 0.00253731, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0141616, None, 0.000360346, None, 0.0200462, None, 0.000632572, None, 0.0200462, None, 0.000632572, None, 0.0200947, None, 0.000628782, None, 0.0200947, None, 0.000628782, None, 0.852745, None, 0.00794898, None, 0.852745, None, 0.00794898, None)
reports[-1].CovMatrix = ['1.71787e-05','-2.07765e-06','-8.95759e-08','3.34096e-09','0','0','0','0','0','-2.07765e-06','0.00957387','1.57085e-07','1.46982e-07','0','0','0','0','0','-8.95759e-08','1.57085e-07','1.86613e-09','3.66114e-11','0','0','0','0','0','3.34096e-09','1.46982e-07','3.66114e-11','6.43796e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 44188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0337316, 0.00491737, 0), \
                           ValErr(-0.0114622, 0.105399, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000118184, 5.00868e-05, 0), \
                           -52864.2, 44188, 44188, -nan)
reports[-1].sigmaresid = ValErr(0.800443, 0.00268862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0396092, None, 0.000373117, None, 0.0410954, None, 0.000570613, None, 0.0410954, None, 0.000570613, None, 0.0436768, None, 0.000525828, None, 0.0436768, None, 0.000525828, None, 0.800492, None, 0.00770704, None, 0.800492, None, 0.00770704, None)
reports[-1].CovMatrix = ['2.41805e-05','4.28551e-05','-1.56991e-07','-5.21676e-08','0','0','0','0','0','4.28551e-05','0.011109','-4.87642e-07','-4.00632e-07','0','0','0','0','0','-1.56991e-07','-4.87642e-07','2.50868e-09','-3.82003e-11','0','0','0','0','0','-5.21676e-08','-4.00632e-07','-3.82003e-11','7.22867e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 68816
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0570807, 0.0035368, 0), \
                           ValErr(0.0569122, 0.0731388, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.82732e-05, 3.88321e-05, 0), \
                           -89008.2, 68816, 68816, -nan)
reports[-1].sigmaresid = ValErr(0.882045, 0.00231683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0544924, None, -0.00126776, None, 0.0556837, None, -0.00113344, None, 0.0556837, None, -0.00113344, None, 0.0590109, None, -0.00122713, None, 0.0590109, None, -0.00122713, None, 0.882051, None, 0.00786683, None, 0.882051, None, 0.00786683, None)
reports[-1].CovMatrix = ['1.2509e-05','-4.92343e-05','-5.80584e-08','4.94285e-07','0','0','0','0','0','-4.92343e-05','0.00534928','-7.10167e-08','2.62997e-05','0','0','0','0','0','-5.80584e-08','-7.10167e-08','1.50793e-09','6.74095e-10','0','0','0','0','0','4.94285e-07','2.62997e-05','6.74095e-10','5.36768e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 61873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0561494, 0.00383519, 0), \
                           ValErr(-0.0374924, 0.053194, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.68425e-05, 3.97967e-05, 0), \
                           -80671.5, 61873, 61873, -nan)
reports[-1].sigmaresid = ValErr(0.891263, 0.00252474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0582795, None, -0.000400711, None, 0.0590553, None, -0.000320401, None, 0.0590553, None, -0.000320401, None, 0.0611156, None, -0.000376279, None, 0.0611156, None, -0.000376279, None, 0.8913, None, 0.00785771, None, 0.8913, None, 0.00785771, None)
reports[-1].CovMatrix = ['1.47086e-05','-1.35517e-05','-5.4367e-08','1.66243e-08','0','0','0','0','0','-1.35517e-05','0.0028296','2.93776e-07','6.03782e-06','0','0','0','0','0','-5.4367e-08','2.93776e-07','1.58378e-09','-8.62584e-10','0','0','0','0','0','1.66243e-08','6.03782e-06','-8.62584e-10','6.37429e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 55451
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0746739, 0.00412792, 0), \
                           ValErr(-0.318973, 0.0966776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000132615, 4.33053e-05, 0), \
                           -70067.8, 55451, 55451, -nan)
reports[-1].sigmaresid = ValErr(0.856125, 0.00256843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0808614, None, 0.000815992, None, 0.0814505, None, 0.000905635, None, 0.0814505, None, 0.000905635, None, 0.0879331, None, 0.000902204, None, 0.0879331, None, 0.000902204, None, 0.856278, None, 0.00762796, None, 0.856278, None, 0.00762796, None)
reports[-1].CovMatrix = ['1.70398e-05','2.75876e-05','-8.4302e-08','-9.81076e-09','0','0','0','0','0','2.75876e-05','0.00934656','-6.21198e-08','-1.90616e-08','0','0','0','0','0','-8.4302e-08','-6.21198e-08','1.87535e-09','-1.21377e-10','0','0','0','0','0','-9.81076e-09','-1.90616e-08','-1.21377e-10','6.59682e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 56162
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0343947, 0.003973, 0), \
                           ValErr(-0.160249, 0.0551217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109176, 4.29484e-05, 0), \
                           -74537, 56162, 56162, -nan)
reports[-1].sigmaresid = ValErr(0.912323, 0.00271841, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0393675, None, 0.000878061, None, 0.0371753, None, 0.000851603, None, 0.0371753, None, 0.000851603, None, 0.0431056, None, 0.000812544, None, 0.0431056, None, 0.000812544, None, 0.912399, None, 0.00848109, None, 0.912399, None, 0.00848109, None)
reports[-1].CovMatrix = ['1.57848e-05','-3.3591e-05','-4.6242e-08','3.07927e-08','0','0','0','0','0','-3.3591e-05','0.00303841','8.26668e-08','5.58177e-06','0','0','0','0','0','-4.6242e-08','8.26668e-08','1.84456e-09','-3.20168e-10','0','0','0','0','0','3.07927e-08','5.58177e-06','-3.20168e-10','7.38973e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 55023
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00342483, 0.00420094, 0), \
                           ValErr(-0.283633, 0.0989047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000122705, 4.39678e-05, 0), \
                           -69600.9, 55023, 55023, -nan)
reports[-1].sigmaresid = ValErr(0.857276, 0.00258425, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00999985, None, 0.000627234, None, 0.00909033, None, 0.000640687, None, 0.00909033, None, 0.000640687, None, 0.0123725, None, 0.000599141, None, 0.0123725, None, 0.000599141, None, 0.857404, None, 0.00794189, None, 0.857404, None, 0.00794189, None)
reports[-1].CovMatrix = ['1.76479e-05','-9.32881e-06','-9.10652e-08','3.34896e-09','0','0','0','0','0','-9.32881e-06','0.00978213','1.16535e-07','1.40987e-07','0','0','0','0','0','-9.10652e-08','1.16535e-07','1.93317e-09','3.79155e-11','0','0','0','0','0','3.34896e-09','1.40987e-07','3.79155e-11','6.67833e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 53861
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0121864, 0.00437272, 0), \
                           ValErr(-0.107846, 0.0973609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.91258e-05, 4.61747e-05, 0), \
                           -65449.4, 53861, 53861, -nan)
reports[-1].sigmaresid = ValErr(0.815638, 0.00248511, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0146527, None, 0.000334631, None, 0.0164851, None, 0.000381911, None, 0.0164851, None, 0.000381911, None, 0.0204602, None, 0.00034462, None, 0.0204602, None, 0.00034462, None, 0.815673, None, 0.00783531, None, 0.815673, None, 0.00783531, None)
reports[-1].CovMatrix = ['1.91207e-05','-3.36175e-05','-1.20002e-07','2.48456e-09','0','0','0','0','0','-3.36175e-05','0.00947915','3.85607e-07','1.31666e-07','0','0','0','0','0','-1.20002e-07','3.85607e-07','2.13211e-09','3.65138e-11','0','0','0','0','0','2.48456e-09','1.31666e-07','3.65138e-11','6.17577e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 44703
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0303765, 0.00457236, 0), \
                           ValErr(0.381942, 0.105708, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000124287, 4.53598e-05, 0), \
                           -54142.6, 44703, 44703, -nan)
reports[-1].sigmaresid = ValErr(0.812389, 0.00271695, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0235743, None, -7.64812e-05, None, 0.0245541, None, -1.84938e-05, None, 0.0245541, None, -1.84938e-05, None, 0.0192465, None, -5.1036e-05, None, 0.0192465, None, -5.1036e-05, None, 0.812572, None, 0.00768174, None, 0.812572, None, 0.00768174, None)
reports[-1].CovMatrix = ['2.09064e-05','-2.11154e-05','-1.11791e-07','3.37153e-09','0','0','0','0','0','-2.11154e-05','0.0111741','-1.21944e-07','1.42063e-07','0','0','0','0','0','-1.11791e-07','-1.21944e-07','2.05751e-09','3.45423e-11','0','0','0','0','0','3.37153e-09','1.42063e-07','3.45423e-11','7.3818e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 66889
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0404008, 0.0037467, 0), \
                           ValErr(-0.0143077, 0.0513817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000204052, 3.94635e-05, 0), \
                           -85974.7, 66889, 66889, -nan)
reports[-1].sigmaresid = ValErr(0.874936, 0.00239209, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0303428, None, 0.000292917, None, -0.0320888, None, 0.000319768, None, -0.0320888, None, 0.000319768, None, -0.0348995, None, 0.000283432, None, -0.0348995, None, 0.000283432, None, 0.875112, None, 0.00829199, None, 0.875112, None, 0.00829199, None)
reports[-1].CovMatrix = ['1.40377e-05','6.07207e-06','-6.33677e-08','-2.30293e-09','0','0','0','0','0','6.07207e-06','0.00264008','-8.1118e-08','1.24252e-06','0','0','0','0','0','-6.33677e-08','-8.1118e-08','1.55737e-09','4.6244e-11','0','0','0','0','0','-2.30293e-09','1.24252e-06','4.6244e-11','5.72211e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 39430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0398428, 0.00477059, 0), \
                           ValErr(-0.292413, 0.112364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000190714, 4.74427e-05, 0), \
                           -49921.5, 39430, 39430, -nan)
reports[-1].sigmaresid = ValErr(0.858251, 0.00305623, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0546042, None, 0.000274761, None, -0.0475003, None, 0.000428777, None, -0.0475003, None, 0.000428777, None, -0.0492417, None, 0.00043529, None, -0.0492417, None, 0.00043529, None, 0.858505, None, 0.00776117, None, 0.858505, None, 0.00776117, None)
reports[-1].CovMatrix = ['2.27585e-05','2.39553e-05','-9.54978e-08','5.46802e-09','0','0','0','0','0','2.39553e-05','0.0126256','-1.40779e-07','1.93289e-07','0','0','0','0','0','-9.54978e-08','-1.40779e-07','2.25081e-09','4.84106e-11','0','0','0','0','0','5.46802e-09','1.93289e-07','4.84106e-11','9.34058e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 60066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0347358, 0.00391142, 0), \
                           ValErr(-0.142928, 0.0942885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.28411e-06, 4.15815e-05, 0), \
                           -77635.2, 60066, 60066, -nan)
reports[-1].sigmaresid = ValErr(0.881228, 0.00254162, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0332771, None, -0.000162119, None, -0.034295, None, -6.43691e-05, None, -0.034295, None, -6.43691e-05, None, -0.0305855, None, -9.41096e-05, None, -0.0305855, None, -9.41096e-05, None, 0.881245, None, 0.00776111, None, 0.881245, None, 0.00776111, None)
reports[-1].CovMatrix = ['1.52992e-05','9.72073e-07','-6.39993e-08','-3.94312e-09','0','0','0','0','0','9.72073e-07','0.00889031','1.40583e-07','-4.50858e-08','0','0','0','0','0','-6.39993e-08','1.40583e-07','1.72902e-09','1.2101e-10','0','0','0','0','0','-3.94312e-09','-4.50858e-08','1.2101e-10','6.45983e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 51292
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0268613, 0.00427877, 0), \
                           ValErr(-0.0590973, 0.0588865, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127928, 4.38177e-05, 0), \
                           -66963, 51292, 51292, -nan)
reports[-1].sigmaresid = ValErr(0.89278, 0.00278389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0326986, None, 7.5951e-05, None, -0.0317707, None, 0.000149018, None, -0.0317707, None, 0.000149018, None, -0.0383045, None, 0.000175961, None, -0.0383045, None, 0.000175961, None, 0.892857, None, 0.00809586, None, 0.892857, None, 0.00809586, None)
reports[-1].CovMatrix = ['1.83079e-05','-1.27248e-05','-7.31054e-08','6.40041e-09','0','0','0','0','0','-1.27248e-05','0.00346762','1.19508e-07','5.21522e-06','0','0','0','0','0','-7.31054e-08','1.19508e-07','1.92e-09','2.41451e-10','0','0','0','0','0','6.40041e-09','5.21522e-06','2.41451e-10','7.75006e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 38653
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0232869, 0.00516648, 0), \
                           ValErr(0.216773, 0.114234, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.86413e-05, 5.48475e-05, 0), \
                           -46858.8, 38653, 38653, -nan)
reports[-1].sigmaresid = ValErr(0.81331, 0.00292516, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0350059, None, 0.000716568, None, -0.0288588, None, 0.000777044, None, -0.0288588, None, 0.000777044, None, -0.0324483, None, 0.000799149, None, -0.0324483, None, 0.000799149, None, 0.813378, None, 0.00731586, None, 0.813378, None, 0.00731586, None)
reports[-1].CovMatrix = ['2.66925e-05','1.65428e-05','-1.68959e-07','4.31146e-09','0','0','0','0','0','1.65428e-05','0.0130494','3.14057e-07','1.97965e-07','0','0','0','0','0','-1.68959e-07','3.14057e-07','3.00825e-09','4.79402e-11','0','0','0','0','0','4.31146e-09','1.97965e-07','4.79402e-11','8.55657e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 156407
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0633812, 0.00113098, 0), \
                           ValErr(-0.00630218, 0.0129949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.25128e-05, 2.58127e-05, 0), \
                           -95646.5, 156407, 156407, -nan)
reports[-1].sigmaresid = ValErr(0.446008, 0.000797439, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0622212, None, -0.000619358, None, 0.0633296, None, -0.000669957, None, 0.0633296, None, -0.000669957, None, 0.0625665, None, -0.000724954, None, 0.0625665, None, -0.000724954, None, 0.44601, None, 0.00813829, None, 0.44601, None, 0.00813829, None)
reports[-1].CovMatrix = ['1.27911e-06','-2.9538e-07','-2.12269e-09','3.1514e-10','0','0','0','0','0','-2.9538e-07','0.000168867','-1.13472e-10','3.88223e-09','0','0','0','0','0','-2.12269e-09','-1.13472e-10','6.66296e-10','7.35189e-12','0','0','0','0','0','3.1514e-10','3.88223e-09','7.35189e-12','6.3591e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 141358
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0373548, 0.00119118, 0), \
                           ValErr(-0.044501, 0.0135716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.29828e-05, 2.80483e-05, 0), \
                           -85098.5, 141358, 141358, -nan)
reports[-1].sigmaresid = ValErr(0.441785, 0.000830876, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0379492, None, -0.000419606, None, 0.0378764, None, -0.000518658, None, 0.0378764, None, -0.000518658, None, 0.0389332, None, -0.000600298, None, 0.0389332, None, -0.000600298, None, 0.441813, None, 0.00828383, None, 0.441813, None, 0.00828383, None)
reports[-1].CovMatrix = ['1.41892e-06','2.04997e-08','-5.48177e-09','3.16003e-10','0','0','0','0','0','2.04997e-08','0.000184189','4.38958e-09','4.32854e-09','0','0','0','0','0','-5.48177e-09','4.38958e-09','7.86705e-10','7.61359e-12','0','0','0','0','0','3.16003e-10','4.32854e-09','7.61359e-12','6.90354e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 151116
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0212845, 0.00114739, 0), \
                           ValErr(-0.0264568, 0.0131505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000101947, 2.62306e-05, 0), \
                           -92274.8, 151116, 151116, -nan)
reports[-1].sigmaresid = ValErr(0.445608, 0.000810555, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0216497, None, -4.04255e-05, None, -0.0210811, None, -8.0444e-05, None, -0.0210811, None, -8.0444e-05, None, -0.0246762, None, -0.000146458, None, -0.0246762, None, -0.000146458, None, 0.445636, None, 0.00811387, None, 0.445636, None, 0.00811387, None)
reports[-1].CovMatrix = ['1.31651e-06','6.52357e-08','-1.30998e-09','3.41153e-10','0','0','0','0','0','6.52357e-08','0.000172936','-2.07113e-09','4.05848e-09','0','0','0','0','0','-1.30998e-09','-2.07113e-09','6.88042e-10','7.71499e-12','0','0','0','0','0','3.41153e-10','4.05848e-09','7.71499e-12','6.56999e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 102734
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0670739, 0.00138659, 0), \
                           ValErr(-0.0184046, 0.0139044, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.44249e-05, 3.18696e-05, 0), \
                           -62403.4, 102734, 102734, -nan)
reports[-1].sigmaresid = ValErr(0.444186, 0.000979922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0648487, None, -0.000773056, None, -0.0669392, None, -0.000805464, None, -0.0669392, None, -0.000805464, None, -0.0659481, None, -0.000942372, None, -0.0659481, None, -0.000942372, None, 0.444205, None, 0.00846384, None, 0.444205, None, 0.00846384, None)
reports[-1].CovMatrix = ['1.92264e-06','1.94022e-07','-1.41121e-09','5.04203e-10','0','0','0','0','0','1.94022e-07','0.000193331','-7.07423e-09','5.13991e-09','0','0','0','0','0','-1.41121e-09','-7.07423e-09','1.01567e-09','1.1317e-11','0','0','0','0','0','5.04203e-10','5.13991e-09','1.1317e-11','9.60247e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 145662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0895731, 0.00116117, 0), \
                           ValErr(-0.0187534, 0.0133812, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.8565e-06, 2.6732e-05, 0), \
                           -87800.1, 145662, 145662, -nan)
reports[-1].sigmaresid = ValErr(0.442121, 0.000819129, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0888377, None, -0.000200952, None, -0.0896297, None, -0.000230914, None, -0.0896297, None, -0.000230914, None, -0.0897729, None, -0.000284442, None, -0.0897729, None, -0.000284442, None, 0.442124, None, 0.0080222, None, 0.442124, None, 0.0080222, None)
reports[-1].CovMatrix = ['1.34831e-06','-4.2947e-07','-1.96568e-09','3.28352e-10','0','0','0','0','0','-4.2947e-07','0.000179058','5.61601e-09','4.10126e-09','0','0','0','0','0','-1.96568e-09','5.61601e-09','7.14598e-10','7.88661e-12','0','0','0','0','0','3.28352e-10','4.10126e-09','7.88661e-12','6.70973e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 152552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.074914, 0.00113449, 0), \
                           ValErr(-0.0119436, 0.0130031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.69693e-05, 2.59157e-05, 0), \
                           -91853.2, 152552, 152552, -nan)
reports[-1].sigmaresid = ValErr(0.44183, 0.000799889, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0748472, None, -0.000172868, None, -0.0750024, None, -0.000218492, None, -0.0750024, None, -0.000218492, None, -0.0756507, None, -0.000263954, None, -0.0756507, None, -0.000263954, None, 0.441834, None, 0.00811765, None, 0.441834, None, 0.00811765, None)
reports[-1].CovMatrix = ['1.28708e-06','9.04725e-09','-2.23306e-09','3.17304e-10','0','0','0','0','0','9.04725e-09','0.000169079','6.55758e-10','3.94921e-09','0','0','0','0','0','-2.23306e-09','6.55758e-10','6.71625e-10','7.22329e-12','0','0','0','0','0','3.17304e-10','3.94921e-09','7.22329e-12','6.39822e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 162881
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0274265, 0.00110045, 0), \
                           ValErr(0.0304279, 0.0126572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28229e-05, 2.50827e-05, 0), \
                           -98268.7, 162881, 162881, -nan)
reports[-1].sigmaresid = ValErr(0.442364, 0.000775049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.028244, None, 0.000329546, None, -0.0273476, None, 0.000277656, None, -0.0273476, None, 0.000277656, None, -0.0265817, None, 0.000273682, None, -0.0265817, None, 0.000273682, None, 0.442373, None, 0.0078465, None, 0.442373, None, 0.0078465, None)
reports[-1].CovMatrix = ['1.21098e-06','5.67346e-08','-2.4529e-09','2.97395e-10','0','0','0','0','0','5.67346e-08','0.000160204','-1.18666e-09','3.7173e-09','0','0','0','0','0','-2.4529e-09','-1.18666e-09','6.29142e-10','6.71056e-12','0','0','0','0','0','2.97395e-10','3.7173e-09','6.71056e-12','6.00701e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 148414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0064788, 0.00116598, 0), \
                           ValErr(0.0845238, 0.0134776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.42591e-05, 2.69472e-05, 0), \
                           -91335.5, 148414, 148414, -nan)
reports[-1].sigmaresid = ValErr(0.447746, 0.000821825, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00712126, None, 0.00061685, None, 0.00709283, None, 0.000634145, None, 0.00709283, None, 0.000634145, None, 0.00799993, None, 0.000678605, None, 0.00799993, None, 0.000678605, None, 0.447812, None, 0.00823333, None, 0.447812, None, 0.00823333, None)
reports[-1].CovMatrix = ['1.3595e-06','-1.22144e-06','-4.38877e-10','3.3406e-10','0','0','0','0','0','-1.22144e-06','0.000181645','-2.35579e-08','3.65577e-09','0','0','0','0','0','-4.38877e-10','-2.35579e-08','7.26151e-10','7.82814e-12','0','0','0','0','0','3.3406e-10','3.65577e-09','7.82814e-12','6.75397e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 156792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0503932, 0.001124, 0), \
                           ValErr(0.0288559, 0.0129488, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.08005e-05, 2.57098e-05, 0), \
                           -94992.1, 156792, 156792, -nan)
reports[-1].sigmaresid = ValErr(0.443485, 0.000791958, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0493584, None, -7.95493e-05, None, 0.0505111, None, -9.43515e-05, None, 0.0505111, None, -9.43515e-05, None, 0.0514637, None, -0.00012561, None, 0.0514637, None, -0.00012561, None, 0.443493, None, 0.00790298, None, 0.443493, None, 0.00790298, None)
reports[-1].CovMatrix = ['1.26338e-06','-2.38189e-07','-2.38782e-09','3.04316e-10','0','0','0','0','0','-2.38189e-07','0.000167671','-1.88077e-09','3.80865e-09','0','0','0','0','0','-2.38782e-09','-1.88077e-09','6.60992e-10','7.08961e-12','0','0','0','0','0','3.04316e-10','3.80865e-09','7.08961e-12','6.27198e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 155387
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0581225, 0.00118096, 0), \
                           ValErr(-0.0322266, 0.0136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00295e-05, 2.75827e-05, 0), \
                           -101415, 155387, 155387, -nan)
reports[-1].sigmaresid = ValErr(0.464739, 0.000833655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0577612, None, -0.000118471, None, 0.0581939, None, -0.000168263, None, 0.0581939, None, -0.000168263, None, 0.0596247, None, -0.000190374, None, 0.0596247, None, -0.000190374, None, 0.464749, None, 0.00756377, None, 0.464749, None, 0.00756377, None)
reports[-1].CovMatrix = ['1.39466e-06','-1.84745e-08','-1.89107e-09','3.6593e-10','0','0','0','0','0','-1.84745e-08','0.000184959','4.14149e-11','4.46516e-09','0','0','0','0','0','-1.89107e-09','4.14149e-11','7.60805e-10','8.55899e-12','0','0','0','0','0','3.6593e-10','4.46516e-09','8.55899e-12','6.94981e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 154347
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0103948, 0.0011781, 0), \
                           ValErr(-0.165766, 0.0135907, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.69963e-05, 2.732e-05, 0), \
                           -99742.5, 154347, 154347, -nan)
reports[-1].sigmaresid = ValErr(0.461757, 0.000831093, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.011621, None, -0.000228211, None, 0.0107237, None, -0.00029846, None, 0.0107237, None, -0.00029846, None, 0.0102768, None, -0.000371754, None, 0.0102768, None, -0.000371754, None, 0.461995, None, 0.00778928, None, 0.461995, None, 0.00778928, None)
reports[-1].CovMatrix = ['1.38791e-06','7.77666e-08','-2.19298e-09','3.60602e-10','0','0','0','0','0','7.77666e-08','0.000184708','1.28826e-09','4.47326e-09','0','0','0','0','0','-2.19298e-09','1.28826e-09','7.46382e-10','8.35348e-12','0','0','0','0','0','3.60602e-10','4.47326e-09','8.35348e-12','6.90716e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 145092
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0556893, 0.00120923, 0), \
                           ValErr(-0.0264869, 0.013874, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.40845e-05, 2.836e-05, 0), \
                           -93316.2, 145092, 145092, -nan)
reports[-1].sigmaresid = ValErr(0.460342, 0.000854562, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.054323, None, -0.000221574, None, -0.0557345, None, -0.000265284, None, -0.0557345, None, -0.000265284, None, -0.0542256, None, -0.000308436, None, -0.0542256, None, -0.000308436, None, 0.46035, None, 0.00769995, None, 0.46035, None, 0.00769995, None)
reports[-1].CovMatrix = ['1.46224e-06','3.34636e-08','-1.16467e-09','3.91629e-10','0','0','0','0','0','3.34636e-08','0.000192489','-2.53426e-09','4.61945e-09','0','0','0','0','0','-1.16467e-09','-2.53426e-09','8.04291e-10','9.1014e-12','0','0','0','0','0','3.91629e-10','4.61945e-09','9.1014e-12','7.30276e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 145588
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0778949, 0.00120748, 0), \
                           ValErr(-0.00257191, 0.0138934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.09933e-05, 2.83613e-05, 0), \
                           -93604.5, 145588, 145588, -nan)
reports[-1].sigmaresid = ValErr(0.460245, 0.000852925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0772466, None, -0.000400046, None, -0.0777178, None, -0.000401152, None, -0.0777178, None, -0.000401152, None, -0.0780803, None, -0.000470214, None, -0.0780803, None, -0.000470214, None, 0.460261, None, 0.00775085, None, 0.460261, None, 0.00775085, None)
reports[-1].CovMatrix = ['1.45801e-06','8.18126e-08','-1.55613e-09','3.87163e-10','0','0','0','0','0','8.18126e-08','0.000193025','-1.27281e-10','4.65881e-09','0','0','0','0','0','-1.55613e-09','-1.27281e-10','8.04366e-10','9.04914e-12','0','0','0','0','0','3.87163e-10','4.65881e-09','9.04914e-12','7.27481e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 152913
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0873021, 0.00117596, 0), \
                           ValErr(0.0282172, 0.0135982, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.6219e-05, 2.73036e-05, 0), \
                           -97626.6, 152913, 152913, -nan)
reports[-1].sigmaresid = ValErr(0.45818, 0.000828512, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0868787, None, -0.000347357, None, -0.0875127, None, -0.000418934, None, -0.0875127, None, -0.000418934, None, -0.0865355, None, -0.000447004, None, -0.0865355, None, -0.000447004, None, 0.458193, None, 0.00777712, None, 0.458193, None, 0.00777712, None)
reports[-1].CovMatrix = ['1.38288e-06','1.79549e-08','-2.73229e-09','3.49565e-10','0','0','0','0','0','1.79549e-08','0.000184911','3.08176e-09','4.44151e-09','0','0','0','0','0','-2.73229e-09','3.08176e-09','7.45485e-10','8.18293e-12','0','0','0','0','0','3.49565e-10','4.44151e-09','8.18293e-12','6.86432e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 152986
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0628841, 0.0011762, 0), \
                           ValErr(0.0193758, 0.0139122, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.81809e-05, 2.71395e-05, 0), \
                           -97144.6, 152986, 152986, -nan)
reports[-1].sigmaresid = ValErr(0.456599, 0.000825456, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0623968, None, 0.000560289, None, -0.0629182, None, 0.000449309, None, -0.0629182, None, 0.000449309, None, -0.0631079, None, 0.000462961, None, -0.0631079, None, 0.000462961, None, 0.456604, None, 0.00775122, None, 0.456604, None, 0.00775122, None)
reports[-1].CovMatrix = ['1.38346e-06','-9.7568e-07','-3.42677e-09','3.1661e-10','0','0','0','0','0','-9.7568e-07','0.000193548','3.49652e-09','4.2326e-09','0','0','0','0','0','-3.42677e-09','3.49652e-09','7.36553e-10','7.85084e-12','0','0','0','0','0','3.1661e-10','4.2326e-09','7.85084e-12','6.81378e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 162166
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00436872, 0.00113794, 0), \
                           ValErr(0.0158337, 0.0131372, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.5223e-05, 2.62344e-05, 0), \
                           -102340, 162166, 162166, -nan)
reports[-1].sigmaresid = ValErr(0.454818, 0.000798624, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00520386, None, 0.000132181, None, -0.00417504, None, 0.0001009, None, -0.00417504, None, 0.0001009, None, -0.00546958, None, 8.50586e-05, None, -0.00546958, None, 8.50586e-05, None, 0.454822, None, 0.00759513, None, 0.454822, None, 0.00759513, None)
reports[-1].CovMatrix = ['1.2949e-06','-7.9127e-08','-3.6414e-09','3.09811e-10','0','0','0','0','0','-7.9127e-08','0.000172586','-1.26905e-10','4.04222e-09','0','0','0','0','0','-3.6414e-09','-1.26905e-10','6.88242e-10','7.18126e-12','0','0','0','0','0','3.09811e-10','4.04222e-09','7.18126e-12','6.37801e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 159689
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0376442, 0.00115127, 0), \
                           ValErr(0.0145699, 0.0133161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000110896, 2.64639e-05, 0), \
                           -101647, 159689, 159689, -nan)
reports[-1].sigmaresid = ValErr(0.457303, 0.00080919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0385142, None, 0.000353636, None, 0.0381576, None, 0.000392297, None, 0.0381576, None, 0.000392297, None, 0.0378248, None, 0.000422919, None, 0.0378248, None, 0.000422919, None, 0.457331, None, 0.00758921, None, 0.457331, None, 0.00758921, None)
reports[-1].CovMatrix = ['1.32543e-06','1.50887e-07','-3.31991e-09','3.29909e-10','0','0','0','0','0','1.50887e-07','0.000177318','-2.29939e-09','4.20959e-09','0','0','0','0','0','-3.31991e-09','-2.29939e-09','7.0034e-10','7.4586e-12','0','0','0','0','0','3.29909e-10','4.20959e-09','7.4586e-12','6.54789e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 162420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0648732, 0.00114285, 0), \
                           ValErr(-0.0227401, 0.0132567, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.61953e-06, 2.64345e-05, 0), \
                           -103624, 162420, 162420, -nan)
reports[-1].sigmaresid = ValErr(0.457977, 0.000803542, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0656238, None, 0.000165249, None, 0.0648442, None, 0.000147607, None, 0.0648442, None, 0.000147607, None, 0.0649402, None, 0.000111295, None, 0.0649402, None, 0.000111295, None, 0.457981, None, 0.00778748, None, 0.457981, None, 0.00778748, None)
reports[-1].CovMatrix = ['1.3061e-06','1.17346e-07','-3.20055e-09','3.24969e-10','0','0','0','0','0','1.17346e-07','0.00017574','1.63421e-10','4.18566e-09','0','0','0','0','0','-3.20055e-09','1.63421e-10','6.98781e-10','7.48714e-12','0','0','0','0','0','3.24969e-10','4.18566e-09','7.48714e-12','6.4568e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 58822
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0511118, 0.00432663, 0), \
                           ValErr(0.0886177, 0.0985553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.8193e-05, 4.65518e-05, 0), \
                           -75198.6, 58822, 58822, -nan)
reports[-1].sigmaresid = ValErr(0.8689, 0.0025333, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0577422, None, 1.48773e-05, None, 0.0525294, None, -9.82682e-05, None, 0.0525294, None, -9.82682e-05, None, 0.0573979, None, -8.70686e-05, None, 0.0573979, None, -8.70686e-05, None, 0.868907, None, 0.00800378, None, 0.868907, None, 0.00800378, None)
reports[-1].CovMatrix = ['1.87197e-05','8.05798e-06','-1.12901e-07','3.37699e-09','0','0','0','0','0','8.05798e-06','0.00971314','-5.75898e-08','1.37846e-07','0','0','0','0','0','-1.12901e-07','-5.75898e-08','2.16707e-09','3.39889e-11','0','0','0','0','0','3.37699e-09','1.37846e-07','3.39889e-11','6.41759e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 49630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0401797, 0.00560395, 0), \
                           ValErr(-0.464564, 0.10331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.33727e-05, 5.7653e-05, 0), \
                           -58949.8, 49630, 49630, -nan)
reports[-1].sigmaresid = ValErr(0.793619, 0.00251793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0383676, None, 5.7358e-05, None, 0.0400552, None, 0.000191582, None, 0.0400552, None, 0.000191582, None, 0.0451314, None, 0.000230007, None, 0.0451314, None, 0.000230007, None, 0.793785, None, 0.00756351, None, 0.793785, None, 0.00756351, None)
reports[-1].CovMatrix = ['3.14042e-05','7.40959e-05','-2.49225e-07','-1.05556e-08','0','0','0','0','0','7.40959e-05','0.0106729','-7.24742e-07','6.99172e-08','0','0','0','0','0','-2.49225e-07','-7.24742e-07','3.32386e-09','1.36961e-10','0','0','0','0','0','-1.05556e-08','6.99172e-08','1.36961e-10','6.33995e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 42552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.047015, 0.00686965, 0), \
                           ValErr(-0.0893616, 0.114174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.85774e-06, 6.88152e-05, 0), \
                           -50322.5, 42552, 42552, -nan)
reports[-1].sigmaresid = ValErr(0.789522, 0.00270638, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0451264, None, 0.000592787, None, 0.0466715, None, 0.000561313, None, 0.0466715, None, 0.000561313, None, 0.0487051, None, 0.000566006, None, 0.0487051, None, 0.000566006, None, 0.789528, None, 0.00722427, None, 0.789528, None, 0.00722427, None)
reports[-1].CovMatrix = ['4.71921e-05','-7.01502e-05','-3.92454e-07','2.12473e-09','0','0','0','0','0','-7.01502e-05','0.0130357','6.59006e-07','1.62995e-07','0','0','0','0','0','-3.92454e-07','6.59006e-07','4.73553e-09','3.83884e-11','0','0','0','0','0','2.12473e-09','1.62995e-07','3.83884e-11','7.32452e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 60267
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0358848, 0.00422692, 0), \
                           ValErr(-0.269269, 0.0969402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000108177, 4.4593e-05, 0), \
                           -78007.3, 60267, 60267, -nan)
reports[-1].sigmaresid = ValErr(0.882871, 0.00254298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0327724, None, -1.11882e-05, None, 0.0306309, None, 4.12541e-05, None, 0.0306309, None, 4.12541e-05, None, 0.0266211, None, -4.35628e-07, None, 0.0266211, None, -4.35628e-07, None, 0.882969, None, 0.00794145, None, 0.882969, None, 0.00794145, None)
reports[-1].CovMatrix = ['1.78668e-05','2.61382e-06','-9.90227e-08','3.36461e-09','0','0','0','0','0','2.61382e-06','0.0093974','4.1757e-08','1.39427e-07','0','0','0','0','0','-9.90227e-08','4.1757e-08','1.98853e-09','3.58675e-11','0','0','0','0','0','3.36461e-09','1.39427e-07','3.58675e-11','6.46675e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 52017
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00382659, 0.00481235, 0), \
                           ValErr(-0.131424, 0.101986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.87004e-05, 4.86702e-05, 0), \
                           -65650.6, 52017, 52017, -nan)
reports[-1].sigmaresid = ValErr(0.854841, 0.00265032, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167304, None, -0.000631848, None, -0.000588121, None, -0.000564101, None, -0.000588121, None, -0.000564101, None, 0.000614457, None, -0.00064067, None, 0.000614457, None, -0.00064067, None, 0.85487, None, 0.0079458, None, 0.85487, None, 0.0079458, None)
reports[-1].CovMatrix = ['2.31587e-05','-2.51173e-05','-1.46771e-07','2.99842e-09','0','0','0','0','0','-2.51173e-05','0.0104011','1.94985e-07','1.46061e-07','0','0','0','0','0','-1.46771e-07','1.94985e-07','2.36879e-09','3.66338e-11','0','0','0','0','0','2.99842e-09','1.46061e-07','3.66338e-11','7.02418e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 52290
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0272635, 0.00477459, 0), \
                           ValErr(-0.0234365, 0.104773, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.1657e-05, 4.9059e-05, 0), \
                           -66458.9, 52290, 52290, -nan)
reports[-1].sigmaresid = ValErr(0.862457, 0.0026641, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0315084, None, 0.000382395, None, -0.0259648, None, 0.000510958, None, -0.0259648, None, 0.000510958, None, -0.0176474, None, 0.000507119, None, -0.0176474, None, 0.000507119, None, 0.862458, None, 0.00761098, None, 0.862458, None, 0.00761098, None)
reports[-1].CovMatrix = ['2.27967e-05','-2.12025e-07','-1.4378e-07','1.32224e-08','0','0','0','0','0','-2.12025e-07','0.0109774','4.09623e-08','2.98881e-09','0','0','0','0','0','-1.4378e-07','4.09623e-08','2.40679e-09','-4.40826e-11','0','0','0','0','0','1.32224e-08','2.98881e-09','-4.40826e-11','7.09741e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 59703
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0553782, 0.00412007, 0), \
                           ValErr(-0.133422, 0.0993957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.43029e-05, 4.29744e-05, 0), \
                           -77413.4, 59703, 59703, -nan)
reports[-1].sigmaresid = ValErr(0.884889, 0.00255199, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0501362, None, -0.00114623, None, -0.0526633, None, -0.00104324, None, -0.0526633, None, -0.00104324, None, -0.0523458, None, -0.00111993, None, -0.0523458, None, -0.00111993, None, 0.884918, None, 0.00800996, None, 0.884918, None, 0.00800996, None)
reports[-1].CovMatrix = ['1.6975e-05','-2.39864e-05','-8.45176e-08','4.15625e-09','0','0','0','0','0','-2.39864e-05','0.00987951','2.12347e-07','-5.49011e-07','0','0','0','0','0','-8.45176e-08','2.12347e-07','1.8468e-09','6.15402e-10','0','0','0','0','0','4.15625e-09','-5.49011e-07','6.15402e-10','6.51263e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 67552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.053091, 0.00380693, 0), \
                           ValErr(0.145486, 0.0911252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.88444e-05, 4.05881e-05, 0), \
                           -88128.7, 67552, 67552, -nan)
reports[-1].sigmaresid = ValErr(0.891964, 0.00240072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.052064, None, 0.000139094, None, -0.0555509, None, 0.00022153, None, -0.0555509, None, 0.00022153, None, -0.0575803, None, 0.000213464, None, -0.0575803, None, 0.000213464, None, 0.891991, None, 0.00814712, None, 0.891991, None, 0.00814712, None)
reports[-1].CovMatrix = ['1.44927e-05','6.58832e-06','-6.71806e-08','-1.14386e-08','0','0','0','0','0','6.58832e-06','0.0083038','-5.7879e-08','1.92982e-06','0','0','0','0','0','-6.71806e-08','-5.7879e-08','1.64739e-09','1.58716e-09','0','0','0','0','0','-1.14386e-08','1.92982e-06','1.58716e-09','5.76347e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 59937
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0916687, 0.00408167, 0), \
                           ValErr(-0.0845339, 0.0557554, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.06733e-05, 4.21644e-05, 0), \
                           -77140.4, 59937, 59937, -nan)
reports[-1].sigmaresid = ValErr(0.876415, 0.00253038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0907624, None, -0.00128937, None, -0.0921447, None, -0.001349, None, -0.0921447, None, -0.001349, None, -0.093484, None, -0.00145845, None, -0.093484, None, -0.00145845, None, 0.876422, None, 0.00821053, None, 0.876422, None, 0.00821053, None)
reports[-1].CovMatrix = ['1.666e-05','1.10511e-05','-8.28605e-08','-4.14553e-09','0','0','0','0','0','1.10511e-05','0.00310866','-1.29685e-07','2.09208e-06','0','0','0','0','0','-8.28605e-08','-1.29685e-07','1.77784e-09','1.18939e-10','0','0','0','0','0','-4.14553e-09','2.09208e-06','1.18939e-10','6.40281e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 64874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0626912, 0.00396083, 0), \
                           ValErr(0.31012, 0.106385, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000197414, 4.19499e-05, 0), \
                           -86479.9, 64874, 64874, -nan)
reports[-1].sigmaresid = ValErr(0.917693, 0.0025477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.068677, None, 0.00164228, None, -0.0686094, None, 0.0018207, None, -0.0686094, None, 0.0018207, None, -0.0717263, None, 0.00188954, None, -0.0717263, None, 0.00188954, None, 0.917914, None, 0.00829752, None, 0.917914, None, 0.00829752, None)
reports[-1].CovMatrix = ['1.56882e-05','-5.64097e-05','-6.59594e-08','3.0233e-09','0','0','0','0','0','-5.64097e-05','0.0113178','1.31157e-07','1.3533e-07','0','0','0','0','0','-6.59594e-08','1.31157e-07','1.75979e-09','4.05052e-11','0','0','0','0','0','3.0233e-09','1.3533e-07','4.05052e-11','6.49076e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 50978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.023462, 0.00425047, 0), \
                           ValErr(-0.338102, 0.102461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000119083, 4.43289e-05, 0), \
                           -66348.3, 50978, 50978, -nan)
reports[-1].sigmaresid = ValErr(0.889204, 0.00278481, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0267252, None, 0.00101711, None, -0.0280255, None, 0.00115992, None, -0.0280255, None, 0.00115992, None, -0.0292658, None, 0.00116071, None, -0.0292658, None, 0.00116071, None, 0.889363, None, 0.00826092, None, 0.889363, None, 0.00826092, None)
reports[-1].CovMatrix = ['1.80665e-05','-6.09973e-06','-7.07803e-08','4.34973e-09','0','0','0','0','0','-6.09973e-06','0.0104983','-6.44152e-08','1.5434e-07','0','0','0','0','0','-7.07803e-08','-6.44152e-08','1.96505e-09','4.51621e-11','0','0','0','0','0','4.34973e-09','1.5434e-07','4.51621e-11','7.75517e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 62449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0383761, 0.00409266, 0), \
                           ValErr(0.1551, 0.0949676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000116843, 4.28043e-05, 0), \
                           -81527.5, 62449, 62449, -nan)
reports[-1].sigmaresid = ValErr(0.892766, 0.00251455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.046973, None, -7.10882e-05, None, -0.0438701, None, -5.70711e-05, None, -0.0438701, None, -5.70711e-05, None, -0.0448451, None, -9.3254e-05, None, -0.0448451, None, -9.3254e-05, None, 0.892835, None, 0.00754256, None, 0.892835, None, 0.00754256, None)
reports[-1].CovMatrix = ['1.67498e-05','4.29741e-06','-8.60344e-08','1.93877e-08','0','0','0','0','0','4.29741e-06','0.00901885','-4.69548e-08','8.62181e-07','0','0','0','0','0','-8.60344e-08','-4.69548e-08','1.83221e-09','6.93758e-10','0','0','0','0','0','1.93877e-08','8.62181e-07','6.93758e-10','6.32296e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 54212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.024135, 0.00478962, 0), \
                           ValErr(0.109885, 0.10144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.10773e-05, 4.99251e-05, 0), \
                           -67807, 54212, 54212, -nan)
reports[-1].sigmaresid = ValErr(0.845216, 0.00256611, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0257392, None, 0.000566311, None, -0.0284573, None, 0.000700492, None, -0.0284573, None, 0.000700492, None, -0.0290409, None, 0.000731092, None, -0.0290409, None, 0.000731092, None, 0.845241, None, 0.00761575, None, 0.845241, None, 0.00761575, None)
reports[-1].CovMatrix = ['2.29405e-05','-2.38417e-05','-1.56092e-07','7.70852e-09','0','0','0','0','0','-2.38417e-05','0.01029','2.01207e-07','-5.60101e-09','0','0','0','0','0','-1.56092e-07','2.01207e-07','2.49252e-09','-3.72336e-13','0','0','0','0','0','7.70852e-09','-5.60101e-09','-3.72336e-13','6.58493e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 51637
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00534359, 0.00456431, 0), \
                           ValErr(0.0144449, 0.106752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00014837, 4.6206e-05, 0), \
                           -67239.8, 51637, 51637, -nan)
reports[-1].sigmaresid = ValErr(0.889786, 0.00276876, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218704, None, -0.000453927, None, -0.00196592, None, -0.00104848, None, -0.00196592, None, -0.00104848, None, -0.00530753, None, -0.0011694, None, -0.00530753, None, -0.0011694, None, 0.889875, None, 0.0089374, None, 0.889875, None, 0.0089374, None)
reports[-1].CovMatrix = ['2.08329e-05','-5.43658e-05','-1.06897e-07','9.47305e-09','0','0','0','0','0','-5.43658e-05','0.011396','2.96841e-07','-4.68364e-08','0','0','0','0','0','-1.06897e-07','2.96841e-07','2.13499e-09','2.66288e-11','0','0','0','0','0','9.47305e-09','-4.68364e-08','2.66288e-11','7.66604e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 46574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0345081, 0.00478348, 0), \
                           ValErr(0.32062, 0.113958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000174744, 4.80528e-05, 0), \
                           -61026.8, 46574, 46574, -nan)
reports[-1].sigmaresid = ValErr(0.897073, 0.00293901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0274963, None, -0.00102997, None, 0.029666, None, -0.00121416, None, 0.029666, None, -0.00121416, None, 0.0360733, None, -0.00132936, None, 0.0360733, None, -0.00132936, None, 0.89728, None, 0.00842233, None, 0.89728, None, 0.00842233, None)
reports[-1].CovMatrix = ['2.28817e-05','-0.000120236','-1.02711e-07','6.70615e-09','0','0','0','0','0','-0.000120236','0.0129864','1.06167e-07','-6.92141e-08','0','0','0','0','0','-1.02711e-07','1.06167e-07','2.30907e-09','-4.76819e-11','0','0','0','0','0','6.70615e-09','-6.92141e-08','-4.76819e-11','8.63776e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 55758
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0222079, 0.00420995, 0), \
                           ValErr(-0.0810223, 0.059902, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.71004e-05, 4.35491e-05, 0), \
                           -73299.6, 55758, 55758, -nan)
reports[-1].sigmaresid = ValErr(0.900922, 0.00269731, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0223683, None, 0.00134309, None, 0.0203661, None, 0.00151263, None, 0.0203661, None, 0.00151263, None, 0.0289101, None, 0.00157684, None, 0.0289101, None, 0.00157684, None, 0.900937, None, 0.00813139, None, 0.900937, None, 0.00813139, None)
reports[-1].CovMatrix = ['1.77237e-05','-2.72777e-05','-8.08195e-08','-2.19318e-08','0','0','0','0','0','-2.72777e-05','0.00358825','-8.40781e-08','-4.43213e-06','0','0','0','0','0','-8.08195e-08','-8.40781e-08','1.89653e-09','-1.80212e-10','0','0','0','0','0','-2.19318e-08','-4.43213e-06','-1.80212e-10','7.2755e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 66266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0118447, 0.00389134, 0), \
                           ValErr(0.0959427, 0.0937311, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00015195, 4.14435e-05, 0), \
                           -86802.5, 66266, 66266, -nan)
reports[-1].sigmaresid = ValErr(0.896705, 0.00246314, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0186646, None, -0.000260669, None, 0.018137, None, -0.000219629, None, 0.018137, None, -0.000219629, None, 0.0176139, None, -0.000312175, None, 0.0176139, None, -0.000312175, None, 0.896801, None, 0.00822055, None, 0.896801, None, 0.00822055, None)
reports[-1].CovMatrix = ['1.51425e-05','2.79114e-06','-7.18318e-08','3.37272e-09','0','0','0','0','0','2.79114e-06','0.00878552','7.88294e-08','1.3235e-07','0','0','0','0','0','-7.18318e-08','7.88294e-08','1.71756e-09','3.63846e-11','0','0','0','0','0','3.37272e-09','1.3235e-07','3.63846e-11','6.06708e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 43573
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0297742, 0.00531893, 0), \
                           ValErr(-0.127592, 0.110418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000112988, 5.23423e-05, 0), \
                           -52842.4, 43573, 43573, -nan)
reports[-1].sigmaresid = ValErr(0.813667, 0.00275371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0428512, None, -0.000605606, None, 0.0377513, None, -0.000885212, None, 0.0377513, None, -0.000885212, None, 0.0323332, None, -0.00101832, None, 0.0323332, None, -0.00101832, None, 0.813721, None, 0.00782967, None, 0.813721, None, 0.00782967, None)
reports[-1].CovMatrix = ['2.8291e-05','2.95716e-05','-1.89578e-07','-2.41073e-08','0','0','0','0','0','2.95716e-05','0.012192','-1.91008e-07','-1.06527e-07','0','0','0','0','0','-1.89578e-07','-1.91008e-07','2.73971e-09','1.14915e-11','0','0','0','0','0','-2.41073e-08','-1.06527e-07','1.14915e-11','7.5829e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 55104
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0419519, 0.00477715, 0), \
                           ValErr(-0.0261777, 0.10347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.09625e-06, 5.05916e-05, 0), \
                           -69969.1, 55104, 55104, -nan)
reports[-1].sigmaresid = ValErr(0.861421, 0.0025849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0420414, None, -0.000134833, None, 0.0424982, None, -0.000112753, None, 0.0424982, None, -0.000112753, None, 0.0414579, None, -0.000167317, None, 0.0414579, None, -0.000167317, None, 0.86142, None, 0.00748357, None, 0.86142, None, 0.00748357, None)
reports[-1].CovMatrix = ['2.28212e-05','4.22084e-06','-1.55661e-07','-7.59234e-08','0','0','0','0','0','4.22084e-06','0.0107061','-1.10119e-07','-5.95196e-07','0','0','0','0','0','-1.55661e-07','-1.10119e-07','2.55951e-09','2.76068e-11','0','0','0','0','0','-7.59234e-08','-5.95196e-07','2.76068e-11','6.68169e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 46915
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0478782, 0.00769501, 0), \
                           ValErr(0.540577, 0.109923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.37463e-05, 7.70435e-05, 0), \
                           -56677.4, 46915, 46915, -nan)
reports[-1].sigmaresid = ValErr(0.809894, 0.00264398, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.045916, None, 0.000807853, None, 0.0496243, None, 0.000839186, None, 0.0496243, None, 0.000839186, None, 0.0468045, None, 0.000880341, None, 0.0468045, None, 0.000880341, None, 0.810104, None, 0.00707181, None, 0.810104, None, 0.00707181, None)
reports[-1].CovMatrix = ['5.92131e-05','2.1623e-05','-5.18129e-07','3.11603e-09','0','0','0','0','0','2.1623e-05','0.012083','-1.64245e-07','1.57882e-07','0','0','0','0','0','-5.18129e-07','-1.64245e-07','5.93571e-09','2.61862e-11','0','0','0','0','0','3.11603e-09','1.57882e-07','2.61862e-11','6.99062e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 59462
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0580771, 0.00454446, 0), \
                           ValErr(0.0120939, 0.0988934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000143641, 4.95101e-05, 0), \
                           -75467.8, 59462, 59462, -nan)
reports[-1].sigmaresid = ValErr(0.860916, 0.00249035, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0527153, None, 0.000447464, None, 0.0498516, None, 0.000337393, None, 0.0498516, None, 0.000337393, None, 0.0482314, None, 0.000279207, None, 0.0482314, None, 0.000279207, None, 0.860976, None, 0.00753224, None, 0.860976, None, 0.00753224, None)
reports[-1].CovMatrix = ['2.06521e-05','-4.85333e-05','-1.41931e-07','-5.88508e-08','0','0','0','0','0','-4.85333e-05','0.0097799','4.49271e-07','4.84736e-07','0','0','0','0','0','-1.41931e-07','4.49271e-07','2.45125e-09','1.28424e-10','0','0','0','0','0','-5.88508e-08','4.84736e-07','1.28424e-10','6.20183e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 63955
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0225834, 0.00410021, 0), \
                           ValErr(0.103501, 0.0902455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000224145, 4.24279e-05, 0), \
                           -82551.9, 63955, 63955, -nan)
reports[-1].sigmaresid = ValErr(0.87972, 0.00235556, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00525766, None, -3.78384e-05, None, 0.0110798, None, -0.000259967, None, 0.0110798, None, -0.000259967, None, 0.0106959, None, -0.000350974, None, 0.0106959, None, -0.000350974, None, 0.879908, None, 0.00768908, None, 0.879908, None, 0.00768908, None)
reports[-1].CovMatrix = ['1.68117e-05','2.76722e-05','-9.50639e-08','-1.72308e-07','0','0','0','0','0','2.76722e-05','0.00814426','5.03194e-08','2.52101e-05','0','0','0','0','0','-9.50639e-08','5.03194e-08','1.80012e-09','-4.41404e-09','0','0','0','0','0','-1.72308e-07','2.52101e-05','-4.41404e-09','5.54868e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 65542
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0182587, 0.00410433, 0), \
                           ValErr(-0.0919892, 0.0970716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138978, 4.39225e-05, 0), \
                           -87141.5, 65542, 65542, -nan)
reports[-1].sigmaresid = ValErr(0.914492, 0.00252583, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0276829, None, -0.00048169, None, -0.0247303, None, -0.000207681, None, -0.0247303, None, -0.000207681, None, -0.027117, None, -0.000205184, None, -0.027117, None, -0.000205184, None, 0.914568, None, 0.00807981, None, 0.914568, None, 0.00807981, None)
reports[-1].CovMatrix = ['1.68455e-05','-1.16695e-05','-8.86868e-08','3.237e-09','0','0','0','0','0','-1.16695e-05','0.00942289','5.63491e-08','1.36398e-07','0','0','0','0','0','-8.86868e-08','5.63491e-08','1.92918e-09','3.65325e-11','0','0','0','0','0','3.237e-09','1.36398e-07','3.65325e-11','6.37984e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 60701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0493702, 0.00424764, 0), \
                           ValErr(0.094183, 0.09641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.51395e-05, 4.57505e-05, 0), \
                           -77285.5, 60701, 60701, -nan)
reports[-1].sigmaresid = ValErr(0.864399, 0.00244797, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0519125, None, 0.000608074, None, -0.0523407, None, 0.000684536, None, -0.0523407, None, 0.000684536, None, -0.0510553, None, 0.000684203, None, -0.0510553, None, 0.000684203, None, 0.864415, None, 0.00759377, None, 0.864415, None, 0.00759377, None)
reports[-1].CovMatrix = ['1.80425e-05','-1.18199e-05','-1.13427e-07','2.43469e-07','0','0','0','0','0','-1.18199e-05','0.0092949','1.05696e-07','3.50943e-06','0','0','0','0','0','-1.13427e-07','1.05696e-07','2.09311e-09','2.31371e-10','0','0','0','0','0','2.43469e-07','3.50943e-06','2.31371e-10','5.99258e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 74166
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0490095, 0.00367201, 0), \
                           ValErr(0.113902, 0.0886328, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.36098e-06, 3.94822e-05, 0), \
                           -98996.5, 74166, 74166, -nan)
reports[-1].sigmaresid = ValErr(0.919304, 0.00236076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0458034, None, 0.000136537, None, -0.0487418, None, 0.000346631, None, -0.0487418, None, 0.000346631, None, -0.0516409, None, 0.000307425, None, -0.0516409, None, 0.000307425, None, 0.91931, None, 0.0080794, None, 0.91931, None, 0.0080794, None)
reports[-1].CovMatrix = ['1.34836e-05','1.32944e-06','-5.74589e-08','-3.32154e-08','0','0','0','0','0','1.32944e-06','0.00785577','-7.64711e-08','2.84963e-06','0','0','0','0','0','-5.74589e-08','-7.64711e-08','1.55884e-09','2.43862e-09','0','0','0','0','0','-3.32154e-08','2.84963e-06','2.43862e-09','5.57319e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 67750
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0662158, 0.00382106, 0), \
                           ValErr(0.0300455, 0.0792528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.68791e-05, 4.03466e-05, 0), \
                           -89531.1, 67750, 67750, -nan)
reports[-1].sigmaresid = ValErr(0.907156, 0.00228542, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.069629, None, -3.11008e-05, None, -0.0677469, None, 7.42871e-05, None, -0.0677469, None, 7.42871e-05, None, -0.067609, None, 5.99681e-05, None, -0.067609, None, 5.99681e-05, None, 0.907158, None, 0.00772856, None, 0.907158, None, 0.00772856, None)
reports[-1].CovMatrix = ['1.46005e-05','3.60754e-05','-6.51898e-08','-5.20045e-07','0','0','0','0','0','3.60754e-05','0.006281','-2.57548e-07','4.37435e-05','0','0','0','0','0','-6.51898e-08','-2.57548e-07','1.62785e-09','3.5042e-09','0','0','0','0','0','-5.20045e-07','4.37435e-05','3.5042e-09','5.22317e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 65830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0994912, 0.00398034, 0), \
                           ValErr(0.0496989, 0.0872922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.10742e-05, 3.98179e-05, 0), \
                           -86543.5, 65830, 65830, -nan)
reports[-1].sigmaresid = ValErr(0.900968, 0.00245245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0970272, None, -0.000231583, None, -0.0980476, None, -0.00030206, None, -0.0980476, None, -0.00030206, None, -0.101656, None, -0.000373475, None, -0.101656, None, -0.000373475, None, 0.900972, None, 0.00758734, None, 0.900972, None, 0.00758734, None)
reports[-1].CovMatrix = ['1.58431e-05','-1.87472e-05','-8.06219e-08','2.38182e-08','0','0','0','0','0','-1.87472e-05','0.00761993','6.90825e-07','-1.35106e-05','0','0','0','0','0','-8.06219e-08','6.90825e-07','1.58546e-09','5.72316e-09','0','0','0','0','0','2.38182e-08','-1.35106e-05','5.72316e-09','6.0145e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 61815
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0536948, 0.00402238, 0), \
                           ValErr(-0.0732236, 0.0531545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.05768e-06, 4.09581e-05, 0), \
                           -82174.5, 61815, 61815, -nan)
reports[-1].sigmaresid = ValErr(0.914316, 0.00259266, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0570205, None, -0.00042101, None, -0.0540127, None, -0.00039686, None, -0.0540127, None, -0.00039686, None, -0.0523629, None, -0.000485895, None, -0.0523629, None, -0.000485895, None, 0.914323, None, 0.00747231, None, 0.914323, None, 0.00747231, None)
reports[-1].CovMatrix = ['1.61796e-05','2.28507e-06','-6.73401e-08','-1.10951e-08','0','0','0','0','0','2.28507e-06','0.0028254','1.31231e-07','1.53138e-06','0','0','0','0','0','-6.73401e-08','1.31231e-07','1.67757e-09','5.91316e-10','0','0','0','0','0','-1.10951e-08','1.53138e-06','5.91316e-10','6.72188e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 67565
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0348934, 0.00395371, 0), \
                           ValErr(-0.100811, 0.0946926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.64929e-07, 4.16689e-05, 0), \
                           -89816.6, 67565, 67565, -nan)
reports[-1].sigmaresid = ValErr(0.914297, 0.00247697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0331546, None, 0.000453385, None, -0.0348742, None, 0.000513585, None, -0.0348742, None, 0.000513585, None, -0.0328305, None, 0.000515564, None, -0.0328305, None, 0.000515564, None, 0.914303, None, 0.00760832, None, 0.914303, None, 0.00760832, None)
reports[-1].CovMatrix = ['1.56318e-05','6.37553e-07','-7.59669e-08','1.31954e-08','0','0','0','0','0','6.37553e-07','0.00896669','-1.09178e-08','-6.99729e-07','0','0','0','0','0','-7.59669e-08','-1.09178e-08','1.73629e-09','8.86168e-10','0','0','0','0','0','1.31954e-08','-6.99729e-07','8.86168e-10','6.13539e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 67544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0331741, 0.00390251, 0), \
                           ValErr(0.0945475, 0.092371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000111398, 4.19783e-05, 0), \
                           -88086.9, 67544, 67544, -nan)
reports[-1].sigmaresid = ValErr(0.891549, 0.00241751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0379299, None, 0.00100529, None, -0.0381327, None, 0.00099084, None, -0.0381327, None, 0.00099084, None, -0.0410424, None, 0.000973252, None, -0.0410424, None, 0.000973252, None, 0.8916, None, 0.00762342, None, 0.8916, None, 0.00762342, None)
reports[-1].CovMatrix = ['1.52296e-05','6.39665e-06','-7.85586e-08','1.1454e-08','0','0','0','0','0','6.39665e-06','0.00853241','-9.86523e-08','5.16548e-07','0','0','0','0','0','-7.85586e-08','-9.86523e-08','1.76218e-09','5.50262e-10','0','0','0','0','0','1.1454e-08','5.16548e-07','5.50262e-10','5.84434e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 59868
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0149457, 0.00431018, 0), \
                           ValErr(0.0980758, 0.0982101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.54399e-06, 4.3893e-05, 0), \
                           -76699.6, 59868, 59868, -nan)
reports[-1].sigmaresid = ValErr(0.871281, 0.00251795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0180433, None, 0.000486065, None, -0.0152337, None, 0.000638421, None, -0.0152337, None, 0.000638421, None, -0.0179686, None, 0.000638619, None, -0.0179686, None, 0.000638619, None, 0.871287, None, 0.00774272, None, 0.871287, None, 0.00774272, None)
reports[-1].CovMatrix = ['1.85777e-05','2.14162e-05','-1.0624e-07','3.68406e-09','0','0','0','0','0','2.14162e-05','0.00964523','-3.6408e-08','1.42699e-07','0','0','0','0','0','-1.0624e-07','-3.6408e-08','1.92659e-09','2.9687e-11','0','0','0','0','0','3.68406e-09','1.42699e-07','2.9687e-11','6.34005e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 73616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00827034, 0.00379227, 0), \
                           ValErr(0.0305915, 0.0506097, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.89813e-05, 4.10784e-05, 0), \
                           -98886.6, 73616, 73616, -nan)
reports[-1].sigmaresid = ValErr(0.927129, 0.00241019, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00942762, None, 4.45865e-05, None, 0.00630926, None, 0.000112442, None, 0.00630926, None, 0.000112442, None, 0.00146133, None, 6.80914e-05, None, 0.00146133, None, 6.80914e-05, None, 0.927139, None, 0.00764068, None, 0.927139, None, 0.00764068, None)
reports[-1].CovMatrix = ['1.43813e-05','5.1017e-06','-6.76429e-08','-1.85124e-08','0','0','0','0','0','5.1017e-06','0.00256134','3.91854e-08','1.31507e-05','0','0','0','0','0','-6.76429e-08','3.91854e-08','1.68743e-09','-3.9252e-11','0','0','0','0','0','-1.85124e-08','1.31507e-05','-3.9252e-11','5.809e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 53501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0336837, 0.00451436, 0), \
                           ValErr(-0.302111, 0.102551, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.93974e-05, 4.42587e-05, 0), \
                           -68823.5, 53501, 53501, -nan)
reports[-1].sigmaresid = ValErr(0.875867, 0.00267758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.037202, None, 0.000261121, None, 0.0368282, None, 0.000231701, None, 0.0368282, None, 0.000231701, None, 0.0369162, None, 0.000205452, None, 0.0369162, None, 0.000205452, None, 0.875953, None, 0.00763632, None, 0.875953, None, 0.00763632, None)
reports[-1].CovMatrix = ['2.03794e-05','-9.46109e-06','-1.08754e-07','3.53549e-09','0','0','0','0','0','-9.46109e-06','0.0105167','7.63366e-08','1.52711e-07','0','0','0','0','0','-1.08754e-07','7.63366e-08','1.95884e-09','3.66208e-11','0','0','0','0','0','3.53549e-09','1.52711e-07','3.66208e-11','7.16945e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 67536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0255757, 0.00390066, 0), \
                           ValErr(0.241837, 0.0934434, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.74246e-05, 4.19754e-05, 0), \
                           -89972, 67536, 67536, -nan)
reports[-1].sigmaresid = ValErr(0.916926, 0.00249489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.027169, None, 0.000788668, None, 0.0264118, None, 0.000874152, None, 0.0264118, None, 0.000874152, None, 0.0292526, None, 0.000919543, None, 0.0292526, None, 0.000919543, None, 0.916971, None, 0.00778784, None, 0.916971, None, 0.00778784, None)
reports[-1].CovMatrix = ['1.52151e-05','-2.54067e-06','-6.9772e-08','3.44179e-09','0','0','0','0','0','-2.54067e-06','0.00873167','-6.94699e-08','1.27591e-07','0','0','0','0','0','-6.9772e-08','-6.94699e-08','1.76193e-09','3.6639e-11','0','0','0','0','0','3.44179e-09','1.27591e-07','3.6639e-11','6.2245e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 60210
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0437693, 0.00428682, 0), \
                           ValErr(0.178339, 0.0998193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.50215e-05, 4.48986e-05, 0), \
                           -78607.7, 60210, 60210, -nan)
reports[-1].sigmaresid = ValErr(0.892814, 0.00256512, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0412474, None, 0.000694269, None, 0.0414091, None, 0.000799411, None, 0.0414091, None, 0.000799411, None, 0.0435543, None, 0.00080349, None, 0.0435543, None, 0.00080349, None, 0.892841, None, 0.00753224, None, 0.892841, None, 0.00753224, None)
reports[-1].CovMatrix = ['1.83768e-05','1.48897e-05','-1.02376e-07','-2.00759e-08','0','0','0','0','0','1.48897e-05','0.00996389','-1.87233e-07','4.71206e-07','0','0','0','0','0','-1.02376e-07','-1.87233e-07','2.01589e-09','-4.92373e-10','0','0','0','0','0','-2.00759e-08','4.71206e-07','-4.92373e-10','6.57985e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 55043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0399031, 0.00450842, 0), \
                           ValErr(-0.186341, 0.10299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.13589e-06, 4.70967e-05, 0), \
                           -70817.6, 55043, 55043, -nan)
reports[-1].sigmaresid = ValErr(0.876034, 0.00264031, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0455061, None, -0.000582284, None, 0.0397833, None, -0.000461426, None, 0.0397833, None, -0.000461426, None, 0.043674, None, -0.00049765, None, 0.043674, None, -0.00049765, None, 0.87606, None, 0.00754417, None, 0.87606, None, 0.00754417, None)
reports[-1].CovMatrix = ['2.03258e-05','-3.22531e-05','-1.18535e-07','2.83385e-09','0','0','0','0','0','-3.22531e-05','0.010607','1.78004e-07','1.45974e-07','0','0','0','0','0','-1.18535e-07','1.78004e-07','2.2181e-09','4.1344e-11','0','0','0','0','0','2.83385e-09','1.45974e-07','4.1344e-11','6.97124e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 120094
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0620577, 0.00151214, 0), \
                           ValErr(0.0177538, 0.0173291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000116224, 3.94965e-05, 0), \
                           -92727.9, 120094, 120094, -nan)
reports[-1].sigmaresid = ValErr(0.523714, 0.00106861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0612182, None, -0.00087488, None, 0.062207, None, -0.000877734, None, 0.062207, None, -0.000877734, None, 0.0589931, None, -0.000965296, None, 0.0589931, None, -0.000965296, None, 0.523735, None, 0.00801189, None, 0.523735, None, 0.00801189, None)
reports[-1].CovMatrix = ['2.28657e-06','-5.74511e-07','-1.58775e-09','6.74731e-10','0','0','0','0','0','-5.74511e-07','0.000300298','-1.91356e-09','7.76152e-09','0','0','0','0','0','-1.58775e-09','-1.91356e-09','1.55998e-09','1.75769e-11','0','0','0','0','0','6.74731e-10','7.76152e-09','1.75769e-11','1.14193e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 117843
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0404217, 0.00152589, 0), \
                           ValErr(-0.0660204, 0.0174347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109717, 3.98099e-05, 0), \
                           -90984.9, 117843, 117843, -nan)
reports[-1].sigmaresid = ValErr(0.523691, 0.00107872, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0403082, None, 1.17777e-05, None, 0.040561, None, 2.17399e-05, None, 0.040561, None, 2.17399e-05, None, 0.0412169, None, 2.37335e-06, None, 0.0412169, None, 2.37335e-06, None, 0.52374, None, 0.00793855, None, 0.52374, None, 0.00793855, None)
reports[-1].CovMatrix = ['2.32834e-06','2.80587e-07','-1.13118e-09','7.01985e-10','0','0','0','0','0','2.80587e-07','0.00030397','2.1522e-09','8.18016e-09','0','0','0','0','0','-1.13118e-09','2.1522e-09','1.58483e-09','1.81003e-11','0','0','0','0','0','7.01985e-10','8.18016e-09','1.81003e-11','1.16364e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 116966
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0241702, 0.00151949, 0), \
                           ValErr(-0.028164, 0.0174047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143666, 3.9763e-05, 0), \
                           -89401.7, 116966, 116966, -nan)
reports[-1].sigmaresid = ValErr(0.519651, 0.0010744, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0248353, None, -0.000627266, None, -0.024118, None, -0.000637843, None, -0.024118, None, -0.000637843, None, -0.0232205, None, -0.000669365, None, -0.0232205, None, -0.000669365, None, 0.519685, None, 0.00814604, None, 0.519685, None, 0.00814604, None)
reports[-1].CovMatrix = ['2.30885e-06','1.23304e-07','-4.48665e-10','6.94174e-10','0','0','0','0','0','1.23304e-07','0.000302925','-2.8953e-09','7.97977e-09','0','0','0','0','0','-4.48665e-10','-2.8953e-09','1.5811e-09','1.80178e-11','0','0','0','0','0','6.94174e-10','7.97977e-09','1.80178e-11','1.15434e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 109330
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0654213, 0.00156798, 0), \
                           ValErr(-0.0497512, 0.0177353, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.26257e-05, 4.10435e-05, 0), \
                           -83300.9, 109330, 109330, -nan)
reports[-1].sigmaresid = ValErr(0.518397, 0.00110861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0621436, None, -0.000504011, None, -0.0654898, None, -0.000487283, None, -0.0654898, None, -0.000487283, None, -0.0644612, None, -0.000521175, None, -0.0644612, None, -0.000521175, None, 0.518419, None, 0.00818157, None, 0.518419, None, 0.00818157, None)
reports[-1].CovMatrix = ['2.45857e-06','-2.50461e-07','7.76146e-10','7.47739e-10','0','0','0','0','0','-2.50461e-07','0.000314542','-9.55688e-09','8.25816e-09','0','0','0','0','0','7.76146e-10','-9.55688e-09','1.68457e-09','1.92429e-11','0','0','0','0','0','7.47739e-10','8.25816e-09','1.92429e-11','1.22902e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 115110
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.093344, 0.00151816, 0), \
                           ValErr(-0.0148491, 0.0173402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.27056e-05, 3.98416e-05, 0), \
                           -86956.5, 115110, 115110, -nan)
reports[-1].sigmaresid = ValErr(0.515036, 0.00107341, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0922407, None, -0.000766345, None, -0.0933515, None, -0.000827572, None, -0.0933515, None, -0.000827572, None, -0.0949723, None, -0.000907096, None, -0.0949723, None, -0.000907096, None, 0.515039, None, 0.00794247, None, 0.515039, None, 0.00794247, None)
reports[-1].CovMatrix = ['2.3048e-06','-2.76019e-07','-4.38568e-10','6.79437e-10','0','0','0','0','0','-2.76019e-07','0.000300682','-3.30525e-09','7.79765e-09','0','0','0','0','0','-4.38568e-10','-3.30525e-09','1.58736e-09','1.79523e-11','0','0','0','0','0','6.79437e-10','7.79765e-09','1.79523e-11','1.15221e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 119238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0826041, 0.00149263, 0), \
                           ValErr(-0.024772, 0.017077, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.74778e-05, 3.89175e-05, 0), \
                           -90113.9, 119238, 119238, -nan)
reports[-1].sigmaresid = ValErr(0.515205, 0.00105501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0813326, None, -0.000130647, None, -0.0826301, None, -9.08537e-05, None, -0.0826301, None, -9.08537e-05, None, -0.0837558, None, -0.000130287, None, -0.0837558, None, -0.000130287, None, 0.515211, None, 0.00780599, None, 0.515211, None, 0.00780599, None)
reports[-1].CovMatrix = ['2.22795e-06','5.81718e-08','-1.66902e-09','6.51731e-10','0','0','0','0','0','5.81718e-08','0.000291625','-3.98624e-09','7.60721e-09','0','0','0','0','0','-1.66902e-09','-3.98624e-09','1.51457e-09','1.68708e-11','0','0','0','0','0','6.51731e-10','7.60721e-09','1.68708e-11','1.11305e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 127932
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0327211, 0.00145128, 0), \
                           ValErr(0.0553683, 0.0166499, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.78916e-05, 3.78923e-05, 0), \
                           -97551.5, 127932, 127932, -nan)
reports[-1].sigmaresid = ValErr(0.518709, 0.00102546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0330522, None, 0.000562523, None, -0.0327676, None, 0.000596354, None, -0.0327676, None, 0.000596354, None, -0.0340187, None, 0.000660793, None, -0.0340187, None, 0.000660793, None, 0.518732, None, 0.00796566, None, 0.518732, None, 0.00796566, None)
reports[-1].CovMatrix = ['2.10622e-06','1.07712e-07','-2.08835e-09','6.13462e-10','0','0','0','0','0','1.07712e-07','0.000277219','-3.40258e-09','7.26633e-09','0','0','0','0','0','-2.08835e-09','-3.40258e-09','1.43583e-09','1.58525e-11','0','0','0','0','0','6.13462e-10','7.26633e-09','1.58525e-11','1.05157e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 74465
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00997671, 0.00195566, 0), \
                           ValErr(0.0859811, 0.0248787, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.70587e-05, 5.09903e-05, 0), \
                           -57523.2, 74465, 74465, -nan)
reports[-1].sigmaresid = ValErr(0.523903, 0.00135757, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0110229, None, -0.000111076, None, 0.0112108, None, 8.22059e-05, None, 0.0112108, None, 8.22059e-05, None, 0.0100711, None, -6.69685e-05, None, 0.0100711, None, -6.69685e-05, None, 0.523945, None, 0.00988885, None, 0.523945, None, 0.00988885, None)
reports[-1].CovMatrix = ['3.82461e-06','-9.17375e-06','5.05892e-09','9.92234e-10','0','0','0','0','0','-9.17375e-06','0.00061895','-1.64326e-07','1.02645e-08','0','0','0','0','0','5.05892e-09','-1.64326e-07','2.60001e-09','2.74816e-11','0','0','0','0','0','9.92234e-10','1.02645e-08','2.74816e-11','1.84299e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 122621
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0482289, 0.00148144, 0), \
                           ValErr(-0.00530162, 0.0170354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000107002, 3.86273e-05, 0), \
                           -93444.7, 122621, 122621, -nan)
reports[-1].sigmaresid = ValErr(0.518468, 0.00104695, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0485112, None, 0.000337481, None, 0.048343, None, 0.000352256, None, 0.048343, None, 0.000352256, None, 0.0491623, None, 0.000373489, None, 0.0491623, None, 0.000373489, None, 0.518484, None, 0.00802662, None, 0.518484, None, 0.00802662, None)
reports[-1].CovMatrix = ['2.19466e-06','-3.79373e-07','-1.70624e-09','6.39016e-10','0','0','0','0','0','-3.79373e-07','0.000290206','-5.54312e-09','7.44523e-09','0','0','0','0','0','-1.70624e-09','-5.54312e-09','1.49207e-09','1.65478e-11','0','0','0','0','0','6.39016e-10','7.44523e-09','1.65478e-11','1.0961e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 123761
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0584144, 0.00153751, 0), \
                           ValErr(-0.0541657, 0.0176588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000162967, 4.03559e-05, 0), \
                           -99537, 123761, 123761, -nan)
reports[-1].sigmaresid = ValErr(0.540819, 0.00108704, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0587105, None, -0.000394393, None, 0.058314, None, -0.000427563, None, 0.058314, None, -0.000427563, None, 0.058034, None, -0.000476839, None, 0.058034, None, -0.000476839, None, 0.540875, None, 0.00759756, None, 0.540875, None, 0.00759756, None)
reports[-1].CovMatrix = ['2.36393e-06','1.37317e-09','1.00608e-09','7.43915e-10','0','0','0','0','0','1.37317e-09','0.000311835','-8.45068e-10','8.39088e-09','0','0','0','0','0','1.00608e-09','-8.45068e-10','1.6286e-09','1.94742e-11','0','0','0','0','0','7.43915e-10','8.39088e-09','1.94742e-11','1.18165e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 122264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0086073, 0.00153763, 0), \
                           ValErr(-0.160503, 0.0177175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000140669, 4.01621e-05, 0), \
                           -97611.4, 122264, 122264, -nan)
reports[-1].sigmaresid = ValErr(0.537637, 0.00108724, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0101948, None, -0.000426765, None, 0.00861784, None, -0.000496018, None, 0.00861784, None, -0.000496018, None, 0.00958067, None, -0.000554531, None, 0.00958067, None, -0.000554531, None, 0.537844, None, 0.00768873, None, 0.537844, None, 0.00768873, None)
reports[-1].CovMatrix = ['2.36429e-06','8.68301e-08','3.80186e-10','7.37565e-10','0','0','0','0','0','8.68301e-08','0.000313911','2.83745e-09','8.43686e-09','0','0','0','0','0','3.80186e-10','2.83745e-09','1.61299e-09','1.92688e-11','0','0','0','0','0','7.37565e-10','8.43686e-09','1.92688e-11','1.1821e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 114849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0628031, 0.00158046, 0), \
                           ValErr(0.0184183, 0.0179849, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.5269e-05, 4.15943e-05, 0), \
                           -91157.5, 114849, 114849, -nan)
reports[-1].sigmaresid = ValErr(0.535142, 0.00111658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0599503, None, 0.000176448, None, -0.0627759, None, 0.000249799, None, -0.0627759, None, 0.000249799, None, -0.0593565, None, 0.000261702, None, -0.0593565, None, 0.000261702, None, 0.535145, None, 0.00766378, None, 0.535145, None, 0.00766378, None)
reports[-1].CovMatrix = ['2.49786e-06','-6.03196e-08','2.73837e-09','7.97525e-10','0','0','0','0','0','-6.03196e-08','0.000323458','-4.89415e-09','8.65556e-09','0','0','0','0','0','2.73837e-09','-4.89415e-09','1.73008e-09','2.09355e-11','0','0','0','0','0','7.97525e-10','8.65556e-09','2.09355e-11','1.24676e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 115898
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0828389, 0.00157206, 0), \
                           ValErr(0.0189961, 0.0179534, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00015409, 4.15698e-05, 0), \
                           -91947.8, 115898, 115898, -nan)
reports[-1].sigmaresid = ValErr(0.534947, 0.00111111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0845448, None, -5.72303e-05, None, -0.0830182, None, 2.74383e-05, None, -0.0830182, None, 2.74383e-05, None, -0.0839911, None, 2.2823e-05, None, -0.0839911, None, 2.2823e-05, None, 0.534981, None, 0.00762561, None, 0.534981, None, 0.00762561, None)
reports[-1].CovMatrix = ['2.47136e-06','1.01107e-07','1.94679e-09','7.85172e-10','0','0','0','0','0','1.01107e-07','0.000322326','1.9206e-09','8.72423e-09','0','0','0','0','0','1.94679e-09','1.9206e-09','1.72805e-09','2.07174e-11','0','0','0','0','0','7.85172e-10','8.72423e-09','2.07174e-11','1.23457e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 122346
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0941056, 0.00151946, 0), \
                           ValErr(0.0172037, 0.0174728, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.99278e-06, 3.98829e-05, 0), \
                           -96258.4, 122346, 122346, -nan)
reports[-1].sigmaresid = ValErr(0.531439, 0.00107435, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0913433, None, -0.000544374, None, -0.0941088, None, -0.000510082, None, -0.0941088, None, -0.000510082, None, -0.0922299, None, -0.000539113, None, -0.0922299, None, -0.000539113, None, 0.531441, None, 0.00754177, None, 0.531441, None, 0.00754177, None)
reports[-1].CovMatrix = ['2.30876e-06','2.93373e-08','-7.14833e-10','6.99514e-10','0','0','0','0','0','2.93373e-08','0.0003053','5.86719e-09','8.21212e-09','0','0','0','0','0','-7.14833e-10','5.86719e-09','1.59064e-09','1.8496e-11','0','0','0','0','0','6.99514e-10','8.21212e-09','1.8496e-11','1.15422e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 127376
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0685316, 0.00149201, 0), \
                           ValErr(0.0204778, 0.0172485, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.71726e-08, 3.88232e-05, 0), \
                           -100382, 127376, 127376, -nan)
reports[-1].sigmaresid = ValErr(0.532133, 0.00105429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0669966, None, -0.000332425, None, -0.0685124, None, -0.000455784, None, -0.0685124, None, -0.000455784, None, -0.0696083, None, -0.000422472, None, -0.0696083, None, -0.000422472, None, 0.532136, None, 0.00822733, None, 0.532136, None, 0.00822733, None)
reports[-1].CovMatrix = ['2.22611e-06','-2.76732e-07','-2.04381e-09','6.50893e-10','0','0','0','0','0','-2.76732e-07','0.000297511','-4.45398e-09','7.74229e-09','0','0','0','0','0','-2.04381e-09','-4.45398e-09','1.50724e-09','1.69961e-11','0','0','0','0','0','6.50893e-10','7.74229e-09','1.69961e-11','1.11153e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 129209
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00310666, 0.00147621, 0), \
                           ValErr(-0.00355857, 0.0169875, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.77949e-05, 3.85043e-05, 0), \
                           -101300, 129209, 129209, -nan)
reports[-1].sigmaresid = ValErr(0.529967, 0.00104253, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00403343, None, -0.000119487, None, -0.00316135, None, -0.000139588, None, -0.00316135, None, -0.000139588, None, -0.00279419, None, -0.000147491, None, -0.00279419, None, -0.000147491, None, 0.529968, None, 0.00767356, None, 0.529968, None, 0.00767356, None)
reports[-1].CovMatrix = ['2.17919e-06','-1.64438e-07','-2.82077e-09','6.27649e-10','0','0','0','0','0','-1.64438e-07','0.000288575','1.22291e-09','7.61817e-09','0','0','0','0','0','-2.82077e-09','1.22291e-09','1.48258e-09','1.65711e-11','0','0','0','0','0','6.27649e-10','7.61817e-09','1.65711e-11','1.08687e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 127207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0378105, 0.00149029, 0), \
                           ValErr(0.0491221, 0.0171552, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143667, 3.87126e-05, 0), \
                           -100000, 127207, 127207, -nan)
reports[-1].sigmaresid = ValErr(0.531096, 0.00105294, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0366493, None, 0.000628606, None, 0.0379998, None, 0.000705547, None, 0.0379998, None, 0.000705547, None, 0.0396776, None, 0.000740801, None, 0.0396776, None, 0.000740801, None, 0.531141, None, 0.00779895, None, 0.531141, None, 0.00779895, None)
reports[-1].CovMatrix = ['2.22097e-06','1.80427e-07','-2.29695e-09','6.65657e-10','0','0','0','0','0','1.80427e-07','0.000294301','-5.80466e-09','7.84109e-09','0','0','0','0','0','-2.29695e-09','-5.80466e-09','1.49866e-09','1.66578e-11','0','0','0','0','0','6.65657e-10','7.84109e-09','1.66578e-11','1.10868e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 128974
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0693394, 0.00148264, 0), \
                           ValErr(-0.0195163, 0.0171357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.16241e-05, 3.87364e-05, 0), \
                           -101629, 128974, 128974, -nan)
reports[-1].sigmaresid = ValErr(0.532083, 0.00104764, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0709505, None, 0.000366278, None, 0.0693636, None, 0.000367431, None, 0.0693636, None, 0.000367431, None, 0.0700275, None, 0.000348412, None, 0.0700275, None, 0.000348412, None, 0.532086, None, 0.00750055, None, 0.532086, None, 0.00750055, None)
reports[-1].CovMatrix = ['2.19823e-06','1.09739e-07','-2.15e-09','6.50645e-10','0','0','0','0','0','1.09739e-07','0.000293631','8.97303e-10','7.82132e-09','0','0','0','0','0','-2.15e-09','8.97303e-10','1.50051e-09','1.69598e-11','0','0','0','0','0','6.50645e-10','7.82132e-09','1.69598e-11','1.09756e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 63252
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0516721, 0.00428203, 0), \
                           ValErr(0.0989303, 0.101988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109128, 4.71608e-05, 0), \
                           -87001.9, 63252, 63252, -nan)
reports[-1].sigmaresid = ValErr(0.957477, 0.00266625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.059516, None, -0.00236111, None, 0.0562195, None, -0.00214713, None, 0.0562195, None, -0.00214713, None, 0.0581523, None, -0.00228194, None, 0.0581523, None, -0.00228194, None, 0.957521, None, 0.00815382, None, 0.957521, None, 0.00815382, None)
reports[-1].CovMatrix = ['1.83358e-05','-2.66874e-06','-9.24537e-08','5.94719e-08','0','0','0','0','0','-2.66874e-06','0.0104015','3.64142e-08','1.68686e-06','0','0','0','0','0','-9.24537e-08','3.64142e-08','2.22414e-09','-8.81412e-10','0','0','0','0','0','5.94719e-08','1.68686e-06','-8.81412e-10','7.10889e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 58969
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0334194, 0.00477454, 0), \
                           ValErr(-0.163391, 0.103508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000217224, 5.26067e-05, 0), \
                           -77870.5, 58969, 58969, -nan)
reports[-1].sigmaresid = ValErr(0.906282, 0.00263898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0446419, None, -0.00180949, None, 0.0458652, None, -0.00164398, None, 0.0458652, None, -0.00164398, None, 0.0456441, None, -0.00176819, None, 0.0456441, None, -0.00176819, None, 0.906424, None, 0.00773955, None, 0.906424, None, 0.00773955, None)
reports[-1].CovMatrix = ['2.27962e-05','4.09276e-05','-1.56501e-07','3.99056e-09','0','0','0','0','0','4.09276e-05','0.010714','-4.82021e-07','1.52672e-07','0','0','0','0','0','-1.56501e-07','-4.82021e-07','2.76746e-09','3.06269e-11','0','0','0','0','0','3.99056e-09','1.52672e-07','3.06269e-11','6.96423e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 51031
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0379771, 0.00549737, 0), \
                           ValErr(-0.0518229, 0.110249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.00611e-05, 6.17108e-05, 0), \
                           -66820.7, 51031, 51031, -nan)
reports[-1].sigmaresid = ValErr(0.896264, 0.00274319, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0372992, None, 0.000164201, None, 0.0385857, None, 0.000240486, None, 0.0385857, None, 0.000240486, None, 0.0309929, None, 0.000214383, None, 0.0309929, None, 0.000214383, None, 0.896262, None, 0.00768008, None, 0.896262, None, 0.00768008, None)
reports[-1].CovMatrix = ['3.02211e-05','-1.94285e-05','-2.43755e-07','-6.09157e-07','0','0','0','0','0','-1.94285e-05','0.0121548','6.10895e-07','1.43127e-05','0','0','0','0','0','-2.43755e-07','6.10895e-07','3.80823e-09','-1.6036e-10','0','0','0','0','0','-6.09157e-07','1.43127e-05','-1.6036e-10','7.52509e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 64169
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.035293, 0.00421383, 0), \
                           ValErr(-0.103685, 0.100289, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103239, 4.6035e-05, 0), \
                           -87634.9, 64169, 64169, -nan)
reports[-1].sigmaresid = ValErr(0.948144, 0.00263815, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.033997, None, 0.000356254, None, 0.0310036, None, 0.000481601, None, 0.0310036, None, 0.000481601, None, 0.0307167, None, 0.000469072, None, 0.0307167, None, 0.000469072, None, 0.948188, None, 0.00814052, None, 0.948188, None, 0.00814052, None)
reports[-1].CovMatrix = ['1.77564e-05','6.07422e-06','-8.91469e-08','-8.32447e-09','0','0','0','0','0','6.07422e-06','0.0100578','-3.12426e-08','-5.10303e-07','0','0','0','0','0','-8.91469e-08','-3.12426e-08','2.11922e-09','-7.55786e-11','0','0','0','0','0','-8.32447e-09','-5.10303e-07','-7.55786e-11','6.95985e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 57139
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0157319, 0.00473536, 0), \
                           ValErr(-0.12043, 0.104722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.98319e-05, 5.09936e-05, 0), \
                           -76474.3, 57139, 57139, -nan)
reports[-1].sigmaresid = ValErr(0.922611, 0.00272921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0179448, None, -0.000212722, None, -0.019033, None, 5.6595e-05, None, -0.019033, None, 5.6595e-05, None, -0.0149258, None, 7.87632e-05, None, -0.0149258, None, 7.87632e-05, None, 0.922631, None, 0.00801021, None, 0.922631, None, 0.00801021, None)
reports[-1].CovMatrix = ['2.24237e-05','-1.90703e-05','-1.39836e-07','3.21678e-09','0','0','0','0','0','-1.90703e-05','0.0109666','1.95933e-07','1.62329e-07','0','0','0','0','0','-1.39836e-07','1.95933e-07','2.60034e-09','4.64126e-11','0','0','0','0','0','3.21678e-09','1.62329e-07','4.64126e-11','7.44861e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 58699
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0371848, 0.0046684, 0), \
                           ValErr(-0.110901, 0.105195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.32376e-05, 5.06863e-05, 0), \
                           -79250.5, 58699, 58699, -nan)
reports[-1].sigmaresid = ValErr(0.933495, 0.00272234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0377415, None, -0.000395307, None, -0.0343937, None, -0.000298025, None, -0.0343937, None, -0.000298025, None, -0.0298301, None, -0.000310832, None, -0.0298301, None, -0.000310832, None, 0.933511, None, 0.00767379, None, 0.933511, None, 0.00767379, None)
reports[-1].CovMatrix = ['2.1794e-05','4.74894e-07','-1.35193e-07','1.43847e-08','0','0','0','0','0','4.74894e-07','0.011066','7.39768e-08','-5.39584e-07','0','0','0','0','0','-1.35193e-07','7.39768e-08','2.5691e-09','4.93361e-10','0','0','0','0','0','1.43847e-08','-5.39584e-07','4.93361e-10','7.41113e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 61753
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0526595, 0.00429929, 0), \
                           ValErr(-0.319323, 0.102781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.41513e-05, 4.69698e-05, 0), \
                           -84037.3, 61753, 61753, -nan)
reports[-1].sigmaresid = ValErr(0.943579, 0.00268429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0510993, None, -0.00101341, None, -0.0565795, None, -0.00104743, None, -0.0565795, None, -0.00104743, None, -0.0556774, None, -0.00121007, None, -0.0556774, None, -0.00121007, None, 0.943672, None, 0.00836893, None, 0.943672, None, 0.00836893, None)
reports[-1].CovMatrix = ['1.84839e-05','-2.06255e-05','-9.46685e-08','-5.67448e-09','0','0','0','0','0','-2.06255e-05','0.010564','2.29242e-07','-8.39758e-09','0','0','0','0','0','-9.46685e-08','2.29242e-07','2.20616e-09','9.58236e-11','0','0','0','0','0','-5.67448e-09','-8.39758e-09','9.58236e-11','7.2054e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 68547
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0616927, 0.00399449, 0), \
                           ValErr(0.182911, 0.0970224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.02865e-05, 4.41445e-05, 0), \
                           -93936.1, 68547, 68547, -nan)
reports[-1].sigmaresid = ValErr(0.952611, 0.0025728, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0525141, None, 0.00254604, None, -0.0610102, None, 0.00255579, None, -0.0610102, None, 0.00255579, None, -0.0657927, None, 0.00271223, None, -0.0657927, None, 0.00271223, None, 0.952637, None, 0.00804739, None, 0.952637, None, 0.00804739, None)
reports[-1].CovMatrix = ['1.5956e-05','5.86124e-06','-7.27487e-08','3.87621e-09','0','0','0','0','0','5.86124e-06','0.00941334','-5.4464e-08','1.43013e-07','0','0','0','0','0','-7.27487e-08','-5.4464e-08','1.94874e-09','4.10189e-11','0','0','0','0','0','3.87621e-09','1.43013e-07','4.10189e-11','6.61932e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 61766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0995698, 0.00428467, 0), \
                           ValErr(0.0927435, 0.101243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.70495e-05, 4.62793e-05, 0), \
                           -83120.8, 61766, 61766, -nan)
reports[-1].sigmaresid = ValErr(0.929415, 0.00264151, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.10386, None, -0.00220886, None, -0.101713, None, -0.00208518, None, -0.101713, None, -0.00208518, None, -0.0994166, None, -0.0022151, None, -0.0994166, None, -0.0022151, None, 0.929428, None, 0.00783958, None, 0.929428, None, 0.00783958, None)
reports[-1].CovMatrix = ['1.83584e-05','1.59254e-06','-9.72449e-08','4.37183e-09','0','0','0','0','0','1.59254e-06','0.0102502','3.12293e-09','-1.18341e-07','0','0','0','0','0','-9.72449e-08','3.12293e-09','2.14177e-09','5.68788e-11','0','0','0','0','0','4.37183e-09','-1.18341e-07','5.68788e-11','6.9776e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 69685
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0832409, 0.00395825, 0), \
                           ValErr(0.317627, 0.0974444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000115297, 4.34835e-05, 0), \
                           -96488.3, 69685, 69685, -nan)
reports[-1].sigmaresid = ValErr(0.966279, 0.00258832, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0847636, None, 0.000657008, None, -0.0876484, None, 0.000676713, None, -0.0876484, None, 0.000676713, None, -0.0938062, None, 0.000720381, None, -0.0938062, None, 0.000720381, None, 0.966398, None, 0.00809175, None, 0.966398, None, 0.00809175, None)
reports[-1].CovMatrix = ['1.56678e-05','1.68212e-05','-6.52382e-08','4.20764e-09','0','0','0','0','0','1.68212e-05','0.00949542','-1.07845e-07','1.47832e-07','0','0','0','0','0','-6.52382e-08','-1.07845e-07','1.89081e-09','4.17311e-11','0','0','0','0','0','4.20764e-09','1.47832e-07','4.17311e-11','6.69941e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 54353
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.05807, 0.00447581, 0), \
                           ValErr(-0.208641, 0.106132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.05908e-05, 4.63853e-05, 0), \
                           -73141.9, 54353, 54353, -nan)
reports[-1].sigmaresid = ValErr(0.929365, 0.0028172, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0555468, None, -0.00363089, None, -0.0608789, None, -0.00341945, None, -0.0608789, None, -0.00341945, None, -0.0641363, None, -0.00366637, None, -0.0641363, None, -0.00366637, None, 0.929411, None, 0.00791842, None, 0.929411, None, 0.00791842, None)
reports[-1].CovMatrix = ['2.00329e-05','-7.86753e-06','-9.45368e-08','-5.05577e-09','0','0','0','0','0','-7.86753e-06','0.0112641','-1.90022e-08','-7.4901e-08','0','0','0','0','0','-9.45368e-08','-1.90022e-08','2.15159e-09','2.82197e-10','0','0','0','0','0','-5.05577e-09','-7.4901e-08','2.82197e-10','7.93663e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 66365
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0382461, 0.00416524, 0), \
                           ValErr(-0.116729, 0.0981646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103021, 4.51909e-05, 0), \
                           -91117.2, 66365, 66365, -nan)
reports[-1].sigmaresid = ValErr(0.955074, 0.00261075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0446857, None, 0.00296664, None, -0.0425578, None, 0.00290704, None, -0.0425578, None, 0.00290704, None, -0.0410725, None, 0.00301055, None, -0.0410725, None, 0.00301055, None, 0.95512, None, 0.00779376, None, 0.95512, None, 0.00779376, None)
reports[-1].CovMatrix = ['1.73492e-05','5.83165e-07','-8.57891e-08','-1.97127e-08','0','0','0','0','0','5.83165e-07','0.00963628','1.17779e-08','-6.942e-07','0','0','0','0','0','-8.57891e-08','1.17779e-08','2.04222e-09','4.48763e-10','0','0','0','0','0','-1.97127e-08','-6.942e-07','4.48763e-10','6.81599e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 62545
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00539624, 0.00439446, 0), \
                           ValErr(0.0277509, 0.101455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.98936e-05, 4.76799e-05, 0), \
                           -84340.9, 62545, 62545, -nan)
reports[-1].sigmaresid = ValErr(0.931967, 0.00263504, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0122219, None, -2.17436e-05, None, -0.00830459, None, 9.43308e-05, None, -0.00830459, None, 9.43308e-05, None, -0.011635, None, 5.96203e-05, None, -0.011635, None, 5.96203e-05, None, 0.931982, None, 0.00787777, None, 0.931982, None, 0.00787777, None)
reports[-1].CovMatrix = ['1.93113e-05','-1.18667e-05','-1.11007e-07','3.50678e-09','0','0','0','0','0','-1.18667e-05','0.0102932','1.13162e-07','1.56531e-07','0','0','0','0','0','-1.11007e-07','1.13162e-07','2.27338e-09','4.10258e-11','0','0','0','0','0','3.50678e-09','1.56531e-07','4.10258e-11','6.94345e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 57101
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00358477, 0.0045995, 0), \
                           ValErr(-0.0720571, 0.107989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.45787e-05, 4.81167e-05, 0), \
                           -77771.7, 57101, 57101, -nan)
reports[-1].sigmaresid = ValErr(0.944656, 0.00279536, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00159827, None, 0.000805414, None, 0.000296989, None, 0.000862328, None, 0.000296989, None, 0.000862328, None, -0.00262728, None, 0.000827279, None, -0.00262728, None, 0.000827279, None, 0.944672, None, 0.00764998, None, 0.944672, None, 0.00764998, None)
reports[-1].CovMatrix = ['2.11554e-05','-4.94091e-05','-1.12276e-07','3.38819e-09','0','0','0','0','0','-4.94091e-05','0.0116616','3.80865e-07','1.7119e-07','0','0','0','0','0','-1.12276e-07','3.80865e-07','2.31522e-09','4.82428e-11','0','0','0','0','0','3.38819e-09','1.7119e-07','4.82428e-11','7.81404e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 65138
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0230094, 0.00419311, 0), \
                           ValErr(0.231152, 0.100503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.09775e-05, 4.56939e-05, 0), \
                           -88858.1, 65138, 65138, -nan)
reports[-1].sigmaresid = ValErr(0.946687, 0.00262286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0208118, None, 0.000429217, None, 0.0191844, None, 0.00048741, None, 0.0191844, None, 0.00048741, None, 0.0196431, None, 0.000501566, None, 0.0196431, None, 0.000501566, None, 0.946744, None, 0.00820957, None, 0.946744, None, 0.00820957, None)
reports[-1].CovMatrix = ['1.75822e-05','3.07245e-05','-8.90062e-08','4.25058e-09','0','0','0','0','0','3.07245e-05','0.0101009','-3.18591e-07','1.51509e-07','0','0','0','0','0','-8.90062e-08','-3.18591e-07','2.08793e-09','3.66093e-11','0','0','0','0','0','4.25058e-09','1.51509e-07','3.66093e-11','6.87938e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 59111
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00511891, 0.00442173, 0), \
                           ValErr(-0.000250438, 0.10836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.44822e-05, 4.67868e-05, 0), \
                           -80518.4, 59111, 59111, -nan)
reports[-1].sigmaresid = ValErr(0.944797, 0.00274782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00208857, None, 0.00132052, None, -0.00266651, None, 0.00129296, None, -0.00266651, None, 0.00129296, None, 0.00447687, None, 0.00134477, None, 0.00447687, None, 0.00134477, None, 0.94481, None, 0.00805848, None, 0.94481, None, 0.00805848, None)
reports[-1].CovMatrix = ['1.95517e-05','1.58787e-05','-9.83907e-08','4.31602e-09','0','0','0','0','0','1.58787e-05','0.011742','5.14106e-08','1.76758e-07','0','0','0','0','0','-9.83907e-08','5.14106e-08','2.189e-09','4.48939e-11','0','0','0','0','0','4.31602e-09','1.76758e-07','4.48939e-11','7.55051e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 68259
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0246299, 0.00402045, 0), \
                           ValErr(0.280962, 0.0978472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000101028, 4.39673e-05, 0), \
                           -94038.4, 68259, 68259, -nan)
reports[-1].sigmaresid = ValErr(0.959573, 0.00259707, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0308016, None, -0.00141743, None, 0.0281408, None, -0.00124945, None, 0.0281408, None, -0.00124945, None, 0.0288355, None, -0.00137021, None, 0.0288355, None, -0.00137021, None, 0.959668, None, 0.00802407, None, 0.959668, None, 0.00802407, None)
reports[-1].CovMatrix = ['1.6164e-05','1.02834e-05','-7.181e-08','4.03762e-09','0','0','0','0','0','1.02834e-05','0.00957407','-5.68624e-08','1.47249e-07','0','0','0','0','0','-7.181e-08','-5.68624e-08','1.93312e-09','4.16507e-11','0','0','0','0','0','4.03762e-09','1.47249e-07','4.16507e-11','6.74477e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 51367
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0227094, 0.00501941, 0), \
                           ValErr(-0.441354, 0.110361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00029329, 5.1721e-05, 0), \
                           -67720.4, 51367, 51367, -nan)
reports[-1].sigmaresid = ValErr(0.904318, 0.0028214, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0450794, None, 0.00076265, None, 0.0403642, None, 0.000827914, None, 0.0403642, None, 0.000827914, None, 0.0362498, None, 0.000822439, None, 0.0362498, None, 0.000822439, None, 0.90473, None, 0.00789839, None, 0.90473, None, 0.00789839, None)
reports[-1].CovMatrix = ['2.51945e-05','2.12502e-05','-1.57416e-07','4.23172e-09','0','0','0','0','0','2.12502e-05','0.0121796','-1.67664e-07','1.7649e-07','0','0','0','0','0','-1.57416e-07','-1.67664e-07','2.67507e-09','3.80454e-11','0','0','0','0','0','4.23172e-09','1.7649e-07','3.80454e-11','7.96029e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 63971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0416761, 0.00439464, 0), \
                           ValErr(0.0729856, 0.103229, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000110444, 4.80154e-05, 0), \
                           -87971.2, 63971, 63971, -nan)
reports[-1].sigmaresid = ValErr(0.957181, 0.00262493, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0466673, None, -0.000611506, None, 0.0467962, None, -0.000433996, None, 0.0467962, None, -0.000433996, None, 0.0516672, None, -0.000494221, None, 0.0516672, None, -0.000494221, None, 0.957222, None, 0.00746443, None, 0.957222, None, 0.00746443, None)
reports[-1].CovMatrix = ['1.93129e-05','7.18939e-06','-1.0728e-07','4.125e-08','0','0','0','0','0','7.18939e-06','0.0106561','-1.07648e-07','3.17585e-06','0','0','0','0','0','-1.0728e-07','-1.07648e-07','2.30548e-09','-1.15708e-09','0','0','0','0','0','4.125e-08','3.17585e-06','-1.15708e-09','6.89024e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 56733
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0400143, 0.00591267, 0), \
                           ValErr(0.365146, 0.108711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.54748e-05, 6.57498e-05, 0), \
                           -75689.6, 56733, 56733, -nan)
reports[-1].sigmaresid = ValErr(0.918696, 0.00272734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0388586, None, -0.00221336, None, 0.0450075, None, -0.00207716, None, 0.0450075, None, -0.00207716, None, 0.0418715, None, -0.00221816, None, 0.0418715, None, -0.00221816, None, 0.918798, None, 0.0072526, None, 0.918798, None, 0.0072526, None)
reports[-1].CovMatrix = ['3.49597e-05','1.28081e-05','-2.94637e-07','3.56991e-09','0','0','0','0','0','1.28081e-05','0.0118181','-1.17275e-07','1.67765e-07','0','0','0','0','0','-2.94637e-07','-1.17275e-07','4.32303e-09','3.58775e-11','0','0','0','0','0','3.56991e-09','1.67765e-07','3.58775e-11','7.43839e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 66831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0342561, 0.00417652, 0), \
                           ValErr(-0.0151575, 0.0999859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127003, 4.74901e-05, 0), \
                           -91875.1, 66831, 66831, -nan)
reports[-1].sigmaresid = ValErr(0.956762, 0.00261339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0270183, None, -0.00177757, None, 0.0291022, None, -0.00162798, None, 0.0291022, None, -0.00162798, None, 0.0252473, None, -0.00177088, None, 0.0252473, None, -0.00177088, None, 0.956812, None, 0.00778003, None, 0.956812, None, 0.00778003, None)
reports[-1].CovMatrix = ['1.74433e-05','-2.45561e-05','-9.16139e-08','2.51123e-08','0','0','0','0','0','-2.45561e-05','0.00999718','2.17219e-07','-3.36139e-08','0','0','0','0','0','-9.16139e-08','2.17219e-07','2.25531e-09','-3.15386e-10','0','0','0','0','0','2.51123e-08','-3.36139e-08','-3.15386e-10','6.82978e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 66086
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00448639, 0.00431234, 0), \
                           ValErr(-0.198141, 0.102327, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.58738e-05, 4.74183e-05, 0), \
                           -91113.7, 66086, 66086, -nan)
reports[-1].sigmaresid = ValErr(0.960568, 0.00264214, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00846677, None, -0.0020018, None, 0.00675114, None, -0.00187686, None, 0.00675114, None, -0.00187686, None, 0.00501256, None, -0.0020331, None, 0.00501256, None, -0.0020331, None, 0.960606, None, 0.00766846, None, 0.960606, None, 0.00766846, None)
reports[-1].CovMatrix = ['1.85962e-05','1.695e-05','-1.01983e-07','3.91374e-09','0','0','0','0','0','1.695e-05','0.0104709','-1.63067e-07','1.54266e-07','0','0','0','0','0','-1.01983e-07','-1.63067e-07','2.2485e-09','3.96177e-11','0','0','0','0','0','3.91374e-09','1.54266e-07','3.96177e-11','6.9809e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 67618
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0302371, 0.00422732, 0), \
                           ValErr(0.0998825, 0.100508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109556, 4.72109e-05, 0), \
                           -94169.8, 67618, 67618, -nan)
reports[-1].sigmaresid = ValErr(0.974079, 0.0026465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0264378, None, -0.000941927, None, -0.0256236, None, -0.00102331, None, -0.0256236, None, -0.00102331, None, -0.0307414, None, -0.00120496, None, -0.0307414, None, -0.00120496, None, 0.974123, None, 0.00786806, None, 0.974123, None, 0.00786806, None)
reports[-1].CovMatrix = ['1.78703e-05','-1.31899e-05','-9.23562e-08','-1.55291e-08','0','0','0','0','0','-1.31899e-05','0.0101018','1.03808e-07','6.19797e-08','0','0','0','0','0','-9.23562e-08','1.03808e-07','2.22887e-09','2.11939e-10','0','0','0','0','0','-1.55291e-08','6.19797e-08','2.11939e-10','7.00397e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 65566
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0750725, 0.00423018, 0), \
                           ValErr(-0.146019, 0.100284, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000144498, 4.6542e-05, 0), \
                           -89475.4, 65566, 65566, -nan)
reports[-1].sigmaresid = ValErr(0.947171, 0.0026142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0696982, None, -0.000939384, None, -0.0687053, None, -0.000912714, None, -0.0687053, None, -0.000912714, None, -0.075694, None, -0.000977977, None, -0.075694, None, -0.000977977, None, 0.947254, None, 0.00770843, None, 0.947254, None, 0.00770843, None)
reports[-1].CovMatrix = ['1.78944e-05','2.31141e-06','-9.57555e-08','-1.01408e-08','0','0','0','0','0','2.31141e-06','0.0100569','1.99307e-08','-1.55759e-07','0','0','0','0','0','-9.57555e-08','1.99307e-08','2.16616e-09','3.631e-10','0','0','0','0','0','-1.01408e-08','-1.55759e-07','3.631e-10','6.83403e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 73941
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0526568, 0.00363716, 0), \
                           ValErr(0.0707896, 0.0806747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.71151e-05, 4.28628e-05, 0), \
                           -103017, 73941, 73941, -nan)
reports[-1].sigmaresid = ValErr(0.974627, 0.0025223, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0511349, None, -4.70854e-05, None, -0.0514511, None, 1.9131e-05, None, -0.0514511, None, 1.9131e-05, None, -0.0524348, None, 5.64754e-06, None, -0.0524348, None, 5.64754e-06, None, 0.974635, None, 0.00746203, None, 0.974635, None, 0.00746203, None)
reports[-1].CovMatrix = ['1.32289e-05','5.80886e-05','-6.67792e-08','-3.06327e-07','0','0','0','0','0','5.80886e-05','0.00650842','2.55746e-07','1.08591e-05','0','0','0','0','0','-6.67792e-08','2.55746e-07','1.83722e-09','-5.29741e-10','0','0','0','0','0','-3.06327e-07','1.08591e-05','-5.29741e-10','6.362e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 68238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0894455, 0.00408531, 0), \
                           ValErr(0.0970977, 0.0972898, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000174554, 4.47436e-05, 0), \
                           -94012.6, 68238, 68238, -nan)
reports[-1].sigmaresid = ValErr(0.959616, 0.00259758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0831105, None, -0.00332958, None, -0.0825353, None, -0.00315625, None, -0.0825353, None, -0.00315625, None, -0.0785267, None, -0.00332314, None, -0.0785267, None, -0.00332314, None, 0.959731, None, 0.00756856, None, 0.959731, None, 0.00756856, None)
reports[-1].CovMatrix = ['1.66898e-05','8.73422e-06','-7.99376e-08','3.93357e-09','0','0','0','0','0','8.73422e-06','0.0094653','-8.32892e-08','1.4531e-07','0','0','0','0','0','-7.99376e-08','-8.32892e-08','2.00199e-09','4.04177e-11','0','0','0','0','0','3.93357e-09','1.4531e-07','4.04177e-11','6.74744e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 68518
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.119388, 0.00407694, 0), \
                           ValErr(0.248459, 0.0981449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.89224e-05, 4.50536e-05, 0), \
                           -94712.3, 68518, 68518, -nan)
reports[-1].sigmaresid = ValErr(0.964023, 0.00260418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.114234, None, -0.00201681, None, -0.115653, None, -0.00186569, None, -0.115653, None, -0.00186569, None, -0.121999, None, -0.00201657, None, -0.121999, None, -0.00201657, None, 0.964094, None, 0.00752358, None, 0.964094, None, 0.00752358, None)
reports[-1].CovMatrix = ['1.66215e-05','-1.63312e-05','-7.86081e-08','3.60887e-09','0','0','0','0','0','-1.63312e-05','0.00963243','1.24224e-07','1.44848e-07','0','0','0','0','0','-7.86081e-08','1.24224e-07','2.02983e-09','4.44494e-11','0','0','0','0','0','3.60887e-09','1.44848e-07','4.44494e-11','6.78174e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 63705
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0556221, 0.0042712, 0), \
                           ValErr(-0.324835, 0.101194, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.66421e-06, 4.55335e-05, 0), \
                           -87994.5, 63705, 63705, -nan)
reports[-1].sigmaresid = ValErr(0.963045, 0.00268685, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0554334, None, 0.0026919, None, -0.0561572, None, 0.00261835, None, -0.0561572, None, 0.00261835, None, -0.05113, None, 0.00272538, None, -0.05113, None, 0.00272538, None, 0.96312, None, 0.00759377, None, 0.96312, None, 0.00759377, None)
reports[-1].CovMatrix = ['1.82431e-05','-1.2811e-05','-8.72779e-08','-4.26574e-08','0','0','0','0','0','-1.2811e-05','0.0102402','7.62704e-08','-1.40581e-06','0','0','0','0','0','-8.72779e-08','7.62704e-08','2.0733e-09','7.35784e-10','0','0','0','0','0','-4.26574e-08','-1.40581e-06','7.35784e-10','7.21917e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 68632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0378838, 0.00414103, 0), \
                           ValErr(-0.0989318, 0.0994586, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.42238e-05, 4.54799e-05, 0), \
                           -95106.1, 68632, 68632, -nan)
reports[-1].sigmaresid = ValErr(0.967346, 0.00261098, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0416845, None, -0.00213808, None, -0.0397264, None, -0.00195527, None, -0.0397264, None, -0.00195527, None, -0.0353862, None, -0.00213522, None, -0.0353862, None, -0.00213522, None, 0.967359, None, 0.00727067, None, 0.967359, None, 0.00727067, None)
reports[-1].CovMatrix = ['1.71481e-05','-2.15317e-06','-8.52467e-08','3.77972e-09','0','0','0','0','0','-2.15317e-06','0.00989201','3.66804e-09','1.48333e-07','0','0','0','0','0','-8.52467e-08','3.66804e-09','2.06842e-09','4.19176e-11','0','0','0','0','0','3.77972e-09','1.48333e-07','4.19176e-11','6.81722e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 71784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0441408, 0.00398063, 0), \
                           ValErr(0.146219, 0.0966562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000229202, 4.43316e-05, 0), \
                           -99691, 71784, 71784, -nan)
reports[-1].sigmaresid = ValErr(0.970279, 0.00253935, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.054063, None, -0.000177544, None, -0.052678, None, -0.00014492, None, -0.052678, None, -0.00014492, None, -0.0495366, None, -0.000190045, None, -0.0495366, None, -0.000190045, None, 0.970471, None, 0.00741489, None, 0.970471, None, 0.00741489, None)
reports[-1].CovMatrix = ['1.58454e-05','7.56319e-07','-7.3262e-08','-3.12192e-08','0','0','0','0','0','7.56319e-07','0.00934243','-3.17452e-08','1.58268e-06','0','0','0','0','0','-7.3262e-08','-3.17452e-08','1.96529e-09','5.3453e-10','0','0','0','0','0','-3.12192e-08','1.58268e-06','5.3453e-10','6.44828e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 63514
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0289308, 0.00446814, 0), \
                           ValErr(0.0761395, 0.100676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.7828e-05, 4.86049e-05, 0), \
                           -85462.6, 63514, 63514, -nan)
reports[-1].sigmaresid = ValErr(0.929259, 0.00260728, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0395512, None, 0.00116206, None, -0.0320548, None, 0.00119742, None, -0.0320548, None, 0.00119742, None, -0.0354296, None, 0.00126633, None, -0.0354296, None, 0.00126633, None, 0.929273, None, 0.00739629, None, 0.929273, None, 0.00739629, None)
reports[-1].CovMatrix = ['1.99643e-05','3.40789e-05','-1.22313e-07','3.99574e-09','0','0','0','0','0','3.40789e-05','0.0101356','-2.90783e-07','1.51983e-07','0','0','0','0','0','-1.22313e-07','-2.90783e-07','2.36244e-09','3.35982e-11','0','0','0','0','0','3.99574e-09','1.51983e-07','3.35982e-11','6.79789e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 75184
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.011836, 0.00391204, 0), \
                           ValErr(-0.00652548, 0.0486683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.27549e-06, 4.40545e-05, 0), \
                           -105771, 75184, 75184, -nan)
reports[-1].sigmaresid = ValErr(0.987965, 0.00254704, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.013064, None, -0.00101752, None, -0.0120205, None, -0.000890089, None, -0.0120205, None, -0.000890089, None, -0.0150202, None, -0.000943162, None, -0.0150202, None, -0.000943162, None, 0.987965, None, 0.00740287, None, 0.987965, None, 0.00740287, None)
reports[-1].CovMatrix = ['1.53041e-05','-8.85065e-06','-6.70402e-08','-3.09512e-09','0','0','0','0','0','-8.85065e-06','0.0023686','1.04314e-07','-5.00861e-06','0','0','0','0','0','-6.70402e-08','1.04314e-07','1.9408e-09','4.54337e-11','0','0','0','0','0','-3.09512e-09','-5.00861e-06','4.54337e-11','6.48741e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 55851
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0348941, 0.00486474, 0), \
                           ValErr(-0.143008, 0.106763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.09087e-05, 5.15787e-05, 0), \
                           -74623.7, 55851, 55851, -nan)
reports[-1].sigmaresid = ValErr(0.92052, 0.00275425, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0322978, None, 0.000712287, None, 0.037161, None, 0.000841093, None, 0.037161, None, 0.000841093, None, 0.0389333, None, 0.000856103, None, 0.0389333, None, 0.000856103, None, 0.92054, None, 0.00728467, None, 0.92054, None, 0.00728467, None)
reports[-1].CovMatrix = ['2.36657e-05','-1.05925e-05','-1.50314e-07','3.62872e-09','0','0','0','0','0','-1.05925e-05','0.0113983','1.25423e-07','1.66366e-07','0','0','0','0','0','-1.50314e-07','1.25423e-07','2.66036e-09','4.19472e-11','0','0','0','0','0','3.62872e-09','1.66366e-07','4.19472e-11','7.58587e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 62007
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0349045, 0.0043417, 0), \
                           ValErr(-0.0429273, 0.115593, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.40665e-05, 4.73e-05, 0), \
                           -86179.2, 62007, 62007, -nan)
reports[-1].sigmaresid = ValErr(0.971314, 0.0027582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0336705, None, -0.00202302, None, 0.0342676, None, -0.00190427, None, 0.0342676, None, -0.00190427, None, 0.0320628, None, -0.00198577, None, 0.0320628, None, -0.00198577, None, 0.971314, None, 0.0076252, None, 0.971314, None, 0.0076252, None)
reports[-1].CovMatrix = ['1.88504e-05','8.21114e-05','-8.40367e-08','5.62489e-09','0','0','0','0','0','8.21114e-05','0.0133617','-5.72268e-08','2.15843e-07','0','0','0','0','0','-8.40367e-08','-5.72268e-08','2.23729e-09','4.68636e-11','0','0','0','0','0','5.62489e-09','2.15843e-07','4.68636e-11','7.6077e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 65049
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0272389, 0.00423705, 0), \
                           ValErr(-0.18385, 0.101698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.26465e-05, 4.53201e-05, 0), \
                           -89807.9, 65049, 65049, -nan)
reports[-1].sigmaresid = ValErr(0.962407, 0.00266823, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0320173, None, -2.01682e-05, None, 0.0299355, None, 9.16888e-05, None, 0.0299355, None, 9.16888e-05, None, 0.0319554, None, 5.64142e-05, None, 0.0319554, None, 5.64142e-05, None, 0.962443, None, 0.0076975, None, 0.962443, None, 0.0076975, None)
reports[-1].CovMatrix = ['1.79526e-05','3.69151e-06','-8.73321e-08','4.01559e-09','0','0','0','0','0','3.69151e-06','0.0103425','-4.33043e-08','1.5577e-07','0','0','0','0','0','-8.73321e-08','-4.33043e-08','2.05391e-09','4.18639e-11','0','0','0','0','0','4.01559e-09','1.5577e-07','4.18639e-11','7.11947e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 60711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0513997, 0.00441394, 0), \
                           ValErr(0.047431, 0.105402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.05874e-05, 4.72231e-05, 0), \
                           -83285.8, 60711, 60711, -nan)
reports[-1].sigmaresid = ValErr(0.953995, 0.00273777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0560988, None, -0.000812229, None, 0.0523991, None, -0.000735401, None, 0.0523991, None, -0.000735401, None, 0.0546819, None, -0.000784024, None, 0.0546819, None, -0.000784024, None, 0.953997, None, 0.00742285, None, 0.953997, None, 0.00742285, None)
reports[-1].CovMatrix = ['1.94828e-05','-2.66131e-05','-9.97232e-08','3.71259e-09','0','0','0','0','0','-2.66131e-05','0.0111096','1.70065e-07','1.60894e-07','0','0','0','0','0','-9.97232e-08','1.70065e-07','2.23002e-09','4.63612e-11','0','0','0','0','0','3.71259e-09','1.60894e-07','4.63612e-11','7.4954e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 106149
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0259511, 0.000537702, 0), \
                           ValErr(-0.0614507, 0.0135548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.57956e-05, 1.4286e-05, 0), \
                           36218.5, 106149, 106149, -nan)
reports[-1].sigmaresid = ValErr(0.17202, 0.000373342, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0264114, None, 0.00049464, None, 0.0264767, None, 0.000480847, None, 0.0264767, None, 0.000480847, None, 0.0274698, None, 0.0004524, None, 0.0274698, None, 0.0004524, None, 0.172054, None, 0.00386313, None, 0.172054, None, 0.00386313, None)
reports[-1].CovMatrix = ['2.89123e-07','1.80409e-07','-1.44093e-09','4.88728e-11','0','0','0','0','0','1.80409e-07','0.000183733','3.22429e-10','1.4943e-09','0','0','0','0','0','-1.44093e-09','3.22429e-10','2.04089e-10','1.27753e-12','0','0','0','0','0','4.88728e-11','1.4943e-09','1.27753e-12','1.39384e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 101332
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0216259, 0.000545878, 0), \
                           ValErr(-0.0352181, 0.0136536, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.37084e-05, 1.45493e-05, 0), \
                           35967, 101332, 101332, -nan)
reports[-1].sigmaresid = ValErr(0.169673, 0.000376898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0228342, None, 0.000596562, None, 0.0223766, None, 0.000568548, None, 0.0223766, None, 0.000568548, None, 0.0223189, None, 0.000592285, None, 0.0223189, None, 0.000592285, None, 0.169714, None, 0.0038299, None, 0.169714, None, 0.0038299, None)
reports[-1].CovMatrix = ['2.97983e-07','-4.29414e-08','-1.71346e-09','4.8138e-11','0','0','0','0','0','-4.29414e-08','0.000186421','4.32151e-10','1.49389e-09','0','0','0','0','0','-1.71346e-09','4.32151e-10','2.11683e-10','1.30792e-12','0','0','0','0','0','4.8138e-11','1.49389e-09','1.30792e-12','1.42052e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 20846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00228996, 0.0012664, 0), \
                           ValErr(-0.134065, 0.0356487, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.58373e-05, 3.1842e-05, 0), \
                           7229.14, 20846, 20846, -nan)
reports[-1].sigmaresid = ValErr(0.171063, 0.000837777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00334295, None, 0.000145114, None, 0.00296733, None, 0.000265429, None, 0.00296733, None, 0.000265429, None, 0.00592521, None, 0.000244643, None, 0.00592521, None, 0.000244643, None, 0.17113, None, 0.00544305, None, 0.17113, None, 0.00544305, None)
reports[-1].CovMatrix = ['1.60377e-06','1.11468e-05','-1.12337e-08','3.19891e-10','0','0','0','0','0','1.11468e-05','0.00127083','-1.2715e-07','1.00296e-08','0','0','0','0','0','-1.12337e-08','-1.2715e-07','1.01391e-09','4.93594e-12','0','0','0','0','0','3.19891e-10','1.00296e-08','4.93594e-12','7.01871e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 86957
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0118686, 0.000603754, 0), \
                           ValErr(-0.0231027, 0.0149251, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.29516e-05, 1.71485e-05, 0), \
                           26762.1, 86957, 86957, -nan)
reports[-1].sigmaresid = ValErr(0.17787, 0.000426517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118059, None, 0.0100465, None, -0.0117335, None, 0.00959675, None, -0.0117335, None, 0.00959675, None, -0.0110752, None, 0.00976903, None, -0.0110752, None, 0.00976903, None, 0.177903, None, 0.00413327, None, 0.177903, None, 0.00413327, None)
reports[-1].CovMatrix = ['3.64519e-07','2.51804e-07','-3.38987e-10','6.95806e-11','0','0','0','0','0','2.51804e-07','0.00022276','3.93345e-09','1.80242e-09','0','0','0','0','0','-3.38987e-10','3.93345e-09','2.94072e-10','1.9442e-12','0','0','0','0','0','6.95806e-11','1.80242e-09','1.9442e-12','1.81917e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 105757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0311797, 0.000536824, 0), \
                           ValErr(0.0101604, 0.0134539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.2858e-05, 1.42172e-05, 0), \
                           36563.1, 105757, 105757, -nan)
reports[-1].sigmaresid = ValErr(0.171244, 0.000372345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0300765, None, -0.00030312, None, -0.0305707, None, -0.000332087, None, -0.0305707, None, -0.000332087, None, -0.029775, None, -0.000332842, None, -0.029775, None, -0.000332842, None, 0.171272, None, 0.00380762, None, 0.171272, None, 0.00380762, None)
reports[-1].CovMatrix = ['2.8818e-07','-7.03881e-09','-1.48419e-09','4.68086e-11','0','0','0','0','0','-7.03881e-09','0.000181008','-2.7656e-10','1.42517e-09','0','0','0','0','0','-1.48419e-09','-2.7656e-10','2.02129e-10','1.25119e-12','0','0','0','0','0','4.68086e-11','1.42517e-09','1.25119e-12','1.38641e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 94348
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0365114, 0.000576508, 0), \
                           ValErr(0.000163747, 0.0147699, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.21581e-07, 1.59662e-05, 0), \
                           30503.9, 94348, 94348, -nan)
reports[-1].sigmaresid = ValErr(0.175126, 0.000403152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0365509, None, -0.000664125, None, -0.0365118, None, -0.000629941, None, -0.0365118, None, -0.000629941, None, -0.0376027, None, -0.000655405, None, -0.0376027, None, -0.000655405, None, 0.175126, None, 0.00381287, None, 0.175126, None, 0.00381287, None)
reports[-1].CovMatrix = ['3.32361e-07','-6.137e-07','-1.10346e-09','5.25708e-11','0','0','0','0','0','-6.137e-07','0.000218151','-2.83492e-08','1.35001e-09','0','0','0','0','0','-1.10346e-09','-2.83492e-08','2.54919e-10','1.38866e-12','0','0','0','0','0','5.25708e-11','1.35001e-09','1.38866e-12','1.62531e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 104494
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0530743, 0.000539551, 0), \
                           ValErr(-0.0189088, 0.0135019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31597e-05, 1.42882e-05, 0), \
                           36169.5, 104494, 104494, -nan)
reports[-1].sigmaresid = ValErr(0.171173, 0.000374434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0535242, None, -0.0005812, None, -0.0532425, None, -0.000584958, None, -0.0532425, None, -0.000584958, None, -0.0531157, None, -0.000573328, None, -0.0531157, None, -0.000573328, None, 0.171177, None, 0.0038365, None, 0.171177, None, 0.0038365, None)
reports[-1].CovMatrix = ['2.91115e-07','-6.38254e-09','-1.47886e-09','4.78903e-11','0','0','0','0','0','-6.38254e-09','0.0001823','5.02574e-10','1.4639e-09','0','0','0','0','0','-1.47886e-09','5.02574e-10','2.04152e-10','1.26708e-12','0','0','0','0','0','4.78903e-11','1.4639e-09','1.26708e-12','1.40201e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 100728
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.06272, 0.000551511, 0), \
                           ValErr(0.00714124, 0.0137678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.75091e-06, 1.44936e-05, 0), \
                           35691.8, 100728, 100728, -nan)
reports[-1].sigmaresid = ValErr(0.169776, 0.000378256, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.062711, None, 0.000557313, None, -0.0627555, None, 0.000484739, None, -0.0627555, None, 0.000484739, None, -0.0626224, None, 0.000529766, None, -0.0626224, None, 0.000529766, None, 0.169776, None, 0.00382794, None, 0.169776, None, 0.00382794, None)
reports[-1].CovMatrix = ['3.04164e-07','1.50682e-08','-1.94498e-09','4.78858e-11','0','0','0','0','0','1.50682e-08','0.000189552','-3.61798e-10','1.50045e-09','0','0','0','0','0','-1.94498e-09','-3.61798e-10','2.10064e-10','1.2382e-12','0','0','0','0','0','4.78858e-11','1.50045e-09','1.2382e-12','1.43077e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 88147
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0576218, 0.000587232, 0), \
                           ValErr(-0.00234803, 0.0142437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.98359e-05, 1.52745e-05, 0), \
                           31919.3, 88147, 88147, -nan)
reports[-1].sigmaresid = ValErr(0.168461, 0.000401218, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0567974, None, -0.000313806, None, -0.0569302, None, -0.000336404, None, -0.0569302, None, -0.000336404, None, -0.0580146, None, -0.000308682, None, -0.0580146, None, -0.000308682, None, 0.168481, None, 0.00380862, None, 0.168481, None, 0.00380862, None)
reports[-1].CovMatrix = ['3.44842e-07','-1.47987e-08','-2.31094e-09','5.29205e-11','0','0','0','0','0','-1.47987e-08','0.000202882','2.55879e-10','1.67492e-09','0','0','0','0','0','-2.31094e-09','2.55879e-10','2.3331e-10','1.38841e-12','0','0','0','0','0','5.29205e-11','1.67492e-09','1.38841e-12','1.60976e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 98828
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0488975, 0.000553191, 0), \
                           ValErr(0.0238633, 0.0138608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.50545e-05, 1.46195e-05, 0), \
                           34998.5, 98828, 98828, -nan)
reports[-1].sigmaresid = ValErr(0.16981, 0.000381952, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0489299, None, -0.000195487, None, -0.0490206, None, -0.000196051, None, -0.0490206, None, -0.000196051, None, -0.0496589, None, -0.000188184, None, -0.0496589, None, -0.000188184, None, 0.169814, None, 0.00384741, None, 0.169814, None, 0.00384741, None)
reports[-1].CovMatrix = ['3.0602e-07','4.33057e-09','-1.74491e-09','4.95078e-11','0','0','0','0','0','4.33057e-09','0.000192122','-4.66833e-10','1.53253e-09','0','0','0','0','0','-1.74491e-09','-4.66833e-10','2.13729e-10','1.30297e-12','0','0','0','0','0','4.95078e-11','1.53253e-09','1.30297e-12','1.45887e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 103096
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0424739, 0.00054502, 0), \
                           ValErr(-0.00992944, 0.0136832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.32908e-06, 1.4501e-05, 0), \
                           35479.7, 103096, 103096, -nan)
reports[-1].sigmaresid = ValErr(0.171515, 0.000377718, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0428332, None, 0.00137159, None, -0.0424025, None, 0.00125049, None, -0.0424025, None, 0.00125049, None, -0.043056, None, 0.00132021, None, -0.043056, None, 0.00132021, None, 0.171516, None, 0.0038611, None, 0.171516, None, 0.0038611, None)
reports[-1].CovMatrix = ['2.97047e-07','2.26145e-08','-1.56848e-09','4.83841e-11','0','0','0','0','0','2.26145e-08','0.000187231','1.61065e-09','1.49189e-09','0','0','0','0','0','-1.56848e-09','1.61065e-09','2.10278e-10','1.30084e-12','0','0','0','0','0','4.83841e-11','1.49189e-09','1.30084e-12','1.42671e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 95402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0278546, 0.000564925, 0), \
                           ValErr(0.0322229, 0.0141938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.37638e-05, 1.49733e-05, 0), \
                           33501.7, 95402, 95402, -nan)
reports[-1].sigmaresid = ValErr(0.170316, 0.000389907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0282796, None, -0.00086193, None, -0.0285365, None, -0.000824673, None, -0.0285365, None, -0.000824673, None, -0.0278748, None, -0.000836433, None, -0.0278748, None, -0.000836433, None, 0.170348, None, 0.00378213, None, 0.170348, None, 0.00378213, None)
reports[-1].CovMatrix = ['3.1914e-07','-3.72084e-08','-1.83881e-09','5.05763e-11','0','0','0','0','0','-3.72084e-08','0.000201463','8.86234e-10','1.58736e-09','0','0','0','0','0','-1.83881e-09','8.86234e-10','2.24201e-10','1.32326e-12','0','0','0','0','0','5.05763e-11','1.58736e-09','1.32326e-12','1.52027e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 97855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0137423, 0.000555227, 0), \
                           ValErr(-0.00222187, 0.0141551, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.71706e-05, 1.46148e-05, 0), \
                           34396.6, 97855, 97855, -nan)
reports[-1].sigmaresid = ValErr(0.170257, 0.000384857, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0142882, None, -0.000916544, None, -0.0136132, None, -0.000890372, None, -0.0136132, None, -0.000890372, None, -0.0134326, None, -0.000837025, None, -0.0134326, None, -0.000837025, None, 0.170259, None, 0.00403294, None, 0.170259, None, 0.00403294, None)
reports[-1].CovMatrix = ['3.08277e-07','3.60673e-07','-1.56769e-09','5.37655e-11','0','0','0','0','0','3.60673e-07','0.000200366','-4.28249e-09','1.61934e-09','0','0','0','0','0','-1.56769e-09','-4.28249e-09','2.13592e-10','1.3029e-12','0','0','0','0','0','5.37655e-11','1.61934e-09','1.3029e-12','1.48115e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 100371
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00096323, 0.000550696, 0), \
                           ValErr(0.0550999, 0.0138102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.92175e-05, 1.45649e-05, 0), \
                           35360.8, 100371, 100371, -nan)
reports[-1].sigmaresid = ValErr(0.170122, 0.000379701, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0019816, None, -0.000440697, None, 0.00148882, None, -0.000394126, None, 0.00148882, None, -0.000394126, None, 0.00182826, None, -0.00038954, None, 0.00182826, None, -0.00038954, None, 0.17015, None, 0.00390613, None, 0.17015, None, 0.00390613, None)
reports[-1].CovMatrix = ['3.03267e-07','-9.5798e-08','-1.77584e-09','4.76102e-11','0','0','0','0','0','-9.5798e-08','0.000190722','-8.26736e-10','1.49106e-09','0','0','0','0','0','-1.77584e-09','-8.26736e-10','2.12137e-10','1.26025e-12','0','0','0','0','0','4.76102e-11','1.49106e-09','1.26025e-12','1.44173e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 107315
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0113523, 0.000532775, 0), \
                           ValErr(-0.0152636, 0.0133986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.35249e-05, 1.40854e-05, 0), \
                           37243, 107315, 107315, -nan)
reports[-1].sigmaresid = ValErr(0.171019, 0.000369146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0120349, None, 0.000524118, None, 0.011756, None, 0.00047258, None, 0.011756, None, 0.00047258, None, 0.0139489, None, 0.000493399, None, 0.0139489, None, 0.000493399, None, 0.171031, None, 0.00382654, None, 0.171031, None, 0.00382654, None)
reports[-1].CovMatrix = ['2.83849e-07','-8.2799e-09','-1.49805e-09','4.66121e-11','0','0','0','0','0','-8.2799e-09','0.000179522','5.9641e-10','1.42502e-09','0','0','0','0','0','-1.49805e-09','5.9641e-10','1.984e-10','1.19798e-12','0','0','0','0','0','4.66121e-11','1.42502e-09','1.19798e-12','1.36269e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 102522
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0211872, 0.000544389, 0), \
                           ValErr(0.0427044, 0.0136709, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000107946, 1.44761e-05, 0), \
                           36611.9, 102522, 102522, -nan)
reports[-1].sigmaresid = ValErr(0.169306, 0.000373894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0221777, None, -1.5934e-05, None, 0.022146, None, -2.96015e-05, None, 0.022146, None, -2.96015e-05, None, 0.0226962, None, -1.69487e-05, None, 0.0226962, None, -1.69487e-05, None, 0.16936, None, 0.00383176, None, 0.16936, None, 0.00383176, None)
reports[-1].CovMatrix = ['2.9636e-07','3.9744e-08','-1.87421e-09','4.59593e-11','0','0','0','0','0','3.9744e-08','0.000186893','-1.07243e-09','1.48999e-09','0','0','0','0','0','-1.87421e-09','-1.07243e-09','2.09559e-10','1.26266e-12','0','0','0','0','0','4.59593e-11','1.48999e-09','1.26266e-12','1.39797e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 102909
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0306662, 0.000545892, 0), \
                           ValErr(0.0348946, 0.0137034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000102488, 1.457e-05, 0), \
                           35151.7, 102909, 102909, -nan)
reports[-1].sigmaresid = ValErr(0.171956, 0.000379031, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0312356, None, -0.001682, None, 0.0313953, None, -0.00162618, None, 0.0313953, None, -0.00162618, None, 0.0321075, None, -0.00165032, None, 0.0321075, None, -0.00165032, None, 0.172002, None, 0.00378837, None, 0.172002, None, 0.00378837, None)
reports[-1].CovMatrix = ['2.97998e-07','-2.16464e-08','-1.50492e-09','4.85854e-11','0','0','0','0','0','-2.16464e-08','0.000187783','1.08443e-09','1.48866e-09','0','0','0','0','0','-1.50492e-09','1.08443e-09','2.12286e-10','1.30831e-12','0','0','0','0','0','4.85854e-11','1.48866e-09','1.30831e-12','1.43664e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 102422
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0286902, 0.000541582, 0), \
                           ValErr(-0.0183832, 0.0135836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000155372, 1.43785e-05, 0), \
                           36629.3, 102422, 102422, -nan)
reports[-1].sigmaresid = ValErr(0.169218, 0.000373882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0304035, None, -0.000549665, None, 0.029958, None, -0.000548778, None, 0.029958, None, -0.000548778, None, 0.0304934, None, -0.000531189, None, 0.0304934, None, -0.000531189, None, 0.169316, None, 0.00381295, None, 0.169316, None, 0.00381295, None)
reports[-1].CovMatrix = ['2.93311e-07','1.26818e-08','-1.68509e-09','4.78468e-11','0','0','0','0','0','1.26818e-08','0.000184513','5.16157e-10','1.49233e-09','0','0','0','0','0','-1.68509e-09','5.16157e-10','2.0674e-10','1.29728e-12','0','0','0','0','0','4.78468e-11','1.49233e-09','1.29728e-12','1.39787e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 106558
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0224724, 0.000476153, 0), \
                           ValErr(0.0547397, 0.0119402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.88906e-05, 1.26155e-05, 0), \
                           49661, 106558, 106558, -nan)
reports[-1].sigmaresid = ValErr(0.151832, 0.000336023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0231257, None, 0.000621358, None, 0.0230829, None, 0.000640256, None, 0.0230829, None, 0.000640256, None, 0.0223767, None, 0.000691977, None, 0.0223767, None, 0.000691977, None, 0.151875, None, 0.00387685, None, 0.151875, None, 0.00387685, None)
reports[-1].CovMatrix = ['2.26722e-07','-3.02969e-08','-1.21121e-09','-2.2858e-09','0','0','0','0','0','-3.02969e-08','0.000142568','-1.13046e-09','-2.82325e-08','0','0','0','0','0','-1.21121e-09','-1.13046e-09','1.59151e-10','9.36876e-11','0','0','0','0','0','-2.2858e-09','-2.82325e-08','9.36876e-11','1.12911e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 106484
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112058, 0.00047959, 0), \
                           ValErr(-0.0185322, 0.0119913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.65184e-05, 1.25764e-05, 0), \
                           48524.3, 106484, 106484, -nan)
reports[-1].sigmaresid = ValErr(0.153411, 0.000337048, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0115309, None, 0.000785405, None, 0.0118273, None, 0.000774572, None, 0.0118273, None, 0.000774572, None, 0.0118662, None, 0.000808667, None, 0.0118662, None, 0.000808667, None, 0.153447, None, 0.00399311, None, 0.153447, None, 0.00399311, None)
reports[-1].CovMatrix = ['2.30007e-07','-1.2446e-08','-1.11164e-09','-2.33734e-10','0','0','0','0','0','-1.2446e-08','0.000143791','1.48552e-10','8.36903e-09','0','0','0','0','0','-1.11164e-09','1.48552e-10','1.58167e-10','3.55529e-11','0','0','0','0','0','-2.33734e-10','8.36903e-09','3.55529e-11','1.13602e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 89191
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000723756, 0.000526086, 0), \
                           ValErr(-0.0820008, 0.0132553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.76813e-05, 1.32896e-05, 0), \
                           41040.6, 89191, 89191, -nan)
reports[-1].sigmaresid = ValErr(0.15273, 0.000361618, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000533001, None, 0.00038544, None, -0.000163306, None, 0.000358838, None, -0.000163306, None, 0.000358838, None, -0.000365752, None, 0.000386473, None, -0.000365752, None, 0.000386473, None, 0.152779, None, 0.00369275, None, 0.152779, None, 0.00369275, None)
reports[-1].CovMatrix = ['2.76767e-07','6.55672e-08','-1.63927e-09','5.02126e-11','0','0','0','0','0','6.55672e-08','0.000175703','-1.24788e-09','1.59137e-09','0','0','0','0','0','-1.63927e-09','-1.24788e-09','1.76613e-10','1.24143e-12','0','0','0','0','0','5.02126e-11','1.59137e-09','1.24143e-12','1.30767e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 104766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0255202, 0.000481257, 0), \
                           ValErr(-0.057792, 0.0120034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.37176e-05, 1.27727e-05, 0), \
                           48736.9, 104766, 104766, -nan)
reports[-1].sigmaresid = ValErr(0.15196, 0.000335738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0248981, None, -0.000453509, None, -0.0249552, None, -0.000440965, None, -0.0249552, None, -0.000440965, None, -0.0241824, None, -0.000419484, None, -0.0241824, None, -0.000419484, None, 0.152002, None, 0.00385348, None, 0.152002, None, 0.00385348, None)
reports[-1].CovMatrix = ['2.31608e-07','-8.54289e-10','-1.27644e-09','1.75274e-09','0','0','0','0','0','-8.54289e-10','0.000144082','4.90294e-11','1.12879e-09','0','0','0','0','0','-1.27644e-09','4.90294e-11','1.63141e-10','-8.09113e-11','0','0','0','0','0','1.75274e-09','1.12879e-09','-8.09113e-11','1.1272e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 107697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0353673, 0.00047685, 0), \
                           ValErr(0.0253649, 0.0119217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.47315e-05, 1.25892e-05, 0), \
                           49461, 107697, 107697, -nan)
reports[-1].sigmaresid = ValErr(0.152865, 0.000329419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0343761, None, -0.000436568, None, -0.0346181, None, -0.000449419, None, -0.0346181, None, -0.000449419, None, -0.0344993, None, -0.000447914, None, -0.0344993, None, -0.000447914, None, 0.152909, None, 0.00383378, None, 0.152909, None, 0.00383378, None)
reports[-1].CovMatrix = ['2.27386e-07','3.27159e-09','-1.26794e-09','1.05107e-10','0','0','0','0','0','3.27159e-09','0.000142126','1.31537e-10','8.77915e-11','0','0','0','0','0','-1.26794e-09','1.31537e-10','1.58488e-10','2.93512e-12','0','0','0','0','0','1.05107e-10','8.77915e-11','2.93512e-12','1.08517e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 102925
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0363515, 0.000485506, 0), \
                           ValErr(-0.0229007, 0.0120993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.73271e-05, 1.28252e-05, 0), \
                           47997.7, 102925, 102925, -nan)
reports[-1].sigmaresid = ValErr(0.151787, 0.000334894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0367863, None, -0.000306873, None, -0.0365589, None, -0.000245986, None, -0.0365589, None, -0.000245986, None, -0.0374574, None, -0.000268553, None, -0.0374574, None, -0.000268553, None, 0.151793, None, 0.00415987, None, 0.151793, None, 0.00415987, None)
reports[-1].CovMatrix = ['2.35716e-07','2.52148e-08','-1.3167e-09','4.35305e-10','0','0','0','0','0','2.52148e-08','0.000146392','-7.70642e-11','-5.56774e-10','0','0','0','0','0','-1.3167e-09','-7.70642e-11','1.64487e-10','-1.5936e-11','0','0','0','0','0','4.35305e-10','-5.56774e-10','-1.5936e-11','1.12154e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 98797
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0513686, 0.000495226, 0), \
                           ValErr(-0.0321059, 0.0122864, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.55239e-06, 1.30398e-05, 0), \
                           45981.3, 98797, 98797, -nan)
reports[-1].sigmaresid = ValErr(0.151928, 0.000341783, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0513174, None, -0.000703526, None, -0.0512838, None, -0.00073774, None, -0.0512838, None, -0.00073774, None, -0.0521183, None, -0.000806542, None, -0.0521183, None, -0.000806542, None, 0.151933, None, 0.00386188, None, 0.151933, None, 0.00386188, None)
reports[-1].CovMatrix = ['2.45249e-07','4.46501e-08','-1.40511e-09','4.70627e-11','0','0','0','0','0','4.46501e-08','0.000150956','-1.53728e-09','1.38003e-09','0','0','0','0','0','-1.40511e-09','-1.53728e-09','1.70037e-10','1.1694e-12','0','0','0','0','0','4.70627e-11','1.38003e-09','1.1694e-12','1.16815e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 103625
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0565218, 0.000487639, 0), \
                           ValErr(0.0151668, 0.0149427, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.72758e-06, 1.31033e-05, 0), \
                           48032.3, 103625, 103625, -nan)
reports[-1].sigmaresid = ValErr(0.152215, 0.000339034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0566634, None, -0.000479739, None, -0.056539, None, -0.000446703, None, -0.056539, None, -0.000446703, None, -0.0564035, None, -0.000469854, None, -0.0564035, None, -0.000469854, None, 0.152217, None, 0.00390054, None, 0.152217, None, 0.00390054, None)
reports[-1].CovMatrix = ['2.37792e-07','-4.51537e-07','-1.50534e-09','3.07719e-09','0','0','0','0','0','-4.51537e-07','0.000223283','2.93775e-08','-4.82727e-07','0','0','0','0','0','-1.50534e-09','2.93775e-08','1.71696e-10','-1.90011e-10','0','0','0','0','0','3.07719e-09','-4.82727e-07','-1.90011e-10','1.14944e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 95527
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0595771, 0.000503293, 0), \
                           ValErr(-0.0646175, 0.0122127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.55848e-05, 1.29051e-05, 0), \
                           44360.7, 95527, 95527, -nan)
reports[-1].sigmaresid = ValErr(0.152085, 0.000347943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0592184, None, -0.000858573, None, -0.059422, None, -0.000817086, None, -0.059422, None, -0.000817086, None, -0.0604667, None, -0.000843575, None, -0.0604667, None, -0.000843575, None, 0.15211, None, 0.00383399, None, 0.15211, None, 0.00383399, None)
reports[-1].CovMatrix = ['2.53304e-07','-1.38394e-07','-1.35804e-09','4.57924e-11','0','0','0','0','0','-1.38394e-07','0.00014915','1.88624e-09','1.39867e-09','0','0','0','0','0','-1.35804e-09','1.88624e-09','1.66542e-10','1.2256e-12','0','0','0','0','0','4.57924e-11','1.39867e-09','1.2256e-12','1.21064e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 103134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0495343, 0.000485363, 0), \
                           ValErr(0.0365233, 0.0121666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.54795e-05, 1.27551e-05, 0), \
                           47550, 103134, 103134, -nan)
reports[-1].sigmaresid = ValErr(0.152592, 0.000335981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0493064, None, -0.000134441, None, -0.0493418, None, -0.000160311, None, -0.0493418, None, -0.000160311, None, -0.0484797, None, -0.000187321, None, -0.0484797, None, -0.000187321, None, 0.152601, None, 0.00397409, None, 0.152601, None, 0.00397409, None)
reports[-1].CovMatrix = ['2.35577e-07','1.71005e-08','-1.26316e-09','4.4163e-11','0','0','0','0','0','1.71005e-08','0.000148026','5.70934e-10','1.35645e-09','0','0','0','0','0','-1.26316e-09','5.70934e-10','1.62693e-10','1.16215e-12','0','0','0','0','0','4.4163e-11','1.35645e-09','1.16215e-12','1.12883e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 103954
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0394974, 0.000482146, 0), \
                           ValErr(-0.0062843, 0.0121722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.88034e-05, 1.26952e-05, 0), \
                           47761.1, 103954, 103954, -nan)
reports[-1].sigmaresid = ValErr(0.152837, 0.000334868, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0389764, None, -0.00119425, None, -0.0392896, None, -0.00113307, None, -0.0392896, None, -0.00113307, None, -0.0393991, None, -0.00115505, None, -0.0393991, None, -0.00115505, None, 0.152841, None, 0.00385384, None, 0.152841, None, 0.00385384, None)
reports[-1].CovMatrix = ['2.32464e-07','2.041e-07','-1.11432e-09','4.00996e-10','0','0','0','0','0','2.041e-07','0.000148163','-1.88767e-11','-4.0955e-10','0','0','0','0','0','-1.11432e-09','-1.88767e-11','1.61169e-10','-2.32169e-12','0','0','0','0','0','4.00996e-10','-4.0955e-10','-2.32169e-12','1.12137e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 103754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0222384, 0.000483199, 0), \
                           ValErr(0.0549021, 0.012105, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.78202e-05, 1.26767e-05, 0), \
                           48036, 103754, 103754, -nan)
reports[-1].sigmaresid = ValErr(0.152298, 0.000334331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.021619, None, -0.0013454, None, -0.0221129, None, -0.0012946, None, -0.0221129, None, -0.0012946, None, -0.0216954, None, -0.00136085, None, -0.0216954, None, -0.00136085, None, 0.152314, None, 0.0038696, None, 0.152314, None, 0.0038696, None)
reports[-1].CovMatrix = ['2.33481e-07','4.24777e-08','-1.26241e-09','4.40004e-11','0','0','0','0','0','4.24777e-08','0.000146531','-5.19978e-10','1.34913e-09','0','0','0','0','0','-1.26241e-09','-5.19978e-10','1.607e-10','1.13402e-12','0','0','0','0','0','4.40004e-11','1.34913e-09','1.13402e-12','1.11777e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 102530
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00903673, 0.000484349, 0), \
                           ValErr(0.0524541, 0.0122744, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.22985e-05, 1.27587e-05, 0), \
                           47712.7, 102530, 102530, -nan)
reports[-1].sigmaresid = ValErr(0.151937, 0.000335523, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00834226, None, -0.000655303, None, -0.00879708, None, -0.000611795, None, -0.00879708, None, -0.000611795, None, -0.0101944, None, -0.000655121, None, -0.0101944, None, -0.000655121, None, 0.151952, None, 0.00391282, None, 0.151952, None, 0.00391282, None)
reports[-1].CovMatrix = ['2.34594e-07','-2.11393e-07','-1.22075e-09','4.24219e-11','0','0','0','0','0','-2.11393e-07','0.00015066','4.1152e-10','1.32566e-09','0','0','0','0','0','-1.22075e-09','4.1152e-10','1.62785e-10','1.17096e-12','0','0','0','0','0','4.24219e-11','1.32566e-09','1.17096e-12','1.12575e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 100698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00245199, 0.000493142, 0), \
                           ValErr(-0.0316448, 0.0123889, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.79958e-05, 1.29387e-05, 0), \
                           45966.3, 100698, 100698, -nan)
reports[-1].sigmaresid = ValErr(0.153291, 0.000341579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00277003, None, -0.000233274, None, 0.00282026, None, -0.000248096, None, 0.00282026, None, -0.000248096, None, 0.00307661, None, -0.000264714, None, 0.00307661, None, -0.000264714, None, 0.153307, None, 0.00400594, None, 0.153307, None, 0.00400594, None)
reports[-1].CovMatrix = ['2.43189e-07','-6.33882e-10','-1.28321e-09','4.49526e-11','0','0','0','0','0','-6.33882e-10','0.000153486','2.00328e-10','1.39849e-09','0','0','0','0','0','-1.28321e-09','2.00328e-10','1.67411e-10','1.19753e-12','0','0','0','0','0','4.49526e-11','1.39849e-09','1.19753e-12','1.16676e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 105959
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0152475, 0.000478183, 0), \
                           ValErr(0.0173397, 0.0120545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.87452e-05, 1.26024e-05, 0), \
                           48752.9, 105959, 105959, -nan)
reports[-1].sigmaresid = ValErr(0.152735, 0.000331784, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0156116, None, -0.00237601, None, 0.0155092, None, -0.0022838, None, 0.0155092, None, -0.0022838, None, 0.0163321, None, -0.0023523, None, 0.0163321, None, -0.0023523, None, 0.152743, None, 0.00394578, None, 0.152743, None, 0.00394578, None)
reports[-1].CovMatrix = ['2.28659e-07','1.45674e-07','-1.14918e-09','4.44559e-11','0','0','0','0','0','1.45674e-07','0.000145312','2.39282e-09','1.38033e-09','0','0','0','0','0','-1.14918e-09','2.39282e-09','1.5882e-10','1.1607e-12','0','0','0','0','0','4.44559e-11','1.38033e-09','1.1607e-12','1.10081e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 105169
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0233003, 0.0004835, 0), \
                           ValErr(0.0382258, 0.0121369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000175283, 1.27524e-05, 0), \
                           48111.1, 105169, 105169, -nan)
reports[-1].sigmaresid = ValErr(0.15314, 0.000333911, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0248347, None, -0.000248288, None, 0.0247163, None, -0.000249803, None, 0.0247163, None, -0.000249803, None, 0.0248593, None, -0.000276253, None, 0.0248593, None, -0.000276253, None, 0.153285, None, 0.00382899, None, 0.153285, None, 0.00382899, None)
reports[-1].CovMatrix = ['2.33772e-07','3.88832e-08','-1.32334e-09','4.32713e-11','0','0','0','0','0','3.88832e-08','0.000147304','1.01826e-10','1.34633e-09','0','0','0','0','0','-1.32334e-09','1.01826e-10','1.62622e-10','1.13914e-12','0','0','0','0','0','4.32713e-11','1.34633e-09','1.13914e-12','1.11496e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 104946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0302463, 0.000483455, 0), \
                           ValErr(0.0324055, 0.0120917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41968e-05, 1.28326e-05, 0), \
                           48353.4, 104946, 104946, -nan)
reports[-1].sigmaresid = ValErr(0.152638, 0.000334489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0305517, None, 0.00128499, None, 0.0303962, None, 0.0012208, None, 0.0303962, None, 0.0012208, None, 0.0312055, None, 0.00123247, None, 0.0312055, None, 0.00123247, None, 0.152646, None, 0.00385568, None, 0.152646, None, 0.00385568, None)
reports[-1].CovMatrix = ['2.33728e-07','1.41735e-07','-1.26665e-09','-1.21106e-09','0','0','0','0','0','1.41735e-07','0.00014621','-1.42418e-09','-9.66002e-10','0','0','0','0','0','-1.26665e-09','-1.42418e-09','1.64676e-10','4.6313e-11','0','0','0','0','0','-1.21106e-09','-9.66002e-10','4.6313e-11','1.11883e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 106496
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.026658, 0.000475756, 0), \
                           ValErr(-0.0552279, 0.0119114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.48303e-05, 1.25209e-05, 0), \
                           50053.8, 106496, 106496, -nan)
reports[-1].sigmaresid = ValErr(0.151232, 0.00032769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0272926, None, 0.000239384, None, 0.0274855, None, 0.000244753, None, 0.0274855, None, 0.000244753, None, 0.0270976, None, 0.000243669, None, 0.0270976, None, 0.000243669, None, 0.151287, None, 0.00382126, None, 0.151287, None, 0.00382126, None)
reports[-1].CovMatrix = ['2.26344e-07','3.29946e-08','-1.34719e-09','4.14374e-11','0','0','0','0','0','3.29946e-08','0.00014188','-8.64295e-11','1.31701e-09','0','0','0','0','0','-1.34719e-09','-8.64295e-11','1.56774e-10','1.10733e-12','0','0','0','0','0','4.14374e-11','1.31701e-09','1.10733e-12','1.0738e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 59021
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0193433, 0.00215169, 0), \
                           ValErr(-0.165601, 0.0525249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143546, 4.52428e-05, 0), \
                           -41383.4, 59021, 59021, -nan)
reports[-1].sigmaresid = ValErr(0.487835, 0.00141989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.015971, None, -0.000277786, None, -0.0171474, None, -0.000279549, None, -0.0171474, None, -0.000279549, None, -0.0162671, None, -0.000285957, None, -0.0162671, None, -0.000285957, None, 0.487921, None, 0.0046179, None, 0.487921, None, 0.0046179, None)
reports[-1].CovMatrix = ['4.62975e-06','-5.10306e-06','-3.48075e-08','8.10189e-10','0','0','0','0','0','-5.10306e-06','0.00275887','6.75367e-08','2.99267e-08','0','0','0','0','0','-3.48075e-08','6.75367e-08','2.04691e-09','1.87327e-11','0','0','0','0','0','8.10189e-10','2.99267e-08','1.87327e-11','2.01608e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 57893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00796291, 0.0021762, 0), \
                           ValErr(0.0179429, 0.0523658, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.48504e-05, 4.62295e-05, 0), \
                           -39343.5, 57893, 57893, -nan)
reports[-1].sigmaresid = ValErr(0.477424, 0.00140306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00684419, None, 0.00037194, None, -0.00709763, None, 0.000414867, None, -0.00709763, None, 0.000414867, None, -0.00767361, None, 0.000394872, None, -0.00767361, None, 0.000394872, None, 0.477429, None, 0.00473758, None, 0.477429, None, 0.00473758, None)
reports[-1].CovMatrix = ['4.73583e-06','1.44089e-06','-4.13131e-08','8.10166e-10','0','0','0','0','0','1.44089e-06','0.00274218','-5.3115e-08','2.9233e-08','0','0','0','0','0','-4.13131e-08','-5.3115e-08','2.13717e-09','1.57783e-11','0','0','0','0','0','8.10166e-10','2.9233e-08','1.57783e-11','1.96857e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 52731
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0081005, 0.00248894, 0), \
                           ValErr(-0.121564, 0.0544437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000235153, 5.30219e-05, 0), \
                           -33772.5, 52731, 52731, -nan)
reports[-1].sigmaresid = ValErr(0.459108, 0.00141373, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0141828, None, -0.00172579, None, -0.014819, None, -0.00164259, None, -0.014819, None, -0.00164259, None, -0.0161205, None, -0.0016981, None, -0.0161205, None, -0.0016981, None, 0.45921, None, 0.0045204, None, 0.45921, None, 0.0045204, None)
reports[-1].CovMatrix = ['6.19484e-06','-9.01295e-06','-7.84931e-08','6.025e-10','0','0','0','0','0','-9.01295e-06','0.00296411','1.71822e-07','2.97389e-08','0','0','0','0','0','-7.84931e-08','1.71822e-07','2.81133e-09','1.64942e-11','0','0','0','0','0','6.025e-10','2.97389e-08','1.64942e-11','1.99864e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 55320
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0330278, 0.00235027, 0), \
                           ValErr(-0.0142987, 0.054181, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.00997e-05, 4.97124e-05, 0), \
                           -37238.9, 55320, 55320, -nan)
reports[-1].sigmaresid = ValErr(0.474362, 0.00142611, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0349949, None, -0.000756922, None, -0.0344863, None, -0.000728974, None, -0.0344863, None, -0.000728974, None, -0.0343335, None, -0.000750836, None, -0.0343335, None, -0.000750836, None, 0.474369, None, 0.00439431, None, 0.474369, None, 0.00439431, None)
reports[-1].CovMatrix = ['5.52379e-06','8.17813e-07','-5.99885e-08','7.74507e-10','0','0','0','0','0','8.17813e-07','0.00293558','-1.9674e-08','3.09033e-08','0','0','0','0','0','-5.99885e-08','-1.9674e-08','2.47132e-09','1.61728e-11','0','0','0','0','0','7.74507e-10','3.09033e-08','1.61728e-11','2.0338e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 59002
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0571896, 0.00216333, 0), \
                           ValErr(-0.16954, 0.0520861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.2999e-05, 4.54969e-05, 0), \
                           -40686.3, 59002, 59002, -nan)
reports[-1].sigmaresid = ValErr(0.482216, 0.00140376, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0589115, None, 5.5114e-05, None, -0.0579918, None, 3.79743e-05, None, -0.0579918, None, 3.79743e-05, None, -0.0588556, None, 7.68851e-05, None, -0.0588556, None, 7.68851e-05, None, 0.482263, None, 0.00463566, None, 0.482263, None, 0.00463566, None)
reports[-1].CovMatrix = ['4.67999e-06','-4.05026e-08','-3.91084e-08','8.08147e-10','0','0','0','0','0','-4.05026e-08','0.00271296','1.07854e-08','2.97501e-08','0','0','0','0','0','-3.91084e-08','1.07854e-08','2.06997e-09','1.70897e-11','0','0','0','0','0','8.08147e-10','2.97501e-08','1.70897e-11','1.97055e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 58859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0237635, 0.00217244, 0), \
                           ValErr(-0.036982, 0.0522246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000209845, 4.57845e-05, 0), \
                           -41180.5, 58859, 58859, -nan)
reports[-1].sigmaresid = ValErr(0.487097, 0.00141969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0282235, None, 0.000347834, None, -0.0275624, None, 0.00031677, None, -0.0275624, None, 0.00031677, None, -0.0277733, None, 0.000345973, None, -0.0277733, None, 0.000345973, None, 0.487186, None, 0.00450522, None, 0.487186, None, 0.00450522, None)
reports[-1].CovMatrix = ['4.71949e-06','5.63733e-07','-3.79876e-08','8.48386e-10','0','0','0','0','0','5.63733e-07','0.00272741','-1.58412e-08','3.02135e-08','0','0','0','0','0','-3.79876e-08','-1.58412e-08','2.09622e-09','1.75665e-11','0','0','0','0','0','8.48386e-10','3.02135e-08','1.75665e-11','2.01553e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 56046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0535626, 0.00224644, 0), \
                           ValErr(0.00741318, 0.0535307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000159951, 4.73253e-05, 0), \
                           -38290.2, 56046, 56046, -nan)
reports[-1].sigmaresid = ValErr(0.479148, 0.00143114, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0518861, None, -0.000217706, None, -0.0502696, None, -0.000229968, None, -0.0502696, None, -0.000229968, None, -0.047269, None, -0.000229798, None, -0.047269, None, -0.000229798, None, 0.479197, None, 0.00446877, None, 0.479197, None, 0.00446877, None)
reports[-1].CovMatrix = ['5.0465e-06','-3.75713e-06','-4.60911e-08','7.74388e-10','0','0','0','0','0','-3.75713e-06','0.00286553','7.71345e-08','3.08582e-08','0','0','0','0','0','-4.60911e-08','7.71345e-08','2.23968e-09','1.80648e-11','0','0','0','0','0','7.74388e-10','3.08582e-08','1.80648e-11','2.04817e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 60431
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0726456, 0.00211781, 0), \
                           ValErr(0.0254269, 0.0517369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.56735e-05, 4.47781e-05, 0), \
                           -41850.3, 60431, 60431, -nan)
reports[-1].sigmaresid = ValErr(0.483643, 0.00139117, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0705292, None, -0.000146777, None, -0.0720367, None, -0.000112851, None, -0.0720367, None, -0.000112851, None, -0.0704069, None, -9.42602e-05, None, -0.0704069, None, -9.42602e-05, None, 0.483646, None, 0.00474234, None, 0.483646, None, 0.00474234, None)
reports[-1].CovMatrix = ['4.48514e-06','2.6418e-06','-3.50749e-08','8.39494e-10','0','0','0','0','0','2.6418e-06','0.00267671','-6.37966e-08','2.92443e-08','0','0','0','0','0','-3.50749e-08','-6.37966e-08','2.00508e-09','1.65111e-11','0','0','0','0','0','8.39494e-10','2.92443e-08','1.65111e-11','1.93535e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 51578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0640283, 0.00236757, 0), \
                           ValErr(0.0490864, 0.0542911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.55428e-05, 4.89451e-05, 0), \
                           -33166, 51578, 51578, -nan)
reports[-1].sigmaresid = ValErr(0.460283, 0.0014331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0649172, None, -7.06372e-05, None, -0.0664694, None, -0.000108955, None, -0.0664694, None, -0.000108955, None, -0.0672802, None, -8.72613e-05, None, -0.0672802, None, -8.72613e-05, None, 0.460304, None, 0.00443203, None, 0.460304, None, 0.00443203, None)
reports[-1].CovMatrix = ['5.60539e-06','5.20518e-06','-5.98178e-08','8.061e-10','0','0','0','0','0','5.20518e-06','0.00294753','-6.7975e-08','3.10833e-08','0','0','0','0','0','-5.98178e-08','-6.7975e-08','2.39562e-09','1.4795e-11','0','0','0','0','0','8.061e-10','3.10833e-08','1.4795e-11','2.05379e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 61810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0662339, 0.00209431, 0), \
                           ValErr(0.0467029, 0.0513618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000140917, 4.47239e-05, 0), \
                           -43294.3, 61810, 61810, -nan)
reports[-1].sigmaresid = ValErr(0.487485, 0.00138649, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0641479, None, -0.000203762, None, -0.0639271, None, -0.000228752, None, -0.0639271, None, -0.000228752, None, -0.0648855, None, -0.000212804, None, -0.0648855, None, -0.000212804, None, 0.487528, None, 0.00473556, None, 0.487528, None, 0.00473556, None)
reports[-1].CovMatrix = ['4.38612e-06','1.74048e-06','-3.29044e-08','8.40655e-10','0','0','0','0','0','1.74048e-06','0.00263804','-7.05172e-08','2.8727e-08','0','0','0','0','0','-3.29044e-08','-7.05172e-08','2.00023e-09','1.67915e-11','0','0','0','0','0','8.40655e-10','2.8727e-08','1.67915e-11','1.92235e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 50659
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0469221, 0.0023324, 0), \
                           ValErr(0.0321118, 0.0534287, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.22622e-05, 4.98968e-05, 0), \
                           -33964.6, 50659, 50659, -nan)
reports[-1].sigmaresid = ValErr(0.473084, 0.00148626, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0515083, None, -0.000791387, None, -0.0486115, None, -0.00076851, None, -0.0486115, None, -0.00076851, None, -0.047686, None, -0.000763938, None, -0.047686, None, -0.000763938, None, 0.473098, None, 0.00460813, None, 0.473098, None, 0.00460813, None)
reports[-1].CovMatrix = ['5.4401e-06','3.25883e-06','-5.04028e-08','9.07784e-10','0','0','0','0','0','3.25883e-06','0.00285462','-4.9874e-08','3.20222e-08','0','0','0','0','0','-5.04028e-08','-4.9874e-08','2.48969e-09','1.81167e-11','0','0','0','0','0','9.07784e-10','3.20222e-08','1.81167e-11','2.20897e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 61071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0507644, 0.00209823, 0), \
                           ValErr(-0.0185213, 0.0511017, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000125252, 4.4414e-05, 0), \
                           -42348.4, 61071, 61071, -nan)
reports[-1].sigmaresid = ValErr(0.48408, 0.00138512, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0497936, None, -0.000476593, None, -0.0486475, None, -0.000419344, None, -0.0486475, None, -0.000419344, None, -0.0479338, None, -0.000461923, None, -0.0479338, None, -0.000461923, None, 0.48411, None, 0.00468439, None, 0.48411, None, 0.00468439, None)
reports[-1].CovMatrix = ['4.40257e-06','-9.39899e-07','-3.33947e-08','7.94786e-10','0','0','0','0','0','-9.39899e-07','0.00261138','1.65703e-08','2.89014e-08','0','0','0','0','0','-3.33947e-08','1.65703e-08','1.9726e-09','1.71067e-11','0','0','0','0','0','7.94786e-10','2.89014e-08','1.71067e-11','1.91855e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 49534
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0327158, 0.00247862, 0), \
                           ValErr(-0.0812668, 0.0554759, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000238568, 5.0088e-05, 0), \
                           -32584.9, 49534, 49534, -nan)
reports[-1].sigmaresid = ValErr(0.467148, 0.00148419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0242955, None, -0.000249556, None, -0.0263635, None, -0.00026315, None, -0.0263635, None, -0.00026315, None, -0.026996, None, -0.000262158, None, -0.026996, None, -0.000262158, None, 0.467263, None, 0.00441162, None, 0.467263, None, 0.00441162, None)
reports[-1].CovMatrix = ['6.14354e-06','6.10298e-06','-6.59584e-08','8.7164e-10','0','0','0','0','0','6.10298e-06','0.00307758','-1.01529e-07','3.2943e-08','0','0','0','0','0','-6.59584e-08','-1.01529e-07','2.50881e-09','1.50994e-11','0','0','0','0','0','8.7164e-10','3.2943e-08','1.50994e-11','2.20281e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 48497
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0216772, 0.002491, 0), \
                           ValErr(0.0949226, 0.0570148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000201065, 5.0291e-05, 0), \
                           -31571.9, 48497, 48497, -nan)
reports[-1].sigmaresid = ValErr(0.463972, 0.00148977, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0136446, None, -0.000579774, None, -0.0162842, None, -0.000512134, None, -0.0162842, None, -0.000512134, None, -0.0206889, None, -0.000518526, None, -0.0206889, None, -0.000518526, None, 0.464061, None, 0.0046931, None, 0.464061, None, 0.0046931, None)
reports[-1].CovMatrix = ['6.20511e-06','-4.25301e-06','-6.67854e-08','7.62912e-10','0','0','0','0','0','-4.25301e-06','0.00325068','4.794e-08','3.29589e-08','0','0','0','0','0','-6.67854e-08','4.794e-08','2.52919e-09','1.6776e-11','0','0','0','0','0','7.62912e-10','3.29589e-08','1.6776e-11','2.21942e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 46659
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0107253, 0.00256223, 0), \
                           ValErr(0.237425, 0.0576874, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.03908e-05, 5.01846e-05, 0), \
                           -30348.2, 46659, 46659, -nan)
reports[-1].sigmaresid = ValErr(0.463701, 0.00151794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00927546, None, -0.000817459, None, -0.0101293, None, -0.000766141, None, -0.0101293, None, -0.000766141, None, -0.0114615, None, -0.000765191, None, -0.0114615, None, -0.000765191, None, 0.463789, None, 0.00461638, None, 0.463789, None, 0.00461638, None)
reports[-1].CovMatrix = ['6.56502e-06','6.33863e-06','-7.01338e-08','8.95337e-10','0','0','0','0','0','6.33863e-06','0.00332784','-1.02368e-07','3.50148e-08','0','0','0','0','0','-7.01338e-08','-1.02368e-07','2.51849e-09','1.52089e-11','0','0','0','0','0','8.95337e-10','3.50148e-08','1.52089e-11','2.30415e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 45563
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.013477, 0.00265379, 0), \
                           ValErr(-0.0943719, 0.0581807, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000163697, 5.32139e-05, 0), \
                           -29535.7, 45563, 45563, -nan)
reports[-1].sigmaresid = ValErr(0.462689, 0.00153274, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00526462, None, -0.000623047, None, -0.00900933, None, -0.000515763, None, -0.00900933, None, -0.000515763, None, -0.00921154, None, -0.000543136, None, -0.00921154, None, -0.000543136, None, 0.462754, None, 0.00475603, None, 0.462754, None, 0.00475603, None)
reports[-1].CovMatrix = ['7.04261e-06','-1.32808e-05','-8.12068e-08','6.93971e-10','0','0','0','0','0','-1.32808e-05','0.003385','2.13375e-07','3.42622e-08','0','0','0','0','0','-8.12068e-08','2.13375e-07','2.83172e-09','1.88699e-11','0','0','0','0','0','6.93971e-10','3.42622e-08','1.88699e-11','2.34929e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 50194
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0192577, 0.00241428, 0), \
                           ValErr(0.201086, 0.0626723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000180355, 5.06928e-05, 0), \
                           -33633.4, 50194, 50194, -nan)
reports[-1].sigmaresid = ValErr(0.472901, 0.00149255, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0183301, None, -0.000269886, None, -0.0169104, None, -0.000286244, None, -0.0169104, None, -0.000286244, None, -0.0165193, None, -0.000265934, None, -0.0165193, None, -0.000265934, None, 0.47301, None, 0.00444625, None, 0.47301, None, 0.00444625, None)
reports[-1].CovMatrix = ['5.82875e-06','2.94261e-05','-5.46595e-08','1.21151e-09','0','0','0','0','0','2.94261e-05','0.00392781','-3.09831e-08','4.61463e-08','0','0','0','0','0','-5.46595e-08','-3.09831e-08','2.56976e-09','1.81998e-11','0','0','0','0','0','1.21151e-09','4.61463e-08','1.81998e-11','2.22771e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 55418
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00843417, 0.00224656, 0), \
                           ValErr(-0.0733973, 0.0527489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.7191e-05, 4.74161e-05, 0), \
                           -36809, 55418, 55418, -nan)
reports[-1].sigmaresid = ValErr(0.470137, 0.00141216, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00587845, None, -0.000173589, None, -0.00671595, None, -0.000156546, None, -0.00671595, None, -0.000156546, None, -0.00606947, None, -0.000175629, None, -0.00606947, None, -0.000175629, None, 0.470155, None, 0.00451031, None, 0.470155, None, 0.00451031, None)
reports[-1].CovMatrix = ['5.04705e-06','2.72739e-06','-4.87631e-08','7.92606e-10','0','0','0','0','0','2.72739e-06','0.00278245','-4.73135e-08','2.98764e-08','0','0','0','0','0','-4.87631e-08','-4.73135e-08','2.24829e-09','1.59971e-11','0','0','0','0','0','7.92606e-10','2.98764e-08','1.59971e-11','1.9942e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 58292
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0123052, 0.00211259, 0), \
                           ValErr(0.0556274, 0.0503984, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000188708, 4.37622e-05, 0), \
                           -38305.8, 58292, 58292, -nan)
reports[-1].sigmaresid = ValErr(0.466824, 0.00136721, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0162709, None, -9.90577e-05, None, -0.0160036, None, -5.76318e-05, None, -0.0160036, None, -5.76318e-05, None, -0.0162619, None, -7.39297e-05, None, -0.0162619, None, -7.39297e-05, None, 0.466903, None, 0.00427655, None, 0.466903, None, 0.00427655, None)
reports[-1].CovMatrix = ['4.46303e-06','2.08036e-06','-3.72288e-08','7.68117e-10','0','0','0','0','0','2.08036e-06','0.00254','-3.23395e-08','2.74149e-08','0','0','0','0','0','-3.72288e-08','-3.23395e-08','1.91513e-09','1.51021e-11','0','0','0','0','0','7.68117e-10','2.74149e-08','1.51021e-11','1.86925e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 45511
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0132145, 0.00283184, 0), \
                           ValErr(-0.0616133, 0.0568019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.82585e-05, 5.58765e-05, 0), \
                           -27307.6, 45511, 45511, -nan)
reports[-1].sigmaresid = ValErr(0.44091, 0.00146142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0114167, None, -0.000961792, None, -0.0140502, None, -0.000899747, None, -0.0140502, None, -0.000899747, None, -0.014048, None, -0.000939586, None, -0.014048, None, -0.000939586, None, 0.440917, None, 0.00460437, None, 0.440917, None, 0.00460437, None)
reports[-1].CovMatrix = ['8.0193e-06','1.66851e-05','-1.07945e-07','8.4571e-10','0','0','0','0','0','1.66851e-05','0.00322646','-2.7749e-07','3.1888e-08','0','0','0','0','0','-1.07945e-07','-2.7749e-07','3.12218e-09','1.08564e-11','0','0','0','0','0','8.4571e-10','3.1888e-08','1.08564e-11','2.13576e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 53181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00983668, 0.00228096, 0), \
                           ValErr(-0.0648952, 0.0518258, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.15771e-05, 4.66492e-05, 0), \
                           -33053.7, 53181, 53181, -nan)
reports[-1].sigmaresid = ValErr(0.450496, 0.00138133, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0112494, None, -0.000684648, None, -0.0117173, None, -0.000664959, None, -0.0117173, None, -0.000664959, None, -0.0140877, None, -0.000645977, None, -0.0140877, None, -0.000645977, None, 0.450512, None, 0.00447147, None, 0.450512, None, 0.00447147, None)
reports[-1].CovMatrix = ['5.20277e-06','-6.23349e-06','-5.48484e-08','6.21585e-10','0','0','0','0','0','-6.23349e-06','0.00268591','1.14151e-07','2.72701e-08','0','0','0','0','0','-5.48484e-08','1.14151e-07','2.17615e-09','1.5202e-11','0','0','0','0','0','6.21585e-10','2.72701e-08','1.5202e-11','1.90808e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 50729
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0309955, 0.00229879, 0), \
                           ValErr(-0.0278651, 0.0522186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00018906, 4.67606e-05, 0), \
                           -30400, 50729, 50729, -nan)
reports[-1].sigmaresid = ValErr(0.440575, 0.00138317, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0388084, None, -0.000320294, None, -0.035892, None, -0.000323868, None, -0.035892, None, -0.000323868, None, -0.0344861, None, -0.000307374, None, -0.0344861, None, -0.000307374, None, 0.440646, None, 0.00441745, None, 0.440646, None, 0.00441745, None)
reports[-1].CovMatrix = ['5.28443e-06','-6.77483e-06','-5.63753e-08','6.03447e-10','0','0','0','0','0','-6.77483e-06','0.00272678','1.25766e-07','2.71542e-08','0','0','0','0','0','-5.63753e-08','1.25766e-07','2.18656e-09','1.49025e-11','0','0','0','0','0','6.03447e-10','2.71542e-08','1.49025e-11','1.91317e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 59942
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0417263, 0.00206159, 0), \
                           ValErr(0.0751504, 0.0502612, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000108201, 4.31414e-05, 0), \
                           -40042.2, 59942, 59942, -nan)
reports[-1].sigmaresid = ValErr(0.471931, 0.00136301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0465004, None, -0.000556886, None, -0.0435474, None, -0.000537262, None, -0.0435474, None, -0.000537262, None, -0.0427937, None, -0.000565044, None, -0.0427937, None, -0.000565044, None, 0.471965, None, 0.00440105, None, 0.471965, None, 0.00440105, None)
reports[-1].CovMatrix = ['4.25017e-06','-5.18299e-07','-3.15413e-08','7.73185e-10','0','0','0','0','0','-5.18299e-07','0.00252619','6.3607e-09','2.72135e-08','0','0','0','0','0','-3.15413e-08','6.3607e-09','1.86118e-09','1.58218e-11','0','0','0','0','0','7.73185e-10','2.72135e-08','1.58218e-11','1.85779e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 56804
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0395659, 0.00209394, 0), \
                           ValErr(0.0800122, 0.0496779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.84084e-05, 4.33063e-05, 0), \
                           -35159.3, 56804, 56804, -nan)
reports[-1].sigmaresid = ValErr(0.449338, 0.00133312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0383967, None, -1.92089e-05, None, -0.0384212, None, -5.38691e-05, None, -0.0384212, None, -5.38691e-05, None, -0.0408328, None, -2.21472e-05, None, -0.0408328, None, -2.21472e-05, None, 0.449356, None, 0.00436519, None, 0.449356, None, 0.00436519, None)
reports[-1].CovMatrix = ['4.38457e-06','3.95894e-06','-3.93992e-08','7.13963e-10','0','0','0','0','0','3.95894e-06','0.00246789','-7.09684e-08','2.56033e-08','0','0','0','0','0','-3.93992e-08','-7.09684e-08','1.87544e-09','1.32174e-11','0','0','0','0','0','7.13963e-10','2.56033e-08','1.32174e-11','1.7772e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 59206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0590711, 0.00206045, 0), \
                           ValErr(-0.0451222, 0.0493309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24969e-05, 4.30008e-05, 0), \
                           -38005.1, 59206, 59206, -nan)
reports[-1].sigmaresid = ValErr(0.459769, 0.0013361, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0574865, None, 0.000579456, None, -0.0586436, None, 0.000526645, None, -0.0586436, None, 0.000526645, None, -0.0587538, None, 0.00054785, None, -0.0587538, None, 0.00054785, None, 0.459776, None, 0.00439109, None, 0.459776, None, 0.00439109, None)
reports[-1].CovMatrix = ['4.24546e-06','3.2798e-07','-3.53311e-08','7.34795e-10','0','0','0','0','0','3.2798e-07','0.00243353','-1.66082e-08','2.56704e-08','0','0','0','0','0','-3.53311e-08','-1.66082e-08','1.84907e-09','1.42557e-11','0','0','0','0','0','7.34795e-10','2.56704e-08','1.42557e-11','1.78516e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 52261
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0734523, 0.00231619, 0), \
                           ValErr(-0.0173465, 0.0523973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00012022, 4.70443e-05, 0), \
                           -32926.3, 52261, 52261, -nan)
reports[-1].sigmaresid = ValErr(0.454343, 0.00140533, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0695614, None, 0.000206765, None, -0.0704139, None, 0.000203762, None, -0.0704139, None, 0.000203762, None, -0.0724549, None, 0.00019357, None, -0.0724549, None, 0.00019357, None, 0.454372, None, 0.00443822, None, 0.454372, None, 0.00443822, None)
reports[-1].CovMatrix = ['5.36474e-06','-6.6054e-08','-5.59572e-08','7.16839e-10','0','0','0','0','0','-6.6054e-08','0.00274548','1.55335e-09','2.85113e-08','0','0','0','0','0','-5.59572e-08','1.55335e-09','2.21316e-09','1.47853e-11','0','0','0','0','0','7.16839e-10','2.85113e-08','1.47853e-11','1.97496e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 53431
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0615798, 0.00219428, 0), \
                           ValErr(-0.0740977, 0.0522237, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000162037, 4.44332e-05, 0), \
                           -34039.9, 53431, 53431, -nan)
reports[-1].sigmaresid = ValErr(0.457555, 0.00139969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0560651, None, -2.23002e-05, None, -0.0582469, None, 2.38228e-05, None, -0.0582469, None, 2.38228e-05, None, -0.0562279, None, 7.73838e-05, None, -0.0562279, None, 7.73838e-05, None, 0.457622, None, 0.00466307, None, 0.457622, None, 0.00466307, None)
reports[-1].CovMatrix = ['4.81486e-06','-4.70487e-06','-4.1945e-08','7.07454e-10','0','0','0','0','0','-4.70487e-06','0.00272732','3.99815e-08','2.77885e-08','0','0','0','0','0','-4.1945e-08','3.99815e-08','1.97431e-09','1.57354e-11','0','0','0','0','0','7.07454e-10','2.77885e-08','1.57354e-11','1.95913e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 51549
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0515365, 0.00233111, 0), \
                           ValErr(-0.0108003, 0.0524881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00016747, 4.80899e-05, 0), \
                           -32527, 51549, 51549, -nan)
reports[-1].sigmaresid = ValErr(0.454778, 0.00141636, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0550982, None, -0.000243284, None, -0.0556915, None, -0.000206597, None, -0.0556915, None, -0.000206597, None, -0.0565279, None, -0.000196169, None, -0.0565279, None, -0.000196169, None, 0.454831, None, 0.0045302, None, 0.454831, None, 0.0045302, None)
reports[-1].CovMatrix = ['5.43405e-06','-1.94059e-06','-5.73372e-08','7.08068e-10','0','0','0','0','0','-1.94059e-06','0.002755','3.92903e-08','2.88268e-08','0','0','0','0','0','-5.73372e-08','3.92903e-08','2.31264e-09','1.5435e-11','0','0','0','0','0','7.08068e-10','2.88268e-08','1.5435e-11','2.00608e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 54357
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0421685, 0.00217528, 0), \
                           ValErr(-0.0272059, 0.0519355, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.0532e-05, 4.51077e-05, 0), \
                           -35151, 54357, 54357, -nan)
reports[-1].sigmaresid = ValErr(0.461963, 0.00140108, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.03914, None, -0.000559173, None, -0.0403865, None, -0.000533586, None, -0.0403865, None, -0.000533586, None, -0.0399377, None, -0.000562391, None, -0.0399377, None, -0.000562391, None, 0.461982, None, 0.00441654, None, 0.461982, None, 0.00441654, None)
reports[-1].CovMatrix = ['4.73185e-06','-3.11043e-06','-4.04647e-08','7.53355e-10','0','0','0','0','0','-3.11043e-06','0.0026973','7.21358e-08','2.85608e-08','0','0','0','0','0','-4.04647e-08','7.21358e-08','2.0347e-09','1.58503e-11','0','0','0','0','0','7.53355e-10','2.85608e-08','1.58503e-11','1.96303e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 60952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0459838, 0.00203001, 0), \
                           ValErr(0.0415767, 0.0496949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.70398e-05, 4.21035e-05, 0), \
                           -39761, 60952, 60952, -nan)
reports[-1].sigmaresid = ValErr(0.464588, 0.00133064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0464848, None, -0.000687391, None, -0.044673, None, -0.000646378, None, -0.044673, None, -0.000646378, None, -0.0453481, None, -0.000660737, None, -0.0453481, None, -0.000660737, None, 0.464603, None, 0.00438716, None, 0.464603, None, 0.00438716, None)
reports[-1].CovMatrix = ['4.12094e-06','5.64719e-06','-3.18745e-08','7.7833e-10','0','0','0','0','0','5.64719e-06','0.00246958','-8.91125e-08','2.64818e-08','0','0','0','0','0','-3.18745e-08','-8.91125e-08','1.77271e-09','1.40071e-11','0','0','0','0','0','7.7833e-10','2.64818e-08','1.40071e-11','1.77059e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 41896
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0326811, 0.00253522, 0), \
                           ValErr(0.178003, 0.0556689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.10228e-05, 4.80586e-05, 0), \
                           -23445.9, 41896, 41896, -nan)
reports[-1].sigmaresid = ValErr(0.423451, 0.00146286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0309072, None, -0.00122466, None, -0.0312969, None, -0.00102596, None, -0.0312969, None, -0.00102596, None, -0.0310693, None, -0.00108827, None, -0.0310693, None, -0.00108827, None, 0.423509, None, 0.00477473, None, 0.423509, None, 0.00477473, None)
reports[-1].CovMatrix = ['6.42732e-06','4.17218e-06','-7.03794e-08','7.28066e-10','0','0','0','0','0','4.17218e-06','0.00309903','-4.00902e-08','3.06285e-08','0','0','0','0','0','-7.03794e-08','-4.00902e-08','2.30963e-09','1.34111e-11','0','0','0','0','0','7.28066e-10','3.06285e-08','1.34111e-11','2.13995e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 46544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0146845, 0.00244821, 0), \
                           ValErr(-0.175256, 0.0557089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000139964, 4.78265e-05, 0), \
                           -29300.8, 46544, 46544, -nan)
reports[-1].sigmaresid = ValErr(0.454113, 0.00148839, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.013383, None, -0.000647827, None, -0.0109791, None, -0.000628173, None, -0.0109791, None, -0.000628173, None, -0.00889838, None, -0.00063092, None, -0.00889838, None, -0.00063092, None, 0.454204, None, 0.00448639, None, 0.454204, None, 0.00448639, None)
reports[-1].CovMatrix = ['5.99373e-06','-4.94089e-07','-5.97909e-08','7.93877e-10','0','0','0','0','0','-4.94089e-07','0.00310348','4.9979e-08','3.25142e-08','0','0','0','0','0','-5.97909e-08','4.9979e-08','2.28737e-09','1.63111e-11','0','0','0','0','0','7.93877e-10','3.25142e-08','1.63111e-11','2.21531e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 40268
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0129368, 0.00254882, 0), \
                           ValErr(-0.118176, 0.0570446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000100975, 4.72773e-05, 0), \
                           -22776.3, 40268, 40268, -nan)
reports[-1].sigmaresid = ValErr(0.425997, 0.0015011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0124532, None, -0.000700415, None, -0.0158735, None, -0.000680408, None, -0.0158735, None, -0.000680408, None, -0.0146077, None, -0.000670824, None, -0.0146077, None, -0.000670824, None, 0.426047, None, 0.00451295, None, 0.426047, None, 0.00451295, None)
reports[-1].CovMatrix = ['6.4965e-06','4.99575e-06','-6.66692e-08','8.17551e-10','0','0','0','0','0','4.99575e-06','0.00325409','-9.95947e-08','3.12645e-08','0','0','0','0','0','-6.66692e-08','-9.95947e-08','2.23515e-09','1.29475e-11','0','0','0','0','0','8.17551e-10','3.12645e-08','1.29475e-11','2.25331e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 51277
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0245504, 0.00230291, 0), \
                           ValErr(-0.031195, 0.0518932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.36046e-05, 4.75813e-05, 0), \
                           -30914.5, 51277, 51277, -nan)
reports[-1].sigmaresid = ValErr(0.442176, 0.00138076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0237904, None, -0.000415152, None, -0.0221257, None, -0.00038956, None, -0.0221257, None, -0.00038956, None, -0.0243487, None, -0.000405996, None, -0.0243487, None, -0.000405996, None, 0.442194, None, 0.00424477, None, 0.442194, None, 0.00424477, None)
reports[-1].CovMatrix = ['5.30341e-06','6.34468e-06','-5.80362e-08','7.31856e-10','0','0','0','0','0','6.34468e-06','0.0026929','-1.43242e-07','2.70935e-08','0','0','0','0','0','-5.80362e-08','-1.43242e-07','2.26398e-09','1.23918e-11','0','0','0','0','0','7.31856e-10','2.70935e-08','1.23918e-11','1.90651e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 56151
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.007901, 0.00214994, 0), \
                           ValErr(-0.0828185, 0.0523422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.957e-05, 4.46235e-05, 0), \
                           -37424.2, 56151, 56151, -nan)
reports[-1].sigmaresid = ValErr(0.471213, 0.00140612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00728972, None, 0.000160141, None, -0.00643414, None, 0.000147128, None, -0.00643414, None, 0.000147128, None, -0.00705372, None, 0.000177091, None, -0.00705372, None, 0.000177091, None, 0.471237, None, 0.00442096, None, 0.471237, None, 0.00442096, None)
reports[-1].CovMatrix = ['4.62223e-06','-1.08404e-06','-3.64668e-08','7.93114e-10','0','0','0','0','0','-1.08404e-06','0.0027397','7.58281e-08','3.01716e-08','0','0','0','0','0','-3.64668e-08','7.58281e-08','1.99126e-09','1.76729e-11','0','0','0','0','0','7.93114e-10','3.01716e-08','1.76729e-11','1.97719e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 55691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00556369, 0.00213341, 0), \
                           ValErr(-0.0294519, 0.0520365, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.92779e-05, 4.37624e-05, 0), \
                           -36462.1, 55691, 55691, -nan)
reports[-1].sigmaresid = ValErr(0.465699, 0.0013954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00266078, None, 0.0001902, None, -0.00428022, None, 0.000222191, None, -0.00428022, None, 0.000222191, None, -0.00356534, None, 0.000217307, None, -0.00356534, None, 0.000217307, None, 0.465711, None, 0.00463196, None, 0.465711, None, 0.00463196, None)
reports[-1].CovMatrix = ['4.55146e-06','1.75253e-07','-3.5477e-08','7.90104e-10','0','0','0','0','0','1.75253e-07','0.0027078','-8.67681e-09','2.8596e-08','0','0','0','0','0','-3.5477e-08','-8.67681e-09','1.91515e-09','1.60672e-11','0','0','0','0','0','7.90104e-10','2.8596e-08','1.60672e-11','1.94713e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 21954
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00940083, 0.00881847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000117028, 0.000192411, 0), \
                           -36609.7, 21954, 21954, -nan)
reports[-1].sigmaresid = ValErr(1.28226, 0.00611935, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00412526, None, -0.00176658, None, -0.0104313, None, -0.00154054, None, -0.0104313, None, -0.00154054, None, 0.0105923, None, -0.00154396, None, 0.0105923, None, -0.00154396, None, 1.28228, None, 0.00775684, None, 1.28228, None, 0.00775684, None)
reports[-1].CovMatrix = ['7.77654e-05','-3.26099e-07','2.796e-08','0','0','0','0','0','0','-3.26099e-07','3.70221e-08','6.11225e-10','0','0','0','0','0','0','2.796e-08','6.11225e-10','3.74465e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 20248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0440314, 0.00882621, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000280332, 0.000192923, 0), \
                           -33044.9, 20248, 20248, -nan)
reports[-1].sigmaresid = ValErr(1.23747, 0.00614934, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0410662, None, -0.00215209, None, -0.0418399, None, -0.00202572, None, -0.0418399, None, -0.00202572, None, -0.0204593, None, -0.00215979, None, -0.0204593, None, -0.00215979, None, 1.23753, None, 0.00690951, None, 1.23753, None, 0.00690951, None)
reports[-1].CovMatrix = ['7.79019e-05','-2.90873e-07','2.84368e-08','0','0','0','0','0','0','-2.90873e-07','3.72191e-08','6.21599e-10','0','0','0','0','0','0','2.84368e-08','6.21599e-10','3.78144e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 18759
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0599628, 0.00947901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000199878, 0.000218522, 0), \
                           -31460.7, 18759, 18759, -nan)
reports[-1].sigmaresid = ValErr(1.29455, 0.00668339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0612326, None, 0.00100013, None, -0.0593074, None, 0.0011667, None, -0.0593074, None, 0.0011667, None, -0.0504631, None, 0.00121567, None, -0.0504631, None, 0.00121567, None, 1.29458, None, 0.00739377, None, 1.29458, None, 0.00739377, None)
reports[-1].CovMatrix = ['8.98517e-05','-1.56954e-07','3.71911e-08','0','0','0','0','0','0','-1.56954e-07','4.77519e-08','8.62905e-10','0','0','0','0','0','0','3.71911e-08','8.62905e-10','4.46677e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 7196
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0894484, 0.0165586, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.72795e-05, 0.000365785, 0), \
                           -12415.8, 7196, 7196, -nan)
reports[-1].sigmaresid = ValErr(1.35857, 0.0113245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0924606, None, 0.000949421, None, -0.0884441, None, 0.00108708, None, -0.0884441, None, 0.00108708, None, -0.0822573, None, 0.00107844, None, -0.0822573, None, 0.00107844, None, 1.35858, None, 0.00755789, None, 1.35858, None, 0.00755789, None)
reports[-1].CovMatrix = ['0.000274187','1.53871e-06','1.5562e-07','0','0','0','0','0','0','1.53871e-06','1.33799e-07','3.43478e-09','0','0','0','0','0','0','1.5562e-07','3.43478e-09','0.000128246','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 9650
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0332494, 0.0130351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000605558, 0.000284927, 0), \
                           -15929.6, 9650, 9650, -nan)
reports[-1].sigmaresid = ValErr(1.26087, 0.0090759, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0272994, None, -0.000143638, None, -0.028417, None, -8.87431e-06, None, -0.028417, None, -8.87431e-06, None, -0.009074, None, 2.16069e-05, None, -0.009074, None, 2.16069e-05, None, 1.26116, None, 0.00750542, None, 1.26116, None, 0.00750542, None)
reports[-1].CovMatrix = ['0.000169915','6.47853e-07','8.84662e-08','0','0','0','0','0','0','6.47853e-07','8.11835e-08','1.93519e-09','0','0','0','0','0','0','8.84662e-08','1.93519e-09','8.23723e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 5827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.096013, 0.0179671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000190954, 0.00037938, 0), \
                           -9863.24, 5827, 5827, -nan)
reports[-1].sigmaresid = ValErr(1.31487, 0.0121799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.109958, None, 0.0021673, None, -0.0985844, None, 0.00225621, None, -0.0985844, None, 0.00225621, None, -0.0723551, None, 0.0022135, None, -0.0723551, None, 0.0022135, None, 1.3149, None, 0.00738581, None, 1.3149, None, 0.00738581, None)
reports[-1].CovMatrix = ['0.000322817','1.93868e-06','1.85878e-07','0','0','0','0','0','0','1.93868e-06','1.43929e-07','3.92447e-09','0','0','0','0','0','0','1.85878e-07','3.92447e-09','0.000148352','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 12002
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00740417, 0.0124948, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000550194, 0.000285596, 0), \
                           -20643.1, 12002, 12002, -nan)
reports[-1].sigmaresid = ValErr(1.35126, 0.00872161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0203204, None, 0.000529702, None, 0.0035538, None, 0.00069892, None, 0.0035538, None, 0.00069892, None, 0.0175293, None, 0.00074047, None, 0.0175293, None, 0.00074047, None, 1.35147, None, 0.00787861, None, 1.35147, None, 0.00787861, None)
reports[-1].CovMatrix = ['0.00015612','5.70245e-07','8.23918e-08','0','0','0','0','0','0','5.70245e-07','8.15653e-08','1.8778e-09','0','0','0','0','0','0','8.23918e-08','1.8778e-09','7.60667e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 17324
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0366675, 0.00947037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.91316e-05, 0.000214142, 0), \
                           -28328, 17324, 17324, -nan)
reports[-1].sigmaresid = ValErr(1.24141, 0.00666926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0360144, None, 0.000256158, None, 0.0368236, None, 0.000394561, None, 0.0368236, None, 0.000394561, None, 0.0458765, None, 0.000492376, None, 0.0458765, None, 0.000492376, None, 1.24141, None, 0.0075077, None, 1.24141, None, 0.0075077, None)
reports[-1].CovMatrix = ['8.9688e-05','-1.82972e-07','3.60042e-08','0','0','0','0','0','0','-1.82972e-07','4.58569e-08','8.13576e-10','0','0','0','0','0','0','3.60042e-08','8.13576e-10','4.44791e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 17610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00134023, 0.00960079, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.38554e-05, 0.000215142, 0), \
                           -29156.9, 17610, 17610, -nan)
reports[-1].sigmaresid = ValErr(1.26714, 0.00675203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00316903, None, 0.00120826, None, 0.00125931, None, 0.00135234, None, 0.00125931, None, 0.00135234, None, -0.0106723, None, 0.00146998, None, -0.0106723, None, 0.00146998, None, 1.26714, None, 0.00730265, None, 1.26714, None, 0.00730265, None)
reports[-1].CovMatrix = ['9.21751e-05','-2.14762e-07','3.7803e-08','0','0','0','0','0','0','-2.14762e-07','4.62861e-08','8.33925e-10','0','0','0','0','0','0','3.7803e-08','8.33925e-10','4.559e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 22222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0256217, 0.00853245, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00046936, 0.000186463, 0), \
                           -36507.3, 22222, 22222, -nan)
reports[-1].sigmaresid = ValErr(1.25095, 0.00593379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0419555, None, 0.00156709, None, -0.0295061, None, 0.00161143, None, -0.0295061, None, 0.00161143, None, -0.0470714, None, 0.00175396, None, -0.0470714, None, 0.00175396, None, 1.25113, None, 0.00722658, None, 1.25113, None, 0.00722658, None)
reports[-1].CovMatrix = ['7.28027e-05','-2.87816e-07','2.63168e-08','0','0','0','0','0','0','-2.87816e-07','3.47683e-08','5.7537e-10','0','0','0','0','0','0','2.63168e-08','5.7537e-10','3.52099e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 20149
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0333835, 0.00902822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000105655, 0.000200292, 0), \
                           -33346, 20149, 20149, -nan)
reports[-1].sigmaresid = ValErr(1.26622, 0.00630763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0286229, None, 0.00138404, None, -0.0326493, None, 0.0015472, None, -0.0326493, None, 0.0015472, None, -0.0470253, None, 0.00161089, None, -0.0470253, None, 0.00161089, None, 1.26622, None, 0.0075036, None, 1.26622, None, 0.0075036, None)
reports[-1].CovMatrix = ['8.15088e-05','-2.78722e-07','3.05888e-08','0','0','0','0','0','0','-2.78722e-07','4.01169e-08','6.79562e-10','0','0','0','0','0','0','3.05888e-08','6.79562e-10','3.97862e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 17739
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0431922, 0.00951112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127094, 0.00021455, 0), \
                           -29237.5, 17739, 17739, -nan)
reports[-1].sigmaresid = ValErr(1.25768, 0.00667714, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.048323, None, 0.00123285, None, -0.0438657, None, 0.00127927, None, -0.0438657, None, 0.00127927, None, -0.0325402, None, 0.0012968, None, -0.0325402, None, 0.0012968, None, 1.25769, None, 0.00703512, None, 1.25769, None, 0.00703512, None)
reports[-1].CovMatrix = ['9.04614e-05','-2.43964e-07','3.52541e-08','0','0','0','0','0','0','-2.43964e-07','4.60315e-08','7.9825e-10','0','0','0','0','0','0','3.52541e-08','7.9825e-10','4.45843e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 17066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0213821, 0.00963833, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.56922e-05, 0.000218169, 0), \
                           -28122.1, 17066, 17066, -nan)
reports[-1].sigmaresid = ValErr(1.25724, 0.00680521, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0147443, None, -0.000487467, None, -0.0211941, None, -0.000361177, None, -0.0211941, None, -0.000361177, None, -0.02737, None, -0.000281957, None, -0.02737, None, -0.000281957, None, 1.25722, None, 0.00718001, None, 1.25722, None, 0.00718001, None)
reports[-1].CovMatrix = ['9.28973e-05','-1.15036e-07','3.68115e-08','0','0','0','0','0','0','-1.15036e-07','4.75977e-08','8.49288e-10','0','0','0','0','0','0','3.68115e-08','8.49288e-10','4.6311e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 22040
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0824692, 0.00851228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000166023, 0.000187805, 0), \
                           -35970.4, 22040, 22040, -nan)
reports[-1].sigmaresid = ValErr(1.23752, 0.00589428, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0773334, None, 0.000241037, None, -0.0839924, None, 0.000338297, None, -0.0839924, None, 0.000338297, None, -0.0930515, None, 0.000380409, None, -0.0930515, None, 0.000380409, None, 1.23755, None, 0.00715093, None, 1.23755, None, 0.00715093, None)
reports[-1].CovMatrix = ['7.24588e-05','-3.23834e-07','2.52545e-08','0','0','0','0','0','0','-3.23834e-07','3.52706e-08','5.78378e-10','0','0','0','0','0','0','2.52545e-08','5.78378e-10','3.47426e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 17736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0681345, 0.00941037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000889079, 0.000206428, 0), \
                           -28998.6, 17736, 17736, -nan)
reports[-1].sigmaresid = ValErr(1.2412, 0.00659017, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0720465, None, -0.00392605, None, -0.0737399, None, -0.00371385, None, -0.0737399, None, -0.00371385, None, -0.0889841, None, -0.00372704, None, -0.0889841, None, -0.00372704, None, 1.24185, None, 0.00728755, None, 1.24185, None, 0.00728755, None)
reports[-1].CovMatrix = ['8.8555e-05','-2.68663e-07','3.36398e-08','0','0','0','0','0','0','-2.68663e-07','4.26125e-08','7.41832e-10','0','0','0','0','0','0','3.36398e-08','7.41832e-10','4.34305e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 17287
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0186239, 0.00984716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000612307, 0.000228758, 0), \
                           -28965.3, 17287, 17287, -nan)
reports[-1].sigmaresid = ValErr(1.29255, 0.00695143, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0231729, None, -0.000527802, None, -0.0171122, None, -0.000405545, None, -0.0171122, None, -0.000405545, None, -0.0191534, None, -0.000399441, None, -0.0191534, None, -0.000399441, None, 1.29282, None, 0.00735781, None, 1.29282, None, 0.00735781, None)
reports[-1].CovMatrix = ['9.69666e-05','1.29887e-07','4.63595e-08','0','0','0','0','0','0','1.29887e-07','5.233e-08','1.04759e-09','0','0','0','0','0','0','4.63595e-08','1.04759e-09','4.83224e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 18959
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0835927, 0.00921786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.54205e-06, 0.000210372, 0), \
                           -31351.4, 18959, 18959, -nan)
reports[-1].sigmaresid = ValErr(1.26453, 0.00649392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.061634, None, 0.00233969, None, -0.0835822, None, 0.00238297, None, -0.0835822, None, 0.00238297, None, -0.0841187, None, 0.00238068, None, -0.0841187, None, 0.00238068, None, 1.26453, None, 0.00732745, None, 1.26453, None, 0.00732745, None)
reports[-1].CovMatrix = ['8.49689e-05','-1.66533e-07','3.46278e-08','0','0','0','0','0','0','-1.66533e-07','4.42564e-08','7.94012e-10','0','0','0','0','0','0','3.46278e-08','7.94012e-10','4.21711e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 19888
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.049048, 0.00895052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.67683e-05, 0.000200512, 0), \
                           -32504.1, 19888, 19888, -nan)
reports[-1].sigmaresid = ValErr(1.24038, 0.00621936, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0502072, None, -0.000929676, None, -0.048661, None, -0.000868426, None, -0.048661, None, -0.000868426, None, -0.0406992, None, -0.000912772, None, -0.0406992, None, -0.000912772, None, 1.24039, None, 0.00700447, None, 1.24039, None, 0.00700447, None)
reports[-1].CovMatrix = ['8.01119e-05','-3.3257e-07','2.86958e-08','0','0','0','0','0','0','-3.3257e-07','4.02051e-08','6.55093e-10','0','0','0','0','0','0','2.86958e-08','6.55093e-10','3.86804e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 22948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0318004, 0.00860986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000157215, 0.000190423, 0), \
                           -38209.1, 22948, 22948, -nan)
reports[-1].sigmaresid = ValErr(1.27901, 0.00597018, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0244313, None, -0.00118332, None, -0.0331925, None, -0.000943408, None, -0.0331925, None, -0.000943408, None, -0.0171056, None, -0.000975179, None, -0.0171056, None, -0.000975179, None, 1.27903, None, 0.00746749, None, 1.27903, None, 0.00746749, None)
reports[-1].CovMatrix = ['7.41297e-05','-3.21103e-07','2.65072e-08','0','0','0','0','0','0','-3.21103e-07','3.6261e-08','5.89424e-10','0','0','0','0','0','0','2.65072e-08','5.89424e-10','3.5643e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 21928
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.046468, 0.00863089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000930318, 0.000191337, 0), \
                           -36143.4, 21928, 21928, -nan)
reports[-1].sigmaresid = ValErr(1.25776, 0.00600598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0615582, None, -0.000713872, None, -0.0539176, None, -0.000538778, None, -0.0539176, None, -0.000538778, None, -0.0599914, None, -0.000473813, None, -0.0599914, None, -0.000473813, None, 1.25844, None, 0.00751434, None, 1.25844, None, 0.00751434, None)
reports[-1].CovMatrix = ['7.44922e-05','-2.93217e-07','2.70265e-08','0','0','0','0','0','0','-2.93217e-07','3.66097e-08','6.03869e-10','0','0','0','0','0','0','2.70265e-08','6.03869e-10','3.60718e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 19528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0192173, 0.00910982, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000518691, 0.000207267, 0), \
                           -32230.9, 19528, 19528, -nan)
reports[-1].sigmaresid = ValErr(1.26056, 0.00637852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.012633, None, -0.000530647, None, -0.0160346, None, -0.000383115, None, -0.0160346, None, -0.000383115, None, -0.00788339, None, -0.000270937, None, -0.00788339, None, -0.000270937, None, 1.26076, None, 0.00711626, None, 1.26076, None, 0.00711626, None)
reports[-1].CovMatrix = ['8.29889e-05','-2.63629e-07','3.16741e-08','0','0','0','0','0','0','-2.63629e-07','4.29595e-08','7.19454e-10','0','0','0','0','0','0','3.16741e-08','7.19454e-10','4.06855e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 18923
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(7.32149e-05, 0.00926908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000474719, 0.0002073, 0), \
                           -31272, 18923, 18923, -nan)
reports[-1].sigmaresid = ValErr(1.26321, 0.00649328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0026577, None, 0.000136762, None, -0.00281507, None, 0.000289672, None, -0.00281507, None, 0.000289672, None, 8.18895e-05, None, 0.000354816, None, 8.18895e-05, None, 0.000354816, None, 1.26338, None, 0.0073568, None, 1.26338, None, 0.0073568, None)
reports[-1].CovMatrix = ['8.59158e-05','-2.61426e-07','3.29457e-08','0','0','0','0','0','0','-2.61426e-07','4.29735e-08','7.35579e-10','0','0','0','0','0','0','3.29457e-08','7.35579e-10','4.21627e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 20121
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0663069, 0.00893894, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000269047, 0.000194939, 0), \
                           -33097.4, 20121, 20121, -nan)
reports[-1].sigmaresid = ValErr(1.25355, 0.00624886, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0666949, None, -0.00036768, None, -0.0681623, None, -0.000136546, None, -0.0681623, None, -0.000136546, None, -0.0604381, None, -0.00017101, None, -0.0604381, None, -0.00017101, None, 1.25361, None, 0.00780821, None, 1.25361, None, 0.00780821, None)
reports[-1].CovMatrix = ['7.99047e-05','-2.62122e-07','2.99665e-08','0','0','0','0','0','0','-2.62122e-07','3.80011e-08','6.6219e-10','0','0','0','0','0','0','2.99665e-08','6.6219e-10','3.90483e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 14819
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0325197, 0.0100524, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000524871, 0.000215944, 0), \
                           -23918.3, 14819, 14819, -nan)
reports[-1].sigmaresid = ValErr(1.21543, 0.00705999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0413715, None, 9.73936e-05, None, -0.0353589, None, 0.000257574, None, -0.0353589, None, 0.000257574, None, -0.0278083, None, 0.000311971, None, -0.0278083, None, 0.000311971, None, 1.21567, None, 0.00735469, None, 1.21567, None, 0.00735469, None)
reports[-1].CovMatrix = ['0.00010105','-2.52167e-07','3.92011e-08','0','0','0','0','0','0','-2.52167e-07','4.66317e-08','8.43641e-10','0','0','0','0','0','0','3.92011e-08','8.43641e-10','4.98435e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 11863
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0381924, 0.0121616, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000694959, 0.000260628, 0), \
                           -19850.1, 11863, 11863, -nan)
reports[-1].sigmaresid = ValErr(1.28961, 0.00837227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0394857, None, 0.000399383, None, -0.0455997, None, 0.000647121, None, -0.0455997, None, 0.000647121, None, -0.0380989, None, 0.000758924, None, -0.0380989, None, 0.000758924, None, 1.28999, None, 0.00735124, None, 1.28999, None, 0.00735124, None)
reports[-1].CovMatrix = ['0.000147905','-7.239e-07','5.10079e-08','0','0','0','0','0','0','-7.239e-07','6.7927e-08','1.09569e-09','0','0','0','0','0','0','5.10079e-08','1.09569e-09','7.00951e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 13498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.110707, 0.0107348, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000196135, 0.000231137, 0), \
                           -22023.5, 13498, 13498, -nan)
reports[-1].sigmaresid = ValErr(1.23698, 0.00752853, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0991516, None, 0.00106488, None, -0.109549, None, 0.00120541, None, -0.109549, None, 0.00120541, None, -0.103644, None, 0.00125665, None, -0.103644, None, 0.00125665, None, 1.23701, None, 0.00701252, None, 1.23701, None, 0.00701252, None)
reports[-1].CovMatrix = ['0.000115235','-3.16647e-07','4.45207e-08','0','0','0','0','0','0','-3.16647e-07','5.34245e-08','9.85168e-10','0','0','0','0','0','0','4.45207e-08','9.85168e-10','5.66789e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 10365
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.112475, 0.0126403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000582483, 0.000257737, 0), \
                           -17104.5, 10365, 10365, -nan)
reports[-1].sigmaresid = ValErr(1.26021, 0.00875272, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.103617, None, 0.00167428, None, -0.106688, None, 0.00175892, None, -0.106688, None, 0.00175892, None, -0.10476, None, 0.00183043, None, -0.10476, None, 0.00183043, None, 1.26052, None, 0.00676351, None, 1.26052, None, 0.00676351, None)
reports[-1].CovMatrix = ['0.000159777','-6.59955e-07','5.64685e-08','0','0','0','0','0','0','-6.59955e-07','6.64282e-08','1.15164e-09','0','0','0','0','0','0','5.64685e-08','1.15164e-09','7.66103e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 8546
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0944319, 0.0139637, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00130917, 0.000278903, 0), \
                           -13893.9, 8546, 8546, -nan)
reports[-1].sigmaresid = ValErr(1.22978, 0.00940655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0629904, None, 0.00136896, None, -0.0744995, None, 0.00153288, None, -0.0744995, None, 0.00153288, None, -0.0761102, None, 0.00162412, None, -0.0761102, None, 0.00162412, None, 1.23136, None, 0.00746511, None, 1.23136, None, 0.00746511, None)
reports[-1].CovMatrix = ['0.000194985','-1.18388e-06','5.88638e-08','0','0','0','0','0','0','-1.18388e-06','7.77868e-08','1.17993e-09','0','0','0','0','0','0','5.88638e-08','1.17993e-09','8.84835e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 7823
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0515258, 0.0149928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000155995, 0.000308497, 0), \
                           -12960.1, 7823, 7823, -nan)
reports[-1].sigmaresid = ValErr(1.26836, 0.01014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0527361, None, -0.00155034, None, 0.0493103, None, -0.00134152, None, 0.0493103, None, -0.00134152, None, 0.0547306, None, -0.00128248, None, 0.0547306, None, -0.00128248, None, 1.26839, None, 0.00725624, None, 1.26839, None, 0.00725624, None)
reports[-1].CovMatrix = ['0.000224785','-1.34974e-06','7.20364e-08','0','0','0','0','0','0','-1.34974e-06','9.51701e-08','1.39637e-09','0','0','0','0','0','0','7.20364e-08','1.39637e-09','0.00010282','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 7712
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0361063, 0.0145377, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000901914, 0.000315891, 0), \
                           -12746.3, 7712, 7712, -nan)
reports[-1].sigmaresid = ValErr(1.26345, 0.0101732, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0426211, None, -0.000231804, None, 0.0301473, None, -0.000139083, None, 0.0301473, None, -0.000139083, None, 0.0183152, None, -4.39469e-05, None, 0.0183152, None, -4.39469e-05, None, 1.26412, None, 0.00690009, None, 1.26412, None, 0.00690009, None)
reports[-1].CovMatrix = ['0.000211346','-6.59306e-07','8.02666e-08','0','0','0','0','0','0','-6.59306e-07','9.97873e-08','1.74653e-09','0','0','0','0','0','0','8.02666e-08','1.74653e-09','0.000103495','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 7707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0393207, 0.0146705, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000292462, 0.000308755, 0), \
                           -12680.9, 7707, 7707, -nan)
reports[-1].sigmaresid = ValErr(1.25411, 0.0101013, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0415754, None, -0.00256899, None, 0.0361573, None, -0.0021143, None, 0.0361573, None, -0.0021143, None, 0.0491956, None, -0.00217288, None, 0.0491956, None, -0.00217288, None, 1.25419, None, 0.00745288, None, 1.25419, None, 0.00745288, None)
reports[-1].CovMatrix = ['0.000215223','-1.03088e-06','7.36723e-08','0','0','0','0','0','0','-1.03088e-06','9.53299e-08','1.54918e-09','0','0','0','0','0','0','7.36723e-08','1.54918e-09','0.000102037','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 12246
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0520542, 0.011398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.82978e-05, 0.000233799, 0), \
                           -19831.6, 12246, 12246, -nan)
reports[-1].sigmaresid = ValErr(1.222, 0.00780835, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0492803, None, -0.00213152, None, -0.0522732, None, -0.00184452, None, -0.0522732, None, -0.00184452, None, -0.038724, None, -0.00183731, None, -0.038724, None, -0.00183731, None, 1.22201, None, 0.00737411, None, 1.22201, None, 0.00737411, None)
reports[-1].CovMatrix = ['0.000129913','-6.60132e-07','4.255e-08','0','0','0','0','0','0','-6.60132e-07','5.4662e-08','8.93944e-10','0','0','0','0','0','0','4.255e-08','8.93944e-10','6.09705e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 13697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0331969, 0.0110427, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000254433, 0.000240163, 0), \
                           -22628.8, 13697, 13697, -nan)
reports[-1].sigmaresid = ValErr(1.26258, 0.00762834, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0265506, None, 0.000640361, None, -0.0356939, None, 0.000782889, None, -0.0356939, None, 0.000782889, None, -0.0163669, None, 0.00072883, None, -0.0163669, None, 0.00072883, None, 1.26263, None, 0.00720039, None, 1.26263, None, 0.00720039, None)
reports[-1].CovMatrix = ['0.000121941','-5.66172e-07','4.24426e-08','0','0','0','0','0','0','-5.66172e-07','5.76783e-08','9.30043e-10','0','0','0','0','0','0','4.24426e-08','9.30043e-10','5.81916e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 18544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0517342, 0.00931597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000176232, 0.000208102, 0), \
                           -30605.9, 18544, 18544, -nan)
reports[-1].sigmaresid = ValErr(1.2605, 0.00654528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0557958, None, -0.000304112, None, -0.0508447, None, -9.56985e-05, None, -0.0508447, None, -9.56985e-05, None, -0.0270809, None, -5.10696e-05, None, -0.0270809, None, -5.10696e-05, None, 1.26053, None, 0.00777055, None, 1.26053, None, 0.00777055, None)
reports[-1].CovMatrix = ['8.67874e-05','-2.18866e-07','3.42e-08','0','0','0','0','0','0','-2.18866e-07','4.33065e-08','7.62483e-10','0','0','0','0','0','0','3.42e-08','7.62483e-10','4.28408e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 18685
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0502906, 0.00937642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000663849, 0.000209013, 0), \
                           -30930, 18685, 18685, -nan)
reports[-1].sigmaresid = ValErr(1.26668, 0.00655248, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0391263, None, 0.000351959, None, -0.045745, None, 0.000590392, None, -0.045745, None, 0.000590392, None, -0.0461236, None, 0.00067419, None, -0.0461236, None, 0.00067419, None, 1.26702, None, 0.00739432, None, 1.26702, None, 0.00739432, None)
reports[-1].CovMatrix = ['8.79172e-05','-2.99045e-07','3.30102e-08','0','0','0','0','0','0','-2.99045e-07','4.36865e-08','7.33085e-10','0','0','0','0','0','0','3.30102e-08','7.33085e-10','4.2935e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 19256
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.06472, 0.00916945, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.161e-05, 0.000202317, 0), \
                           -31523.8, 19256, 19256, -nan)
reports[-1].sigmaresid = ValErr(1.24377, 0.00633784, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.075473, None, 0.000302284, None, -0.0638424, None, 0.000487211, None, -0.0638424, None, 0.000487211, None, -0.0513516, None, 0.000469046, None, -0.0513516, None, 0.000469046, None, 1.24378, None, 0.00691615, None, 1.24378, None, 0.00691615, None)
reports[-1].CovMatrix = ['8.40789e-05','-3.91361e-07','2.89761e-08','0','0','0','0','0','0','-3.91361e-07','4.09321e-08','6.67818e-10','0','0','0','0','0','0','2.89761e-08','6.67818e-10','4.01683e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 106149
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0259511, 0.000537702, 0), \
                           ValErr(-0.0614304, 0.0135503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.57956e-05, 1.4286e-05, 0), \
                           36218.5, 106149, 106149, -nan)
reports[-1].sigmaresid = ValErr(0.17202, 0.000373342, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0264114, None, 0.00049464, None, 0.0264767, None, 0.000480847, None, 0.0264767, None, 0.000480847, None, 0.0274698, None, 0.0004524, None, 0.0274698, None, 0.0004524, None, 0.172054, None, 0.00386313, None, 0.172054, None, 0.00386313, None)
reports[-1].CovMatrix = ['2.89123e-07','1.80349e-07','-1.44093e-09','4.88841e-11','0','0','0','0','0','1.80349e-07','0.000183611','3.22353e-10','1.49415e-09','0','0','0','0','0','-1.44093e-09','3.22353e-10','2.04089e-10','1.27793e-12','0','0','0','0','0','4.88841e-11','1.49415e-09','1.27793e-12','1.39384e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 101332
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0216259, 0.000545878, 0), \
                           ValErr(-0.0352114, 0.013651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.37084e-05, 1.45493e-05, 0), \
                           35967, 101332, 101332, -nan)
reports[-1].sigmaresid = ValErr(0.169673, 0.000376898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0228342, None, 0.000596562, None, 0.0223766, None, 0.000568548, None, 0.0223766, None, 0.000568548, None, 0.0223189, None, 0.000592285, None, 0.0223189, None, 0.000592285, None, 0.169714, None, 0.0038299, None, 0.169714, None, 0.0038299, None)
reports[-1].CovMatrix = ['2.97983e-07','-4.29332e-08','-1.71346e-09','4.81332e-11','0','0','0','0','0','-4.29332e-08','0.00018635','4.32063e-10','1.49378e-09','0','0','0','0','0','-1.71346e-09','4.32063e-10','2.11683e-10','1.30818e-12','0','0','0','0','0','4.81332e-11','1.49378e-09','1.30818e-12','1.42052e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 20846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00228997, 0.0012664, 0), \
                           ValErr(-0.133967, 0.0356228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.58376e-05, 3.1842e-05, 0), \
                           7229.14, 20846, 20846, -nan)
reports[-1].sigmaresid = ValErr(0.171063, 0.000837777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00334295, None, 0.000145114, None, 0.00296733, None, 0.000265429, None, 0.00296733, None, 0.000265429, None, 0.00592521, None, 0.000244643, None, 0.00592521, None, 0.000244643, None, 0.17113, None, 0.00544305, None, 0.17113, None, 0.00544305, None)
reports[-1].CovMatrix = ['1.60377e-06','1.11386e-05','-1.12337e-08','3.19899e-10','0','0','0','0','0','1.11386e-05','0.00126898','-1.27055e-07','1.00226e-08','0','0','0','0','0','-1.12337e-08','-1.27055e-07','1.01391e-09','4.93574e-12','0','0','0','0','0','3.19899e-10','1.00226e-08','4.93574e-12','7.01871e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 86957
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0118686, 0.000603754, 0), \
                           ValErr(-0.0230999, 0.0149233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.29516e-05, 1.71485e-05, 0), \
                           26762.1, 86957, 86957, -nan)
reports[-1].sigmaresid = ValErr(0.17787, 0.000426517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118059, None, 0.0100465, None, -0.0117335, None, 0.00959675, None, -0.0117335, None, 0.00959675, None, -0.0110752, None, 0.00976903, None, -0.0110752, None, 0.00976903, None, 0.177903, None, 0.00413327, None, 0.177903, None, 0.00413327, None)
reports[-1].CovMatrix = ['3.64519e-07','2.51773e-07','-3.38988e-10','6.95781e-11','0','0','0','0','0','2.51773e-07','0.000222705','3.93296e-09','1.80202e-09','0','0','0','0','0','-3.38988e-10','3.93296e-09','2.94072e-10','1.94422e-12','0','0','0','0','0','6.95781e-11','1.80202e-09','1.94422e-12','1.81917e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 105757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0311797, 0.000536824, 0), \
                           ValErr(0.0101609, 0.0134546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.2858e-05, 1.42172e-05, 0), \
                           36563.1, 105757, 105757, -nan)
reports[-1].sigmaresid = ValErr(0.171244, 0.000372345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0300765, None, -0.00030312, None, -0.0305707, None, -0.000332087, None, -0.0305707, None, -0.000332087, None, -0.029775, None, -0.000332842, None, -0.029775, None, -0.000332842, None, 0.171272, None, 0.00380762, None, 0.171272, None, 0.00380762, None)
reports[-1].CovMatrix = ['2.8818e-07','-7.03899e-09','-1.48419e-09','4.68032e-11','0','0','0','0','0','-7.03899e-09','0.000181027','-2.76582e-10','1.42536e-09','0','0','0','0','0','-1.48419e-09','-2.76582e-10','2.02129e-10','1.25096e-12','0','0','0','0','0','4.68032e-11','1.42536e-09','1.25096e-12','1.38641e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 94348
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0365114, 0.000576508, 0), \
                           ValErr(0.000163736, 0.01477, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.21578e-07, 1.59662e-05, 0), \
                           30503.9, 94348, 94348, -nan)
reports[-1].sigmaresid = ValErr(0.175126, 0.000403152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0365509, None, -0.000664125, None, -0.0365118, None, -0.000629941, None, -0.0365118, None, -0.000629941, None, -0.0376027, None, -0.000655405, None, -0.0376027, None, -0.000655405, None, 0.175126, None, 0.00381287, None, 0.175126, None, 0.00381287, None)
reports[-1].CovMatrix = ['3.32361e-07','-6.137e-07','-1.10346e-09','5.2587e-11','0','0','0','0','0','-6.137e-07','0.000218151','-2.83493e-08','1.34995e-09','0','0','0','0','0','-1.10346e-09','-2.83493e-08','2.5492e-10','1.38836e-12','0','0','0','0','0','5.2587e-11','1.34995e-09','1.38836e-12','1.62531e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 104494
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0530743, 0.000539551, 0), \
                           ValErr(-0.0189068, 0.0135005, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31597e-05, 1.42882e-05, 0), \
                           36169.5, 104494, 104494, -nan)
reports[-1].sigmaresid = ValErr(0.171173, 0.000374434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0535242, None, -0.0005812, None, -0.0532425, None, -0.000584958, None, -0.0532425, None, -0.000584958, None, -0.0531157, None, -0.000573328, None, -0.0531157, None, -0.000573328, None, 0.171177, None, 0.0038365, None, 0.171177, None, 0.0038365, None)
reports[-1].CovMatrix = ['2.91115e-07','-6.38205e-09','-1.47886e-09','4.78776e-11','0','0','0','0','0','-6.38205e-09','0.000182263','5.02514e-10','1.46359e-09','0','0','0','0','0','-1.47886e-09','5.02514e-10','2.04152e-10','1.26725e-12','0','0','0','0','0','4.78776e-11','1.46359e-09','1.26725e-12','1.40201e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 100728
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.06272, 0.000551511, 0), \
                           ValErr(0.00714152, 0.0137683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.75091e-06, 1.44936e-05, 0), \
                           35691.8, 100728, 100728, -nan)
reports[-1].sigmaresid = ValErr(0.169776, 0.000378256, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.062711, None, 0.000557313, None, -0.0627555, None, 0.000484739, None, -0.0627555, None, 0.000484739, None, -0.0626224, None, 0.000529766, None, -0.0626224, None, 0.000529766, None, 0.169776, None, 0.00382794, None, 0.169776, None, 0.00382794, None)
reports[-1].CovMatrix = ['3.04164e-07','1.50692e-08','-1.94498e-09','4.78932e-11','0','0','0','0','0','1.50692e-08','0.000189567','-3.61815e-10','1.50065e-09','0','0','0','0','0','-1.94498e-09','-3.61815e-10','2.10064e-10','1.23804e-12','0','0','0','0','0','4.78932e-11','1.50065e-09','1.23804e-12','1.43077e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 88147
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0576218, 0.000587232, 0), \
                           ValErr(-0.002348, 0.0142435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.98359e-05, 1.52745e-05, 0), \
                           31919.3, 88147, 88147, -nan)
reports[-1].sigmaresid = ValErr(0.168461, 0.000401218, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0567974, None, -0.000313806, None, -0.0569302, None, -0.000336404, None, -0.0569302, None, -0.000336404, None, -0.0580146, None, -0.000308682, None, -0.0580146, None, -0.000308682, None, 0.168481, None, 0.00380862, None, 0.168481, None, 0.00380862, None)
reports[-1].CovMatrix = ['3.44842e-07','-1.47988e-08','-2.31094e-09','5.2911e-11','0','0','0','0','0','-1.47988e-08','0.000202877','2.55866e-10','1.67471e-09','0','0','0','0','0','-2.31094e-09','2.55866e-10','2.3331e-10','1.38836e-12','0','0','0','0','0','5.2911e-11','1.67471e-09','1.38836e-12','1.60976e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 98828
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0488975, 0.000553191, 0), \
                           ValErr(0.0238663, 0.0138626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.50545e-05, 1.46195e-05, 0), \
                           34998.5, 98828, 98828, -nan)
reports[-1].sigmaresid = ValErr(0.16981, 0.000381952, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0489299, None, -0.000195487, None, -0.0490206, None, -0.000196051, None, -0.0490206, None, -0.000196051, None, -0.0496589, None, -0.000188184, None, -0.0496589, None, -0.000188184, None, 0.169814, None, 0.00384741, None, 0.169814, None, 0.00384741, None)
reports[-1].CovMatrix = ['3.0602e-07','4.33135e-09','-1.74491e-09','4.95102e-11','0','0','0','0','0','4.33135e-09','0.000192171','-4.66886e-10','1.53286e-09','0','0','0','0','0','-1.74491e-09','-4.66886e-10','2.13729e-10','1.3031e-12','0','0','0','0','0','4.95102e-11','1.53286e-09','1.3031e-12','1.45887e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 103096
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0424739, 0.00054502, 0), \
                           ValErr(-0.0099289, 0.0136825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.32908e-06, 1.4501e-05, 0), \
                           35479.7, 103096, 103096, -nan)
reports[-1].sigmaresid = ValErr(0.171515, 0.000377718, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0428332, None, 0.00137159, None, -0.0424025, None, 0.00125049, None, -0.0424025, None, 0.00125049, None, -0.043056, None, 0.00132021, None, -0.043056, None, 0.00132021, None, 0.171516, None, 0.0038611, None, 0.171516, None, 0.0038611, None)
reports[-1].CovMatrix = ['2.97047e-07','2.2613e-08','-1.56848e-09','4.83806e-11','0','0','0','0','0','2.2613e-08','0.000187211','1.61054e-09','1.49158e-09','0','0','0','0','0','-1.56848e-09','1.61054e-09','2.10278e-10','1.30071e-12','0','0','0','0','0','4.83806e-11','1.49158e-09','1.30071e-12','1.42671e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 95402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0278546, 0.000564925, 0), \
                           ValErr(0.0322285, 0.0141962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.37638e-05, 1.49733e-05, 0), \
                           33501.7, 95402, 95402, -nan)
reports[-1].sigmaresid = ValErr(0.170316, 0.000389907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0282796, None, -0.00086193, None, -0.0285365, None, -0.000824673, None, -0.0285365, None, -0.000824673, None, -0.0278748, None, -0.000836433, None, -0.0278748, None, -0.000836433, None, 0.170348, None, 0.00378213, None, 0.170348, None, 0.00378213, None)
reports[-1].CovMatrix = ['3.1914e-07','-3.72147e-08','-1.83881e-09','5.05805e-11','0','0','0','0','0','-3.72147e-08','0.000201533','8.8639e-10','1.58757e-09','0','0','0','0','0','-1.83881e-09','8.8639e-10','2.24201e-10','1.32297e-12','0','0','0','0','0','5.05805e-11','1.58757e-09','1.32297e-12','1.52027e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 97855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0137423, 0.000555227, 0), \
                           ValErr(-0.00222185, 0.0141549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.71706e-05, 1.46148e-05, 0), \
                           34396.6, 97855, 97855, -nan)
reports[-1].sigmaresid = ValErr(0.170257, 0.000384857, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0142882, None, -0.000916544, None, -0.0136132, None, -0.000890372, None, -0.0136132, None, -0.000890372, None, -0.0134326, None, -0.000837025, None, -0.0134326, None, -0.000837025, None, 0.170259, None, 0.00403294, None, 0.170259, None, 0.00403294, None)
reports[-1].CovMatrix = ['3.08277e-07','3.6067e-07','-1.56769e-09','5.37779e-11','0','0','0','0','0','3.6067e-07','0.000200361','-4.28243e-09','1.61972e-09','0','0','0','0','0','-1.56769e-09','-4.28243e-09','2.13592e-10','1.30302e-12','0','0','0','0','0','5.37779e-11','1.61972e-09','1.30302e-12','1.48115e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 100371
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00096323, 0.000550696, 0), \
                           ValErr(0.0551164, 0.0138143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.92175e-05, 1.45649e-05, 0), \
                           35360.8, 100371, 100371, -nan)
reports[-1].sigmaresid = ValErr(0.170122, 0.000379701, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0019816, None, -0.000440697, None, 0.00148882, None, -0.000394126, None, 0.00148882, None, -0.000394126, None, 0.00182826, None, -0.00038954, None, 0.00182826, None, -0.00038954, None, 0.17015, None, 0.00390613, None, 0.17015, None, 0.00390613, None)
reports[-1].CovMatrix = ['3.03267e-07','-9.58264e-08','-1.77584e-09','4.76103e-11','0','0','0','0','0','-9.58264e-08','0.000190836','-8.26965e-10','1.49188e-09','0','0','0','0','0','-1.77584e-09','-8.26965e-10','2.12137e-10','1.26049e-12','0','0','0','0','0','4.76103e-11','1.49188e-09','1.26049e-12','1.44173e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 107315
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0113523, 0.000532775, 0), \
                           ValErr(-0.0152623, 0.0133975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.35249e-05, 1.40854e-05, 0), \
                           37243, 107315, 107315, -nan)
reports[-1].sigmaresid = ValErr(0.171019, 0.000369146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0120349, None, 0.000524118, None, 0.011756, None, 0.00047258, None, 0.011756, None, 0.00047258, None, 0.0139489, None, 0.000493399, None, 0.0139489, None, 0.000493399, None, 0.171031, None, 0.00382654, None, 0.171031, None, 0.00382654, None)
reports[-1].CovMatrix = ['2.83849e-07','-8.27942e-09','-1.49805e-09','4.66108e-11','0','0','0','0','0','-8.27942e-09','0.000179492','5.96354e-10','1.42472e-09','0','0','0','0','0','-1.49805e-09','5.96354e-10','1.984e-10','1.19769e-12','0','0','0','0','0','4.66108e-11','1.42472e-09','1.19769e-12','1.36269e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 102522
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0211872, 0.000544389, 0), \
                           ValErr(0.0427143, 0.013674, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000107946, 1.44761e-05, 0), \
                           36611.9, 102522, 102522, -nan)
reports[-1].sigmaresid = ValErr(0.169306, 0.000373894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0221777, None, -1.5934e-05, None, 0.022146, None, -2.96015e-05, None, 0.022146, None, -2.96015e-05, None, 0.0226962, None, -1.69487e-05, None, 0.0226962, None, -1.69487e-05, None, 0.16936, None, 0.00383176, None, 0.16936, None, 0.00383176, None)
reports[-1].CovMatrix = ['2.9636e-07','3.97537e-08','-1.87421e-09','4.59861e-11','0','0','0','0','0','3.97537e-08','0.000186979','-1.0727e-09','1.49048e-09','0','0','0','0','0','-1.87421e-09','-1.0727e-09','2.09559e-10','1.26243e-12','0','0','0','0','0','4.59861e-11','1.49048e-09','1.26243e-12','1.39797e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 102909
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0306662, 0.000545892, 0), \
                           ValErr(0.0349012, 0.013706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000102488, 1.457e-05, 0), \
                           35151.7, 102909, 102909, -nan)
reports[-1].sigmaresid = ValErr(0.171956, 0.000379031, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0312356, None, -0.001682, None, 0.0313953, None, -0.00162618, None, 0.0313953, None, -0.00162618, None, 0.0321075, None, -0.00165032, None, 0.0321075, None, -0.00165032, None, 0.172002, None, 0.00378837, None, 0.172002, None, 0.00378837, None)
reports[-1].CovMatrix = ['2.97998e-07','-2.16508e-08','-1.50492e-09','4.85877e-11','0','0','0','0','0','-2.16508e-08','0.000187853','1.08462e-09','1.48867e-09','0','0','0','0','0','-1.50492e-09','1.08462e-09','2.12286e-10','1.30824e-12','0','0','0','0','0','4.85877e-11','1.48867e-09','1.30824e-12','1.43664e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 102422
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0286902, 0.000541582, 0), \
                           ValErr(-0.0183814, 0.0135822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000155372, 1.43785e-05, 0), \
                           36629.3, 102422, 102422, -nan)
reports[-1].sigmaresid = ValErr(0.169218, 0.000373882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0304035, None, -0.000549665, None, 0.029958, None, -0.000548778, None, 0.029958, None, -0.000548778, None, 0.0304934, None, -0.000531189, None, 0.0304934, None, -0.000531189, None, 0.169316, None, 0.00381295, None, 0.169316, None, 0.00381295, None)
reports[-1].CovMatrix = ['2.93311e-07','1.26805e-08','-1.68509e-09','4.78499e-11','0','0','0','0','0','1.26805e-08','0.000184476','5.16104e-10','1.49182e-09','0','0','0','0','0','-1.68509e-09','5.16104e-10','2.0674e-10','1.2968e-12','0','0','0','0','0','4.78499e-11','1.49182e-09','1.2968e-12','1.39787e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 106558
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0224724, 0.000476153, 0), \
                           ValErr(0.0547558, 0.0119437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.88906e-05, 1.26155e-05, 0), \
                           49661, 106558, 106558, -nan)
reports[-1].sigmaresid = ValErr(0.151832, 0.000336023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0231257, None, 0.000621358, None, 0.0230829, None, 0.000640256, None, 0.0230829, None, 0.000640256, None, 0.0223767, None, 0.000691977, None, 0.0223767, None, 0.000691977, None, 0.151875, None, 0.00387685, None, 0.151875, None, 0.00387685, None)
reports[-1].CovMatrix = ['2.26722e-07','-3.03033e-08','-1.21121e-09','-2.2858e-09','0','0','0','0','0','-3.03033e-08','0.000142652','-1.13068e-09','-2.82438e-08','0','0','0','0','0','-1.21121e-09','-1.13068e-09','1.59151e-10','9.36884e-11','0','0','0','0','0','-2.2858e-09','-2.82438e-08','9.36884e-11','1.12911e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 106484
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112058, 0.00047959, 0), \
                           ValErr(-0.0185303, 0.0119901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.65184e-05, 1.25764e-05, 0), \
                           48524.3, 106484, 106484, -nan)
reports[-1].sigmaresid = ValErr(0.153411, 0.000337048, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0115309, None, 0.000785405, None, 0.0118273, None, 0.000774572, None, 0.0118273, None, 0.000774572, None, 0.0118662, None, 0.000808667, None, 0.0118662, None, 0.000808667, None, 0.153447, None, 0.00399311, None, 0.153447, None, 0.00399311, None)
reports[-1].CovMatrix = ['2.30007e-07','-1.24538e-08','-1.11164e-09','-2.33722e-10','0','0','0','0','0','-1.24538e-08','0.000143762','1.48652e-10','8.37044e-09','0','0','0','0','0','-1.11164e-09','1.48652e-10','1.58167e-10','3.55529e-11','0','0','0','0','0','-2.33722e-10','8.37044e-09','3.55529e-11','1.13602e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 89191
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000723756, 0.000526086, 0), \
                           ValErr(-0.0819647, 0.0132494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.76813e-05, 1.32896e-05, 0), \
                           41040.6, 89191, 89191, -nan)
reports[-1].sigmaresid = ValErr(0.15273, 0.000361618, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000533001, None, 0.00038544, None, -0.000163306, None, 0.000358838, None, -0.000163306, None, 0.000358838, None, -0.000365752, None, 0.000386473, None, -0.000365752, None, 0.000386473, None, 0.152779, None, 0.00369275, None, 0.152779, None, 0.00369275, None)
reports[-1].CovMatrix = ['2.76767e-07','6.55379e-08','-1.63927e-09','5.01997e-11','0','0','0','0','0','6.55379e-08','0.000175547','-1.24732e-09','1.5905e-09','0','0','0','0','0','-1.63927e-09','-1.24732e-09','1.76613e-10','1.24165e-12','0','0','0','0','0','5.01997e-11','1.5905e-09','1.24165e-12','1.30767e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 104766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0255202, 0.000481257, 0), \
                           ValErr(-0.0577741, 0.0119997, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.37176e-05, 1.27727e-05, 0), \
                           48736.9, 104766, 104766, -nan)
reports[-1].sigmaresid = ValErr(0.15196, 0.000335738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0248981, None, -0.000453509, None, -0.0249552, None, -0.000440965, None, -0.0249552, None, -0.000440965, None, -0.0241824, None, -0.000419484, None, -0.0241824, None, -0.000419484, None, 0.152002, None, 0.00385348, None, 0.152002, None, 0.00385348, None)
reports[-1].CovMatrix = ['2.31608e-07','-8.51288e-10','-1.27644e-09','1.75273e-09','0','0','0','0','0','-8.51288e-10','0.000143992','4.89835e-11','1.13015e-09','0','0','0','0','0','-1.27644e-09','4.89835e-11','1.63141e-10','-8.09113e-11','0','0','0','0','0','1.75273e-09','1.13015e-09','-8.09113e-11','1.1272e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 107697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0353673, 0.00047685, 0), \
                           ValErr(0.0253684, 0.0119233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.47315e-05, 1.25892e-05, 0), \
                           49461, 107697, 107697, -nan)
reports[-1].sigmaresid = ValErr(0.152865, 0.000329419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0343761, None, -0.000436568, None, -0.0346181, None, -0.000449419, None, -0.0346181, None, -0.000449419, None, -0.0344993, None, -0.000447914, None, -0.0344993, None, -0.000447914, None, 0.152909, None, 0.00383378, None, 0.152909, None, 0.00383378, None)
reports[-1].CovMatrix = ['2.27386e-07','3.27017e-09','-1.26794e-09','1.05101e-10','0','0','0','0','0','3.27017e-09','0.000142165','1.32081e-10','8.5091e-11','0','0','0','0','0','-1.26794e-09','1.32081e-10','1.58488e-10','2.93599e-12','0','0','0','0','0','1.05101e-10','8.5091e-11','2.93599e-12','1.08517e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 102925
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0363515, 0.000485506, 0), \
                           ValErr(-0.0228979, 0.0120978, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.73271e-05, 1.28252e-05, 0), \
                           47997.7, 102925, 102925, -nan)
reports[-1].sigmaresid = ValErr(0.151787, 0.000334894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0367863, None, -0.000306873, None, -0.0365589, None, -0.000245986, None, -0.0365589, None, -0.000245986, None, -0.0374574, None, -0.000268553, None, -0.0374574, None, -0.000268553, None, 0.151793, None, 0.00415987, None, 0.151793, None, 0.00415987, None)
reports[-1].CovMatrix = ['2.35716e-07','2.52087e-08','-1.3167e-09','4.35304e-10','0','0','0','0','0','2.52087e-08','0.000146356','-7.68394e-11','-5.57164e-10','0','0','0','0','0','-1.3167e-09','-7.68394e-11','1.64487e-10','-1.59364e-11','0','0','0','0','0','4.35304e-10','-5.57164e-10','-1.59364e-11','1.12154e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 98797
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0513686, 0.000495226, 0), \
                           ValErr(-0.0321004, 0.0122843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.55239e-06, 1.30398e-05, 0), \
                           45981.3, 98797, 98797, -nan)
reports[-1].sigmaresid = ValErr(0.151928, 0.000341783, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0513174, None, -0.000703526, None, -0.0512838, None, -0.00073774, None, -0.0512838, None, -0.00073774, None, -0.0521183, None, -0.000806542, None, -0.0521183, None, -0.000806542, None, 0.151933, None, 0.00386188, None, 0.151933, None, 0.00386188, None)
reports[-1].CovMatrix = ['2.45249e-07','4.46419e-08','-1.40511e-09','4.70471e-11','0','0','0','0','0','4.46419e-08','0.000150904','-1.537e-09','1.37982e-09','0','0','0','0','0','-1.40511e-09','-1.537e-09','1.70037e-10','1.16959e-12','0','0','0','0','0','4.70471e-11','1.37982e-09','1.16959e-12','1.16815e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 103625
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0565218, 0.000487639, 0), \
                           ValErr(0.015168, 0.0149439, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.72758e-06, 1.31033e-05, 0), \
                           48032.3, 103625, 103625, -nan)
reports[-1].sigmaresid = ValErr(0.152215, 0.000339034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0566634, None, -0.000479739, None, -0.056539, None, -0.000446703, None, -0.056539, None, -0.000446703, None, -0.0564035, None, -0.000469854, None, -0.0564035, None, -0.000469854, None, 0.152217, None, 0.00390054, None, 0.152217, None, 0.00390054, None)
reports[-1].CovMatrix = ['2.37792e-07','-4.51587e-07','-1.50534e-09','3.07713e-09','0','0','0','0','0','-4.51587e-07','0.000223319','2.93802e-08','-4.82774e-07','0','0','0','0','0','-1.50534e-09','2.93802e-08','1.71696e-10','-1.90014e-10','0','0','0','0','0','3.07713e-09','-4.82774e-07','-1.90014e-10','1.14944e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 95527
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0595771, 0.000503293, 0), \
                           ValErr(-0.0645951, 0.0122084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.55848e-05, 1.29051e-05, 0), \
                           44360.7, 95527, 95527, -nan)
reports[-1].sigmaresid = ValErr(0.152085, 0.000347943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0592184, None, -0.000858573, None, -0.059422, None, -0.000817086, None, -0.059422, None, -0.000817086, None, -0.0604667, None, -0.000843575, None, -0.0604667, None, -0.000843575, None, 0.15211, None, 0.00383399, None, 0.15211, None, 0.00383399, None)
reports[-1].CovMatrix = ['2.53304e-07','-1.38346e-07','-1.35804e-09','4.57963e-11','0','0','0','0','0','-1.38346e-07','0.000149046','1.88558e-09','1.39821e-09','0','0','0','0','0','-1.35804e-09','1.88558e-09','1.66542e-10','1.22555e-12','0','0','0','0','0','4.57963e-11','1.39821e-09','1.22555e-12','1.21064e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 103134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0495343, 0.000485363, 0), \
                           ValErr(0.0365305, 0.012169, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.54795e-05, 1.27551e-05, 0), \
                           47550, 103134, 103134, -nan)
reports[-1].sigmaresid = ValErr(0.152592, 0.000335981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0493064, None, -0.000134441, None, -0.0493418, None, -0.000160311, None, -0.0493418, None, -0.000160311, None, -0.0484797, None, -0.000187321, None, -0.0484797, None, -0.000187321, None, 0.152601, None, 0.00397409, None, 0.152601, None, 0.00397409, None)
reports[-1].CovMatrix = ['2.35577e-07','1.71038e-08','-1.26316e-09','4.41619e-11','0','0','0','0','0','1.71038e-08','0.000148085','5.71048e-10','1.35669e-09','0','0','0','0','0','-1.26316e-09','5.71048e-10','1.62693e-10','1.16211e-12','0','0','0','0','0','4.41619e-11','1.35669e-09','1.16211e-12','1.12883e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 103954
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0394974, 0.000482146, 0), \
                           ValErr(-0.00628408, 0.0121718, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.88034e-05, 1.26952e-05, 0), \
                           47761.1, 103954, 103954, -nan)
reports[-1].sigmaresid = ValErr(0.152837, 0.000334868, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0389764, None, -0.00119425, None, -0.0392896, None, -0.00113307, None, -0.0392896, None, -0.00113307, None, -0.0393991, None, -0.00115505, None, -0.0393991, None, -0.00115505, None, 0.152841, None, 0.00385384, None, 0.152841, None, 0.00385384, None)
reports[-1].CovMatrix = ['2.32464e-07','2.04091e-07','-1.11432e-09','4.00997e-10','0','0','0','0','0','2.04091e-07','0.000148153','-1.85746e-11','-3.99695e-10','0','0','0','0','0','-1.11432e-09','-1.85746e-11','1.61169e-10','-2.32015e-12','0','0','0','0','0','4.00997e-10','-3.99695e-10','-2.32015e-12','1.12137e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 103754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0222384, 0.000483199, 0), \
                           ValErr(0.0549183, 0.0121086, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.78202e-05, 1.26767e-05, 0), \
                           48036, 103754, 103754, -nan)
reports[-1].sigmaresid = ValErr(0.152298, 0.000334331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.021619, None, -0.0013454, None, -0.0221129, None, -0.0012946, None, -0.0221129, None, -0.0012946, None, -0.0216954, None, -0.00136085, None, -0.0216954, None, -0.00136085, None, 0.152314, None, 0.0038696, None, 0.152314, None, 0.0038696, None)
reports[-1].CovMatrix = ['2.33481e-07','4.24905e-08','-1.26241e-09','4.40097e-11','0','0','0','0','0','4.24905e-08','0.000146618','-5.20128e-10','1.34966e-09','0','0','0','0','0','-1.26241e-09','-5.20128e-10','1.607e-10','1.13441e-12','0','0','0','0','0','4.40097e-11','1.34966e-09','1.13441e-12','1.11777e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 102530
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00903673, 0.000484349, 0), \
                           ValErr(0.0524689, 0.0122778, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.22985e-05, 1.27587e-05, 0), \
                           47712.7, 102530, 102530, -nan)
reports[-1].sigmaresid = ValErr(0.151937, 0.000335523, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00834226, None, -0.000655303, None, -0.00879708, None, -0.000611795, None, -0.00879708, None, -0.000611795, None, -0.0101944, None, -0.000655121, None, -0.0101944, None, -0.000655121, None, 0.151952, None, 0.00391282, None, 0.151952, None, 0.00391282, None)
reports[-1].CovMatrix = ['2.34594e-07','-2.11453e-07','-1.22075e-09','4.24159e-11','0','0','0','0','0','-2.11453e-07','0.000150745','4.11653e-10','1.32604e-09','0','0','0','0','0','-1.22075e-09','4.11653e-10','1.62785e-10','1.17076e-12','0','0','0','0','0','4.24159e-11','1.32604e-09','1.17076e-12','1.12575e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 100698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00245199, 0.000493142, 0), \
                           ValErr(-0.0316395, 0.0123868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.79958e-05, 1.29387e-05, 0), \
                           45966.3, 100698, 100698, -nan)
reports[-1].sigmaresid = ValErr(0.153291, 0.000341579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00277003, None, -0.000233274, None, 0.00282026, None, -0.000248096, None, 0.00282026, None, -0.000248096, None, 0.00307661, None, -0.000264714, None, 0.00307661, None, -0.000264714, None, 0.153307, None, 0.00400594, None, 0.153307, None, 0.00400594, None)
reports[-1].CovMatrix = ['2.43189e-07','-6.33195e-10','-1.28321e-09','4.4965e-11','0','0','0','0','0','-6.33195e-10','0.000153433','2.00287e-10','1.3982e-09','0','0','0','0','0','-1.28321e-09','2.00287e-10','1.67411e-10','1.19757e-12','0','0','0','0','0','4.4965e-11','1.3982e-09','1.19757e-12','1.16676e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 105959
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0152475, 0.000478183, 0), \
                           ValErr(0.0173413, 0.0120557, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.87452e-05, 1.26024e-05, 0), \
                           48752.9, 105959, 105959, -nan)
reports[-1].sigmaresid = ValErr(0.152735, 0.000331784, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0156116, None, -0.00237601, None, 0.0155092, None, -0.0022838, None, 0.0155092, None, -0.0022838, None, 0.0163321, None, -0.0023523, None, 0.0163321, None, -0.0023523, None, 0.152743, None, 0.00394578, None, 0.152743, None, 0.00394578, None)
reports[-1].CovMatrix = ['2.28659e-07','1.45687e-07','-1.14918e-09','4.44627e-11','0','0','0','0','0','1.45687e-07','0.000145339','2.39303e-09','1.38041e-09','0','0','0','0','0','-1.14918e-09','2.39303e-09','1.5882e-10','1.16059e-12','0','0','0','0','0','4.44627e-11','1.38041e-09','1.16059e-12','1.10081e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 105169
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0233003, 0.0004835, 0), \
                           ValErr(0.0382336, 0.0121394, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000175283, 1.27524e-05, 0), \
                           48111.1, 105169, 105169, -nan)
reports[-1].sigmaresid = ValErr(0.15314, 0.000333911, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0248347, None, -0.000248288, None, 0.0247163, None, -0.000249803, None, 0.0247163, None, -0.000249803, None, 0.0248593, None, -0.000276253, None, 0.0248593, None, -0.000276253, None, 0.153285, None, 0.00382899, None, 0.153285, None, 0.00382899, None)
reports[-1].CovMatrix = ['2.33772e-07','3.88919e-08','-1.32334e-09','4.32741e-11','0','0','0','0','0','3.88919e-08','0.000147365','1.01846e-10','1.347e-09','0','0','0','0','0','-1.32334e-09','1.01846e-10','1.62622e-10','1.13912e-12','0','0','0','0','0','4.32741e-11','1.347e-09','1.13912e-12','1.11496e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 104946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0302463, 0.000483455, 0), \
                           ValErr(0.0324111, 0.0120939, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41968e-05, 1.28326e-05, 0), \
                           48353.4, 104946, 104946, -nan)
reports[-1].sigmaresid = ValErr(0.152638, 0.000334489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0305517, None, 0.00128499, None, 0.0303962, None, 0.0012208, None, 0.0303962, None, 0.0012208, None, 0.0312055, None, 0.00123247, None, 0.0312055, None, 0.00123247, None, 0.152646, None, 0.00385568, None, 0.152646, None, 0.00385568, None)
reports[-1].CovMatrix = ['2.33728e-07','1.41754e-07','-1.26665e-09','-1.21107e-09','0','0','0','0','0','1.41754e-07','0.000146262','-1.42448e-09','-9.64822e-10','0','0','0','0','0','-1.26665e-09','-1.42448e-09','1.64676e-10','4.63131e-11','0','0','0','0','0','-1.21107e-09','-9.64822e-10','4.63131e-11','1.11883e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 106496
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.026658, 0.000475756, 0), \
                           ValErr(-0.0552116, 0.0119078, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.48303e-05, 1.25209e-05, 0), \
                           50053.8, 106496, 106496, -nan)
reports[-1].sigmaresid = ValErr(0.151232, 0.00032769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0272926, None, 0.000239384, None, 0.0274855, None, 0.000244753, None, 0.0274855, None, 0.000244753, None, 0.0270976, None, 0.000243669, None, 0.0270976, None, 0.000243669, None, 0.151287, None, 0.00382126, None, 0.151287, None, 0.00382126, None)
reports[-1].CovMatrix = ['2.26344e-07','3.29846e-08','-1.34719e-09','4.14367e-11','0','0','0','0','0','3.29846e-08','0.000141796','-8.64123e-11','1.3165e-09','0','0','0','0','0','-1.34719e-09','-8.64123e-11','1.56774e-10','1.10734e-12','0','0','0','0','0','4.14367e-11','1.3165e-09','1.10734e-12','1.0738e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 196842
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00937364, 0.000848966, 0), \
                           ValErr(-0.0639131, 0.0097709, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.07028e-05, 1.70409e-05, 0), \
                           -85084.4, 196842, 196842, -nan)
reports[-1].sigmaresid = ValErr(0.372808, 0.000594171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0096022, None, 7.71324e-05, None, 0.0100345, None, -9.05857e-05, None, 0.0100345, None, -9.05857e-05, None, 0.00785639, None, -5.74035e-05, None, 0.00785639, None, -5.74035e-05, None, 0.372875, None, 0.0077058, None, 0.372875, None, 0.0077058, None)
reports[-1].CovMatrix = ['7.20743e-07','2.64486e-08','-2.06308e-09','1.42317e-10','0','0','0','0','0','2.64486e-08','9.54704e-05','-1.19089e-10','1.85712e-09','0','0','0','0','0','-2.06308e-09','-1.19089e-10','2.90393e-10','2.77645e-12','0','0','0','0','0','1.42317e-10','1.85712e-09','2.77645e-12','3.5304e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 193943
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0522043, 0.000858005, 0), \
                           ValErr(-0.0367007, 0.00994642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.22769e-05, 1.70941e-05, 0), \
                           -84188.7, 193943, 193943, -nan)
reports[-1].sigmaresid = ValErr(0.373496, 0.0005997, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0530287, None, -0.000309448, None, -0.0516744, None, -0.000450136, None, -0.0516744, None, -0.000450136, None, -0.0523842, None, -0.000432962, None, -0.0523842, None, -0.000432962, None, 0.373526, None, 0.0076549, None, 0.373526, None, 0.0076549, None)
reports[-1].CovMatrix = ['7.36172e-07','-4.99538e-08','-2.22001e-09','1.4112e-10','0','0','0','0','0','-4.99538e-08','9.89312e-05','-2.45596e-10','1.86538e-09','0','0','0','0','0','-2.22001e-09','-2.45596e-10','2.92209e-10','2.8352e-12','0','0','0','0','0','1.4112e-10','1.86538e-09','2.8352e-12','3.5964e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 190606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0619897, 0.000862672, 0), \
                           ValErr(0.0303026, 0.0100053, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.29833e-05, 1.73147e-05, 0), \
                           -81968.9, 190606, 190606, -nan)
reports[-1].sigmaresid = ValErr(0.371988, 0.000602391, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.062358, None, -0.000660146, None, -0.0623861, None, -0.000738024, None, -0.0623861, None, -0.000738024, None, -0.0613446, None, -0.000762965, None, -0.0613446, None, -0.000762965, None, 0.372002, None, 0.00765571, None, 0.372002, None, 0.00765571, None)
reports[-1].CovMatrix = ['7.44203e-07','2.22527e-07','-2.35027e-09','4.72051e-10','0','0','0','0','0','2.22527e-07','0.000100105','-2.96212e-09','6.54749e-10','0','0','0','0','0','-2.35027e-09','-2.96212e-09','2.99798e-10','-2.25564e-12','0','0','0','0','0','4.72051e-10','6.54749e-10','-2.25564e-12','3.62875e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 108774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0570776, 0.00118196, 0), \
                           ValErr(-0.0442672, 0.0133628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.98607e-05, 2.26321e-05, 0), \
                           -47986.9, 108774, 108774, -nan)
reports[-1].sigmaresid = ValErr(0.376147, 0.000806454, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0585325, None, 9.74994e-05, None, -0.0578209, None, -6.40515e-05, None, -0.0578209, None, -6.40515e-05, None, -0.0571393, None, 0.000157565, None, -0.0571393, None, 0.000157565, None, 0.376167, None, 0.0083297, None, 0.376167, None, 0.0083297, None)
reports[-1].CovMatrix = ['1.39704e-06','-3.64255e-06','-3.7174e-09','2.03493e-10','0','0','0','0','0','-3.64255e-06','0.000178564','1.79646e-08','2.97005e-09','0','0','0','0','0','-3.7174e-09','1.79646e-08','5.12211e-10','5.41174e-12','0','0','0','0','0','2.03493e-10','2.97005e-09','5.41174e-12','6.50368e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 195155
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0332816, 0.000852053, 0), \
                           ValErr(-0.00274784, 0.00989991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.52581e-05, 1.71254e-05, 0), \
                           -84146.6, 195155, 195155, -nan)
reports[-1].sigmaresid = ValErr(0.37241, 0.000596096, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0333778, None, -0.000338367, None, -0.03368, None, -0.000337082, None, -0.03368, None, -0.000337082, None, -0.0337769, None, -0.000337239, None, -0.0337769, None, -0.000337239, None, 0.37242, None, 0.00760695, None, 0.37242, None, 0.00760695, None)
reports[-1].CovMatrix = ['7.25995e-07','3.43532e-08','-2.11973e-09','1.41289e-10','0','0','0','0','0','3.43532e-08','9.80082e-05','2.26841e-10','1.89031e-09','0','0','0','0','0','-2.11973e-09','2.26841e-10','2.93281e-10','2.83561e-12','0','0','0','0','0','1.41289e-10','1.89031e-09','2.83561e-12','3.55331e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 185972
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00374824, 0.000870081, 0), \
                           ValErr(-0.00420943, 0.00986174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.97796e-05, 1.74047e-05, 0), \
                           -79230.3, 185972, 185972, -nan)
reports[-1].sigmaresid = ValErr(0.370499, 0.000607502, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0037, None, -8.52608e-05, None, -0.00406486, None, -5.65519e-05, None, -0.00406486, None, -5.65519e-05, None, -0.00425334, None, -1.52008e-05, None, -0.00425334, None, -1.52008e-05, None, 0.370504, None, 0.00749391, None, 0.370504, None, 0.00749391, None)
reports[-1].CovMatrix = ['7.57041e-07','-5.58822e-08','-2.39205e-09','1.42494e-10','0','0','0','0','0','-5.58822e-08','9.7254e-05','-1.94329e-10','1.89027e-09','0','0','0','0','0','-2.39205e-09','-1.94329e-10','3.02924e-10','2.87111e-12','0','0','0','0','0','1.42494e-10','1.89027e-09','2.87111e-12','3.69059e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 200432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.013119, 0.000840725, 0), \
                           ValErr(0.0341444, 0.00980244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.66591e-05, 1.6844e-05, 0), \
                           -86120.2, 200432, 200432, -nan)
reports[-1].sigmaresid = ValErr(0.37185, 0.000587312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0119741, None, -0.00051656, None, 0.0132862, None, -0.000611676, None, 0.0132862, None, -0.000611676, None, 0.0131789, None, -0.000648914, None, 0.0131789, None, -0.000648914, None, 0.371863, None, 0.00752843, None, 0.371863, None, 0.00752843, None)
reports[-1].CovMatrix = ['7.06819e-07','9.54016e-08','-2.18503e-09','1.37042e-10','0','0','0','0','0','9.54016e-08','9.60878e-05','1.58123e-09','1.88141e-09','0','0','0','0','0','-2.18503e-09','1.58123e-09','2.8372e-10','2.73885e-12','0','0','0','0','0','1.37042e-10','1.88141e-09','2.73885e-12','3.44936e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 117396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0239627, 0.00110002, 0), \
                           ValErr(0.0601315, 0.0127608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.83845e-05, 2.18426e-05, 0), \
                           -51365.7, 117396, 117396, -nan)
reports[-1].sigmaresid = ValErr(0.374788, 0.000773471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0235295, None, -0.00043876, None, 0.0242334, None, -0.000488065, None, 0.0242334, None, -0.000488065, None, 0.0247967, None, -0.000570848, None, 0.0247967, None, -0.000570848, None, 0.374838, None, 0.00886397, None, 0.374838, None, 0.00886397, None)
reports[-1].CovMatrix = ['1.21003e-06','2.34825e-07','-2.50674e-09','2.54157e-10','0','0','0','0','0','2.34825e-07','0.000162837','7.21099e-10','3.2838e-09','0','0','0','0','0','-2.50674e-09','7.21099e-10','4.77099e-10','4.89061e-12','0','0','0','0','0','2.54157e-10','3.2838e-09','4.89061e-12','5.98258e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 195115
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00492483, 0.000811522, 0), \
                           ValErr(-0.0350581, 0.00939501, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.62401e-05, 1.63021e-05, 0), \
                           -74508.3, 195115, 195115, -nan)
reports[-1].sigmaresid = ValErr(0.354492, 0.000567473, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00413064, None, 0.000206169, None, 0.00507204, None, 0.000139359, None, 0.00507204, None, 0.000139359, None, 0.00511573, None, 0.000150678, None, 0.00511573, None, 0.000150678, None, 0.354507, None, 0.00788212, None, 0.354507, None, 0.00788212, None)
reports[-1].CovMatrix = ['6.58568e-07','-1.27951e-07','-1.95378e-09','1.1657e-10','0','0','0','0','0','-1.27951e-07','8.82662e-05','1.6994e-09','1.60443e-09','0','0','0','0','0','-1.95378e-09','1.6994e-09','2.65759e-10','2.44883e-12','0','0','0','0','0','1.1657e-10','1.60443e-09','2.44883e-12','3.22026e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 192725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0411874, 0.000823383, 0), \
                           ValErr(-0.0624346, 0.00948531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000121847, 1.6729e-05, 0), \
                           -75757.2, 192725, 192725, -nan)
reports[-1].sigmaresid = ValErr(0.35849, 0.00057742, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0406227, None, 0.000823226, None, -0.0404926, None, 0.000882959, None, -0.0404926, None, 0.000882959, None, -0.0409293, None, 0.000902457, None, -0.0409293, None, 0.000902457, None, 0.358579, None, 0.0077421, None, 0.358579, None, 0.0077421, None)
reports[-1].CovMatrix = ['6.77959e-07','-8.78594e-08','-1.75564e-09','1.26284e-10','0','0','0','0','0','-8.78594e-08','8.99712e-05','-2.20924e-09','1.61897e-09','0','0','0','0','0','-1.75564e-09','-2.20924e-09','2.7986e-10','2.58517e-12','0','0','0','0','0','1.26284e-10','1.61897e-09','2.58517e-12','3.33414e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 194140
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0450859, 0.000813962, 0), \
                           ValErr(0.0214065, 0.00940607, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.95449e-05, 1.64237e-05, 0), \
                           -73479.5, 194140, 194140, -nan)
reports[-1].sigmaresid = ValErr(0.353295, 0.000575043, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0467211, None, 2.91797e-05, None, -0.0454016, None, 2.93706e-05, None, -0.0454016, None, 2.93706e-05, None, -0.0458222, None, 2.19283e-05, None, -0.0458222, None, 2.19283e-05, None, 0.353305, None, 0.00772345, None, 0.353305, None, 0.00772345, None)
reports[-1].CovMatrix = ['6.62535e-07','-2.85803e-08','-2.18025e-09','2.1164e-09','0','0','0','0','0','-2.85803e-08','8.84742e-05','-1.1719e-10','2.26153e-08','0','0','0','0','0','-2.18025e-09','-1.1719e-10','2.69737e-10','-1.66842e-10','0','0','0','0','0','2.1164e-09','2.26153e-08','-1.66842e-10','3.30675e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 172332
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0646915, 0.000869031, 0), \
                           ValErr(0.0443229, 0.00987817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.19931e-07, 1.73647e-05, 0), \
                           -66043.4, 172332, 172332, -nan)
reports[-1].sigmaresid = ValErr(0.354976, 0.000611989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0653202, None, -0.000984749, None, -0.0647234, None, -0.00105, None, -0.0647234, None, -0.00105, None, -0.0659692, None, -0.00111671, None, -0.0659692, None, -0.00111671, None, 0.354997, None, 0.00815362, None, 0.354997, None, 0.00815362, None)
reports[-1].CovMatrix = ['7.55216e-07','-1.17005e-08','-2.33019e-09','8.17201e-09','0','0','0','0','0','-1.17005e-08','9.75782e-05','3.81016e-09','-5.22457e-08','0','0','0','0','0','-2.33019e-09','3.81016e-09','3.01534e-10','-2.33797e-10','0','0','0','0','0','8.17201e-09','-5.22457e-08','-2.33797e-10','3.7453e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 159865
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0479593, 0.000897362, 0), \
                           ValErr(-0.00722805, 0.0104911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.99968e-06, 1.77739e-05, 0), \
                           -61928, 159865, 159865, -nan)
reports[-1].sigmaresid = ValErr(0.35645, 0.000630385, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0485754, None, 0.000609379, None, -0.0479036, None, 0.000699851, None, -0.0479036, None, 0.000699851, None, -0.0473957, None, 0.000753826, None, -0.0473957, None, 0.000753826, None, 0.356451, None, 0.00836245, None, 0.356451, None, 0.00836245, None)
reports[-1].CovMatrix = ['8.05259e-07','-3.80241e-08','-1.81942e-09','1.52497e-10','0','0','0','0','0','-3.80241e-08','0.000110062','1.65863e-09','2.02197e-09','0','0','0','0','0','-1.81942e-09','1.65863e-09','3.1591e-10','3.07743e-12','0','0','0','0','0','1.52497e-10','2.02197e-09','3.07743e-12','3.97386e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 189896
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0154726, 0.000826858, 0), \
                           ValErr(0.0052433, 0.00957196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000102686, 1.65731e-05, 0), \
                           -73223.5, 189896, 189896, -nan)
reports[-1].sigmaresid = ValErr(0.355816, 0.000577366, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0164791, None, -0.00128074, None, -0.0162589, None, -0.00134598, None, -0.0162589, None, -0.00134598, None, -0.017509, None, -0.00144216, None, -0.017509, None, -0.00144216, None, 0.355853, None, 0.00783826, None, 0.355853, None, 0.00783826, None)
reports[-1].CovMatrix = ['6.83695e-07','-2.02383e-07','-2.13392e-09','1.20575e-10','0','0','0','0','0','-2.02383e-07','9.16225e-05','1.11825e-09','1.66509e-09','0','0','0','0','0','-2.13392e-09','1.11825e-09','2.74669e-10','2.51889e-12','0','0','0','0','0','1.20575e-10','1.66509e-09','2.51889e-12','3.33352e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 193804
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0056578, 0.000816901, 0), \
                           ValErr(-0.000658165, 0.0132502, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.50179e-05, 1.6319e-05, 0), \
                           -73805.6, 193804, 193804, -nan)
reports[-1].sigmaresid = ValErr(0.354122, 0.00056962, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00526312, None, -0.0011431, None, 0.00578132, None, -0.00122105, None, 0.00578132, None, -0.00122105, None, 0.00602438, None, -0.00128357, None, 0.00602438, None, -0.00128357, None, 0.354123, None, 0.00772525, None, 0.354123, None, 0.00772525, None)
reports[-1].CovMatrix = ['6.67328e-07','-4.68913e-07','-2.19737e-09','1.35523e-09','0','0','0','0','0','-4.68913e-07','0.000175569','1.10935e-09','-2.85597e-07','0','0','0','0','0','-2.19737e-09','1.10935e-09','2.66309e-10','-3.83948e-12','0','0','0','0','0','1.35523e-09','-2.85597e-07','-3.83948e-12','3.24467e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 195640
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0185858, 0.000821114, 0), \
                           ValErr(-0.0194376, 0.00955781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000108885, 1.65255e-05, 0), \
                           -74159.7, 195640, 195640, -nan)
reports[-1].sigmaresid = ValErr(0.353498, 0.000586849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.019112, None, -0.000378864, None, 0.0195031, None, -0.000359085, None, 0.0195031, None, -0.000359085, None, 0.0196928, None, -0.000394673, None, 0.0196928, None, -0.000394673, None, 0.353542, None, 0.00777396, None, 0.353542, None, 0.00777396, None)
reports[-1].CovMatrix = ['6.74228e-07','-2.73856e-07','-1.97536e-09','1.77136e-08','0','0','0','0','0','-2.73856e-07','9.13517e-05','-3.18348e-09','-2.8903e-07','0','0','0','0','0','-1.97536e-09','-3.18348e-09','2.73091e-10','3.31728e-10','0','0','0','0','0','1.77136e-08','-2.8903e-07','3.31728e-10','3.44392e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 197436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.012432, 0.000804237, 0), \
                           ValErr(-0.0179342, 0.00929707, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000128226, 1.61986e-05, 0), \
                           -74007.1, 197436, 197436, -nan)
reports[-1].sigmaresid = ValErr(0.352009, 0.000560176, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.012212, None, -0.000344102, None, 0.0135118, None, -0.000419454, None, 0.0135118, None, -0.000419454, None, 0.0136866, None, -0.000431135, None, 0.0136866, None, -0.000431135, None, 0.352069, None, 0.00772906, None, 0.352069, None, 0.00772906, None)
reports[-1].CovMatrix = ['6.46797e-07','-7.57571e-08','-2.24062e-09','1.10649e-10','0','0','0','0','0','-7.57571e-08','8.64355e-05','-1.65429e-11','1.55041e-09','0','0','0','0','0','-2.24062e-09','-1.65429e-11','2.62396e-10','2.28444e-12','0','0','0','0','0','1.10649e-10','1.55041e-09','2.28444e-12','3.13798e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 52922
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.043708, 0.004538, 0), \
                           ValErr(0.029454, 0.110564, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.94051e-05, 4.54445e-05, 0), \
                           -68892.9, 52922, 52922, -nan)
reports[-1].sigmaresid = ValErr(0.889445, 0.00273392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0360781, None, -0.000342152, None, -0.0417704, None, -0.000166484, None, -0.0417704, None, -0.000166484, None, -0.0491351, None, -9.78845e-05, None, -0.0491351, None, -9.78845e-05, None, 0.889453, None, 0.00743814, None, 0.889453, None, 0.00743814, None)
reports[-1].CovMatrix = ['2.05935e-05','-0.000174947','-8.37591e-08','2.42949e-09','0','0','0','0','0','-0.000174947','0.0122245','2.30733e-07','1.22868e-07','0','0','0','0','0','-8.37591e-08','2.30733e-07','2.06521e-09','4.60239e-11','0','0','0','0','0','2.42949e-09','1.22868e-07','4.60239e-11','7.47432e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 47663
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.023606, 0.00484758, 0), \
                           ValErr(-0.262937, 0.114757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.44357e-05, 4.71066e-05, 0), \
                           -60412.3, 47663, 47663, -nan)
reports[-1].sigmaresid = ValErr(0.859462, 0.00278369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0181684, None, 0.00136241, None, -0.0214616, None, 0.00135002, None, -0.0214616, None, 0.00135002, None, -0.0220056, None, 0.00159432, None, -0.0220056, None, 0.00159432, None, 0.859517, None, 0.00740706, None, 0.859517, None, 0.00740706, None)
reports[-1].CovMatrix = ['2.34991e-05','0.000211796','-1.09411e-07','8.10366e-09','0','0','0','0','0','0.000211796','0.0131692','-5.57961e-07','2.52029e-07','0','0','0','0','0','-1.09411e-07','-5.57961e-07','2.21903e-09','3.20972e-11','0','0','0','0','0','8.10366e-09','2.52029e-07','3.20972e-11','7.74895e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 46635
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0158596, 0.00525723, 0), \
                           ValErr(0.213356, 0.101741, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.39277e-05, 5.05744e-05, 0), \
                           -53272.3, 46635, 46635, -nan)
reports[-1].sigmaresid = ValErr(0.758346, 0.00248311, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0223714, None, -0.00111937, None, -0.0221667, None, -0.00112115, None, -0.0221667, None, -0.00112115, None, -0.0292705, None, -0.00121358, None, -0.0292705, None, -0.00121358, None, 0.758402, None, 0.00642376, None, 0.758402, None, 0.00642376, None)
reports[-1].CovMatrix = ['2.76385e-05','6.33952e-06','-1.97814e-07','2.68166e-09','0','0','0','0','0','6.33952e-06','0.0103513','-2.00632e-07','1.26665e-07','0','0','0','0','0','-1.97814e-07','-2.00632e-07','2.55777e-09','2.26365e-11','0','0','0','0','0','2.68166e-09','1.26665e-07','2.26365e-11','6.16585e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 53146
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0419011, 0.00469513, 0), \
                           ValErr(0.105502, 0.0989683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00019691, 4.71111e-05, 0), \
                           -63685.8, 53146, 53146, -nan)
reports[-1].sigmaresid = ValErr(0.802024, 0.0024355, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0582383, None, -0.000525815, None, -0.0553765, None, -0.000453911, None, -0.0553765, None, -0.000453911, None, -0.0523314, None, -0.000503416, None, -0.0523314, None, -0.000503416, None, 0.802158, None, 0.00651001, None, 0.802158, None, 0.00651001, None)
reports[-1].CovMatrix = ['2.20443e-05','1.19142e-05','-1.52628e-07','2.19778e-07','0','0','0','0','0','1.19142e-05','0.00979472','-1.62691e-07','3.7e-06','0','0','0','0','0','-1.52628e-07','-1.62691e-07','2.21945e-09','5.77427e-10','0','0','0','0','0','2.19778e-07','3.7e-06','5.77427e-10','5.93167e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 66085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0506215, 0.00387188, 0), \
                           ValErr(-0.0698148, 0.0902661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132381, 4.07814e-05, 0), \
                           -84034, 66085, 66085, -nan)
reports[-1].sigmaresid = ValErr(0.863008, 0.0023483, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0611528, None, -0.000210382, None, -0.0568871, None, -0.000133863, None, -0.0568871, None, -0.000133863, None, -0.0533657, None, -0.000204314, None, -0.0533657, None, -0.000204314, None, 0.863077, None, 0.00698545, None, 0.863077, None, 0.00698545, None)
reports[-1].CovMatrix = ['1.49915e-05','-5.2875e-06','-7.92051e-08','2.1512e-08','0','0','0','0','0','-5.2875e-06','0.00814796','8.83517e-08','-1.81031e-06','0','0','0','0','0','-7.92051e-08','8.83517e-08','1.66312e-09','1.13321e-09','0','0','0','0','0','2.1512e-08','-1.81031e-06','1.13321e-09','5.5145e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 68352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0344888, 0.00366399, 0), \
                           ValErr(-0.103736, 0.0869855, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.07418e-05, 3.94894e-05, 0), \
                           -88006.8, 68352, 68352, -nan)
reports[-1].sigmaresid = ValErr(0.876884, 0.00225488, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0339068, None, 0.000316743, None, -0.0348362, None, 0.000570156, None, -0.0348362, None, 0.000570156, None, -0.0397401, None, 0.000609451, None, -0.0397401, None, 0.000609451, None, 0.876888, None, 0.0075693, None, 0.876888, None, 0.0075693, None)
reports[-1].CovMatrix = ['1.34248e-05','-4.44815e-06','-6.51892e-08','-5.16933e-07','0','0','0','0','0','-4.44815e-06','0.00756647','-9.5574e-08','-1.66423e-05','0','0','0','0','0','-6.51892e-08','-9.5574e-08','1.55941e-09','-6.07324e-11','0','0','0','0','0','-5.16933e-07','-1.66423e-05','-6.07324e-11','5.08448e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 61701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0758424, 0.00397584, 0), \
                           ValErr(-0.000553547, 0.055368, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000242709, 4.1446e-05, 0), \
                           -77971.6, 61701, 61701, -nan)
reports[-1].sigmaresid = ValErr(0.85621, 0.0024307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0593039, None, 0.000544596, None, -0.0642996, None, 0.000723317, None, -0.0642996, None, 0.000723317, None, -0.0699015, None, 0.000749024, None, -0.0699015, None, 0.000749024, None, 0.856448, None, 0.00736727, None, 0.856448, None, 0.00736727, None)
reports[-1].CovMatrix = ['1.58073e-05','-1.52834e-05','-8.21706e-08','4.00916e-09','0','0','0','0','0','-1.52834e-05','0.00306561','1.57553e-07','5.17369e-06','0','0','0','0','0','-8.21706e-08','1.57553e-07','1.71777e-09','2.58296e-10','0','0','0','0','0','4.00916e-09','5.17369e-06','2.58296e-10','5.90829e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 69147
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0866235, 0.00375712, 0), \
                           ValErr(0.192441, 0.0879589, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.52317e-05, 4.00125e-05, 0), \
                           -87732.3, 69147, 69147, -nan)
reports[-1].sigmaresid = ValErr(0.860572, 0.00231305, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0789193, None, 0.000899122, None, -0.0842502, None, 0.00107906, None, -0.0842502, None, 0.00107906, None, -0.0828641, None, 0.0011109, None, -0.0828641, None, 0.0011109, None, 0.860613, None, 0.00698435, None, 0.860613, None, 0.00698435, None)
reports[-1].CovMatrix = ['1.4116e-05','9.03517e-06','-7.38791e-08','-1.30373e-09','0','0','0','0','0','9.03517e-06','0.00773676','-5.06909e-08','2.05231e-08','0','0','0','0','0','-7.38791e-08','-5.06909e-08','1.601e-09','9.8218e-11','0','0','0','0','0','-1.30373e-09','2.05231e-08','9.8218e-11','5.35021e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 56114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0846707, 0.0041068, 0), \
                           ValErr(0.140979, 0.0978913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00014228, 4.08717e-05, 0), \
                           -69645.4, 56114, 56114, -nan)
reports[-1].sigmaresid = ValErr(0.837114, 0.0024537, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0698513, None, 0.000387945, None, -0.0773384, None, 0.000596178, None, -0.0773384, None, 0.000596178, None, -0.0777381, None, 0.000617974, None, -0.0777381, None, 0.000617974, None, 0.837212, None, 0.00738434, None, 0.837212, None, 0.00738434, None)
reports[-1].CovMatrix = ['1.68658e-05','-1.80852e-05','-8.6266e-08','3.60129e-08','0','0','0','0','0','-1.80852e-05','0.00958271','2.85855e-07','-4.10952e-06','0','0','0','0','0','-8.6266e-08','2.85855e-07','1.67049e-09','1.84695e-09','0','0','0','0','0','3.60129e-08','-4.10952e-06','1.84695e-09','6.02066e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 73321
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0754759, 0.00361548, 0), \
                           ValErr(0.216044, 0.0882772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.88611e-05, 3.84084e-05, 0), \
                           -95084.5, 73321, 73321, -nan)
reports[-1].sigmaresid = ValErr(0.885049, 0.00231016, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0752079, None, -0.000350806, None, -0.0766721, None, -0.000414471, None, -0.0766721, None, -0.000414471, None, -0.0762886, None, -0.000445589, None, -0.0762886, None, -0.000445589, None, 0.885088, None, 0.00718548, None, 0.885088, None, 0.00718548, None)
reports[-1].CovMatrix = ['1.30717e-05','1.13518e-06','-5.93177e-08','-7.48866e-09','0','0','0','0','0','1.13518e-06','0.00779287','6.93669e-09','5.12766e-08','0','0','0','0','0','-5.93177e-08','6.93669e-09','1.4752e-09','1.81181e-10','0','0','0','0','0','-7.48866e-09','5.12766e-08','1.81181e-10','5.33682e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 60536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0415422, 0.00392649, 0), \
                           ValErr(-0.0918003, 0.092612, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000134398, 4.06805e-05, 0), \
                           -77100.9, 60536, 60536, -nan)
reports[-1].sigmaresid = ValErr(0.864763, 0.00247591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0502874, None, -0.00137239, None, -0.0472745, None, -0.00134298, None, -0.0472745, None, -0.00134298, None, -0.0448328, None, -0.00146236, None, -0.0448328, None, -0.00146236, None, 0.864846, None, 0.0071774, None, 0.864846, None, 0.0071774, None)
reports[-1].CovMatrix = ['1.54173e-05','2.14605e-06','-7.14129e-08','5.6324e-09','0','0','0','0','0','2.14605e-06','0.00857698','5.68283e-08','-5.78777e-07','0','0','0','0','0','-7.14129e-08','5.68283e-08','1.6549e-09','4.60511e-10','0','0','0','0','0','5.6324e-09','-5.78777e-07','4.60511e-10','6.13013e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 71836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0585342, 0.00362301, 0), \
                           ValErr(0.287661, 0.0865451, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.55791e-05, 3.85561e-05, 0), \
                           -91843.7, 71836, 71836, -nan)
reports[-1].sigmaresid = ValErr(0.868996, 0.00228286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0601733, None, -0.00030861, None, -0.0613219, None, -0.000228087, None, -0.0613219, None, -0.000228087, None, -0.0676528, None, -0.000229099, None, -0.0676528, None, -0.000229099, None, 0.869076, None, 0.00742667, None, 0.869076, None, 0.00742667, None)
reports[-1].CovMatrix = ['1.31262e-05','3.82272e-06','-6.25206e-08','5.31972e-11','0','0','0','0','0','3.82272e-06','0.00749006','-7.43992e-08','8.62131e-07','0','0','0','0','0','-6.25206e-08','-7.43992e-08','1.48657e-09','5.23779e-10','0','0','0','0','0','5.31972e-11','8.62131e-07','5.23779e-10','5.21144e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 56420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0647163, 0.00412001, 0), \
                           ValErr(0.185678, 0.0976195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000324475, 4.17096e-05, 0), \
                           -71684, 56420, 56420, -nan)
reports[-1].sigmaresid = ValErr(0.862091, 0.00256581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0427241, None, 0.000276187, None, -0.049877, None, 0.000304892, None, -0.049877, None, 0.000304892, None, -0.0507221, None, 0.000288064, None, -0.0507221, None, 0.000288064, None, 0.862584, None, 0.0070056, None, 0.862584, None, 0.0070056, None)
reports[-1].CovMatrix = ['1.69745e-05','1.58338e-05','-8.11426e-08','-5.08526e-09','0','0','0','0','0','1.58338e-05','0.00952957','-8.11664e-08','-1.06602e-08','0','0','0','0','0','-8.11426e-08','-8.11664e-08','1.73969e-09','9.87445e-11','0','0','0','0','0','-5.08526e-09','-1.06602e-08','9.87445e-11','6.58336e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 52397
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0511661, 0.00432869, 0), \
                           ValErr(-0.207349, 0.100848, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00012054, 4.39441e-05, 0), \
                           -65513.8, 52397, 52397, -nan)
reports[-1].sigmaresid = ValErr(0.844845, 0.00260981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0364125, None, 0.000414417, None, -0.0450273, None, 0.000676489, None, -0.0450273, None, 0.000676489, None, -0.0437608, None, 0.00061921, None, -0.0437608, None, 0.00061921, None, 0.844936, None, 0.00722782, None, 0.844936, None, 0.00722782, None)
reports[-1].CovMatrix = ['1.87375e-05','4.12968e-06','-9.93782e-08','3.51325e-09','0','0','0','0','0','4.12968e-06','0.0101703','-1.4439e-07','1.39892e-07','0','0','0','0','0','-9.93782e-08','-1.4439e-07','1.93108e-09','3.29462e-11','0','0','0','0','0','3.51325e-09','1.39892e-07','3.29462e-11','6.81112e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 53124
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00637192, 0.00424298, 0), \
                           ValErr(0.28694, 0.102213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000165577, 4.3052e-05, 0), \
                           -67845.6, 53124, 53124, -nan)
reports[-1].sigmaresid = ValErr(0.867777, 0.00266224, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0071213, None, -0.000705585, None, -0.00153771, None, -0.000641362, None, -0.00153771, None, -0.000641362, None, -0.00375993, None, -0.000715547, None, -0.00375993, None, -0.000715547, None, 0.867958, None, 0.00717116, None, 0.867958, None, 0.00717116, None)
reports[-1].CovMatrix = ['1.80029e-05','1.96157e-05','-8.39841e-08','4.076e-09','0','0','0','0','0','1.96157e-05','0.0104475','-9.59205e-08','1.54313e-07','0','0','0','0','0','-8.39841e-08','-9.59205e-08','1.85348e-09','3.70745e-11','0','0','0','0','0','4.076e-09','1.54313e-07','3.70745e-11','7.08755e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 48275
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0233644, 0.00455153, 0), \
                           ValErr(-0.144758, 0.104038, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.22922e-05, 4.55847e-05, 0), \
                           -59690.9, 48275, 48275, -nan)
reports[-1].sigmaresid = ValErr(0.833216, 0.00268152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0194263, None, 0.000483584, None, -0.0214971, None, 0.000568098, None, -0.0214971, None, 0.000568098, None, -0.0199832, None, 0.000594346, None, -0.0199832, None, 0.000594346, None, 0.833241, None, 0.00723878, None, 0.833241, None, 0.00723878, None)
reports[-1].CovMatrix = ['2.07164e-05','-4.67949e-05','-1.13855e-07','2.93766e-09','0','0','0','0','0','-4.67949e-05','0.0108239','2.63482e-07','1.44098e-07','0','0','0','0','0','-1.13855e-07','2.63482e-07','2.07796e-09','3.9415e-11','0','0','0','0','0','2.93766e-09','1.44098e-07','3.9415e-11','7.19056e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 57839
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0187472, 0.00421476, 0), \
                           ValErr(0.553976, 0.098724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.19613e-05, 4.38248e-05, 0), \
                           -72558.6, 57839, 57839, -nan)
reports[-1].sigmaresid = ValErr(0.848364, 0.00249435, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0180163, None, 0.000461397, None, -0.0205248, None, 0.000654417, None, -0.0205248, None, 0.000654417, None, -0.021267, None, 0.00067905, None, -0.021267, None, 0.00067905, None, 0.848601, None, 0.00727337, None, 0.848601, None, 0.00727337, None)
reports[-1].CovMatrix = ['1.77642e-05','-6.88134e-06','-1.00974e-07','3.00143e-09','0','0','0','0','0','-6.88134e-06','0.00974643','3.36762e-07','1.44464e-07','0','0','0','0','0','-1.00974e-07','3.36762e-07','1.92062e-09','3.72284e-11','0','0','0','0','0','3.00143e-09','1.44464e-07','3.72284e-11','6.22179e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 62491
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0122773, 0.00390127, 0), \
                           ValErr(-0.039058, 0.092746, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.04119e-05, 3.99321e-05, 0), \
                           -78962.2, 62491, 62491, -nan)
reports[-1].sigmaresid = ValErr(0.856106, 0.00242161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0189333, None, 0.000442684, None, -0.0160163, None, 0.000587591, None, -0.0160163, None, 0.000587591, None, -0.0196451, None, 0.000633764, None, -0.0196451, None, 0.000633764, None, 0.856134, None, 0.00726195, None, 0.856134, None, 0.00726195, None)
reports[-1].CovMatrix = ['1.52199e-05','2.86667e-06','-7.45818e-08','3.1247e-09','0','0','0','0','0','2.86667e-06','0.00860183','5.07278e-08','1.2622e-07','0','0','0','0','0','-7.45818e-08','5.07278e-08','1.59458e-09','3.2145e-11','0','0','0','0','0','3.1247e-09','1.2622e-07','3.2145e-11','5.8642e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 68668
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0221541, 0.0037524, 0), \
                           ValErr(0.212066, 0.090754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000144736, 3.9521e-05, 0), \
                           -89321.4, 68668, 68668, -nan)
reports[-1].sigmaresid = ValErr(0.888549, 0.00239767, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0299401, None, -0.000442898, None, -0.0281674, None, -0.000358155, None, -0.0281674, None, -0.000358155, None, -0.0266694, None, -0.000366077, None, -0.0266694, None, -0.000366077, None, 0.88867, None, 0.00801174, None, 0.88867, None, 0.00801174, None)
reports[-1].CovMatrix = ['1.40805e-05','4.28488e-06','-6.34774e-08','3.23559e-09','0','0','0','0','0','4.28488e-06','0.00823629','1.91648e-08','1.23244e-07','0','0','0','0','0','-6.34774e-08','1.91648e-08','1.56191e-09','3.34766e-11','0','0','0','0','0','3.23559e-09','1.23244e-07','3.34766e-11','5.74883e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 39579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0109362, 0.00582527, 0), \
                           ValErr(0.0930765, 0.0748979, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000153779, 5.34508e-05, 0), \
                           -46224.3, 39579, 39579, -nan)
reports[-1].sigmaresid = ValErr(0.777993, 0.00276252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0207431, None, -0.000939568, None, -0.0235138, None, -0.00075826, None, -0.0235138, None, -0.00075826, None, -0.0271774, None, -0.000752147, None, -0.0271774, None, -0.000752147, None, 0.778076, None, 0.00723269, None, 0.778076, None, 0.00723269, None)
reports[-1].CovMatrix = ['3.39338e-05','8.61664e-05','-2.30599e-07','1.71026e-08','0','0','0','0','0','8.61664e-05','0.00560969','-8.84581e-07','9.93491e-06','0','0','0','0','0','-2.30599e-07','-8.84581e-07','2.85699e-09','3.74914e-10','0','0','0','0','0','1.71026e-08','9.93491e-06','3.74914e-10','7.63154e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 47954
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0501157, 0.00531847, 0), \
                           ValErr(0.0246508, 0.100854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000169979, 5.33585e-05, 0), \
                           -55877.7, 47954, 47954, -nan)
reports[-1].sigmaresid = ValErr(0.775922, 0.0025051, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0372297, None, -0.0006727, None, -0.0376045, None, -0.000558268, None, -0.0376045, None, -0.000558268, None, -0.034529, None, -0.000712114, None, -0.034529, None, -0.000712114, None, 0.776004, None, 0.00719584, None, 0.776004, None, 0.00719584, None)
reports[-1].CovMatrix = ['2.82862e-05','-9.6979e-05','-2.10662e-07','5.28553e-09','0','0','0','0','0','-9.6979e-05','0.0101715','8.46375e-07','-1.43918e-08','0','0','0','0','0','-2.10662e-07','8.46375e-07','2.84713e-09','-8.23925e-11','0','0','0','0','0','5.28553e-09','-1.43918e-08','-8.23925e-11','6.27553e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 54909
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0276551, 0.00416033, 0), \
                           ValErr(0.442816, 0.098625, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000207759, 4.18876e-05, 0), \
                           -67991.9, 54909, 54909, -nan)
reports[-1].sigmaresid = ValErr(0.834708, 0.00251882, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0371278, None, 3.83243e-05, None, -0.0371343, None, -5.83813e-05, None, -0.0371343, None, -5.83813e-05, None, -0.0375839, None, -0.000104331, None, -0.0375839, None, -0.000104331, None, 0.83507, None, 0.00778459, None, 0.83507, None, 0.00778459, None)
reports[-1].CovMatrix = ['1.73083e-05','-3.53122e-05','-8.95018e-08','2.51941e-09','0','0','0','0','0','-3.53122e-05','0.00972689','2.44412e-07','1.31443e-07','0','0','0','0','0','-8.95018e-08','2.44412e-07','1.75457e-09','3.82623e-11','0','0','0','0','0','2.51941e-09','1.31443e-07','3.82623e-11','6.34447e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 71552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0588084, 0.00353516, 0), \
                           ValErr(0.061915, 0.0704453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.07232e-05, 3.86187e-05, 0), \
                           -91965.5, 71552, 71552, -nan)
reports[-1].sigmaresid = ValErr(0.874906, 0.00226324, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0569486, None, 0.000314023, None, -0.0571509, None, 0.000467988, None, -0.0571509, None, 0.000467988, None, -0.0524325, None, 0.00040224, None, -0.0524325, None, 0.00040224, None, 0.874913, None, 0.00788817, None, 0.874913, None, 0.00788817, None)
reports[-1].CovMatrix = ['1.24974e-05','4.41845e-05','-6.43297e-08','-3.85179e-07','0','0','0','0','0','4.41845e-05','0.00496254','1.44744e-07','2.36933e-05','0','0','0','0','0','-6.43297e-08','1.44744e-07','1.4914e-09','-1.08873e-09','0','0','0','0','0','-3.85179e-07','2.36933e-05','-1.08873e-09','5.12226e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 61651
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0445746, 0.00390672, 0), \
                           ValErr(0.123892, 0.0905531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000156394, 4.01499e-05, 0), \
                           -76574.5, 61651, 61651, -nan)
reports[-1].sigmaresid = ValErr(0.837885, 0.0023855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0343618, None, 0.000276237, None, -0.0370255, None, 0.000394479, None, -0.0370255, None, 0.000394479, None, -0.0368443, None, 0.000365806, None, -0.0368443, None, 0.000365806, None, 0.838001, None, 0.00734872, None, 0.838001, None, 0.00734872, None)
reports[-1].CovMatrix = ['1.52625e-05','9.23512e-06','-7.90552e-08','2.09119e-11','0','0','0','0','0','9.23512e-06','0.00819987','-4.42788e-08','-2.28728e-08','0','0','0','0','0','-7.90552e-08','-4.42788e-08','1.61201e-09','3.92875e-11','0','0','0','0','0','2.09119e-11','-2.28728e-08','3.92875e-11','5.69063e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 69792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0694492, 0.00363709, 0), \
                           ValErr(-0.00582994, 0.0502443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.1769e-05, 3.83026e-05, 0), \
                           -89143.6, 69792, 69792, -nan)
reports[-1].sigmaresid = ValErr(0.867912, 0.00231528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0637346, None, 8.42549e-05, None, -0.0673495, None, -0.000144695, None, -0.0673495, None, -0.000144695, None, -0.0653682, None, -0.000188783, None, -0.0653682, None, -0.000188783, None, 0.867925, None, 0.00808574, None, 0.867925, None, 0.00808574, None)
reports[-1].CovMatrix = ['1.32284e-05','-1.70157e-06','-5.97957e-08','-1.20632e-08','0','0','0','0','0','-1.70157e-06','0.00252448','1.71962e-08','1.05727e-06','0','0','0','0','0','-5.97957e-08','1.71962e-08','1.46709e-09','5.13292e-10','0','0','0','0','0','-1.20632e-08','1.05727e-06','5.13292e-10','5.36051e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 53137
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0610141, 0.0043488, 0), \
                           ValErr(-0.192006, 0.0980857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000100408, 4.31013e-05, 0), \
                           -65923, 53137, 53137, -nan)
reports[-1].sigmaresid = ValErr(0.836681, 0.0025511, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0651862, None, -0.00126049, None, -0.0664959, None, -0.00119532, None, -0.0664959, None, -0.00119532, None, -0.0642747, None, -0.00132515, None, -0.0642747, None, -0.00132515, None, 0.836752, None, 0.00754985, None, 0.836752, None, 0.00754985, None)
reports[-1].CovMatrix = ['1.89121e-05','9.96975e-06','-1.03942e-07','6.91011e-08','0','0','0','0','0','9.96975e-06','0.00962081','-4.71883e-08','-1.3399e-06','0','0','0','0','0','-1.03942e-07','-4.71883e-08','1.85772e-09','2.00938e-10','0','0','0','0','0','6.91011e-08','-1.3399e-06','2.00938e-10','6.50811e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 61409
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0634125, 0.00389862, 0), \
                           ValErr(0.278741, 0.0920993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.22761e-05, 4.02287e-05, 0), \
                           -78349.3, 61409, 61409, -nan)
reports[-1].sigmaresid = ValErr(0.866688, 0.00246581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0581759, None, 0.000259144, None, -0.0620964, None, 0.000446107, None, -0.0620964, None, 0.000446107, None, -0.0603937, None, 0.00045292, None, -0.0603937, None, 0.00045292, None, 0.866753, None, 0.00786539, None, 0.866753, None, 0.00786539, None)
reports[-1].CovMatrix = ['1.51992e-05','-9.73891e-06','-6.92393e-08','-6.71944e-09','0','0','0','0','0','-9.73891e-06','0.00848228','-4.41623e-08','8.27745e-07','0','0','0','0','0','-6.92393e-08','-4.41623e-08','1.61835e-09','5.09579e-10','0','0','0','0','0','-6.71944e-09','8.27745e-07','5.09579e-10','6.08021e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 55354
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0765918, 0.00409092, 0), \
                           ValErr(-0.188568, 0.0981347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000130595, 4.06385e-05, 0), \
                           -71152.6, 55354, 55354, -nan)
reports[-1].sigmaresid = ValErr(0.875006, 0.00260656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0688532, None, -0.00167705, None, -0.071112, None, -0.00179653, None, -0.071112, None, -0.00179653, None, -0.0743509, None, -0.00194585, None, -0.0743509, None, -0.00194585, None, 0.875112, None, 0.00856295, None, 0.875112, None, 0.00856295, None)
reports[-1].CovMatrix = ['1.67357e-05','1.36428e-06','-6.92176e-08','-7.52077e-08','0','0','0','0','0','1.36428e-06','0.00963042','2.89415e-08','-2.53755e-06','0','0','0','0','0','-6.92176e-08','2.89415e-08','1.65149e-09','2.06225e-09','0','0','0','0','0','-7.52077e-08','-2.53755e-06','2.06225e-09','6.79415e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 62013
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0395099, 0.00390856, 0), \
                           ValErr(-0.28014, 0.0929501, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.1393e-05, 4.08828e-05, 0), \
                           -79415.7, 62013, 62013, -nan)
reports[-1].sigmaresid = ValErr(0.870831, 0.00247041, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0408798, None, 0.000171358, None, -0.0402219, None, 9.08892e-05, None, -0.0402219, None, 9.08892e-05, None, -0.0367492, None, 4.02342e-05, None, -0.0367492, None, 4.02342e-05, None, 0.870894, None, 0.00800831, None, 0.870894, None, 0.00800831, None)
reports[-1].CovMatrix = ['1.52769e-05','-7.26146e-06','-7.15177e-08','2.15178e-09','0','0','0','0','0','-7.26146e-06','0.00863971','1.11667e-08','-1.53903e-07','0','0','0','0','0','-7.15177e-08','1.11667e-08','1.67141e-09','2.14376e-10','0','0','0','0','0','2.15178e-09','-1.53903e-07','2.14376e-10','6.10291e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 66286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0462059, 0.00387034, 0), \
                           ValErr(-0.232076, 0.088116, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.50341e-05, 4.14723e-05, 0), \
                           -82463, 66286, 66286, -nan)
reports[-1].sigmaresid = ValErr(0.83955, 0.0023058, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0483721, None, 1.36658e-06, None, -0.0470932, None, 9.66518e-05, None, -0.0470932, None, 9.66518e-05, None, -0.0478725, None, 5.40966e-05, None, -0.0478725, None, 5.40966e-05, None, 0.839596, None, 0.00759904, None, 0.839596, None, 0.00759904, None)
reports[-1].CovMatrix = ['1.49795e-05','1.20504e-05','-8.62638e-08','2.85099e-09','0','0','0','0','0','1.20504e-05','0.00776443','5.62281e-09','1.16169e-07','0','0','0','0','0','-8.62638e-08','5.62281e-09','1.71995e-09','2.84667e-11','0','0','0','0','0','2.85099e-09','1.16169e-07','2.84667e-11','5.3167e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 46535
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0506113, 0.00437073, 0), \
                           ValErr(0.0683729, 0.0631782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109887, 4.4075e-05, 0), \
                           -58332.1, 46535, 46535, -nan)
reports[-1].sigmaresid = ValErr(0.847529, 0.00277676, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0442162, None, -0.000128724, None, -0.0459292, None, 0.000162437, None, -0.0459292, None, 0.000162437, None, -0.0486584, None, 0.000121394, None, -0.0486584, None, 0.000121394, None, 0.847591, None, 0.00817948, None, 0.847591, None, 0.00817948, None)
reports[-1].CovMatrix = ['1.91033e-05','1.7094e-05','-8.43183e-08','-4.9638e-09','0','0','0','0','0','1.7094e-05','0.00399148','-4.12929e-08','3.09399e-07','0','0','0','0','0','-8.43183e-08','-4.12929e-08','1.94261e-09','2.29716e-10','0','0','0','0','0','-4.9638e-09','3.09399e-07','2.29716e-10','7.71039e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 48948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0218209, 0.00451705, 0), \
                           ValErr(-0.179387, 0.103964, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.82827e-05, 4.75327e-05, 0), \
                           -62023.2, 48948, 48948, -nan)
reports[-1].sigmaresid = ValErr(0.859148, 0.00274591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0235732, None, -0.000370065, None, -0.0190217, None, -0.000265232, None, -0.0190217, None, -0.000265232, None, -0.0144508, None, -0.000357095, None, -0.0144508, None, -0.000357095, None, 0.859188, None, 0.00766134, None, 0.859188, None, 0.00766134, None)
reports[-1].CovMatrix = ['2.04038e-05','-7.84763e-06','-1.09671e-07','3.7674e-09','0','0','0','0','0','-7.84763e-06','0.0108086','1.25358e-07','1.58269e-07','0','0','0','0','0','-1.09671e-07','1.25358e-07','2.25936e-09','4.25756e-11','0','0','0','0','0','3.7674e-09','1.58269e-07','4.25756e-11','7.54e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 41402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0102181, 0.00478313, 0), \
                           ValErr(-0.164642, 0.109007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.30075e-05, 4.85262e-05, 0), \
                           -50803.4, 41402, 41402, -nan)
reports[-1].sigmaresid = ValErr(0.825418, 0.00286845, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0085879, None, -0.000156676, None, -0.0117714, None, -0.000324502, None, -0.0117714, None, -0.000324502, None, -0.00625889, None, -0.000363393, None, -0.00625889, None, -0.000363393, None, 0.825448, None, 0.00787133, None, 0.825448, None, 0.00787133, None)
reports[-1].CovMatrix = ['2.28783e-05','1.81957e-05','-1.22854e-07','4.47877e-09','0','0','0','0','0','1.81957e-05','0.0118825','-1.13573e-07','1.71533e-07','0','0','0','0','0','-1.22854e-07','-1.13573e-07','2.35479e-09','3.93052e-11','0','0','0','0','0','4.47877e-09','1.71533e-07','3.93052e-11','8.22801e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 58630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0379303, 0.00401196, 0), \
                           ValErr(-0.177335, 0.0924786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30864e-05, 4.11394e-05, 0), \
                           -72294, 58630, 58630, -nan)
reports[-1].sigmaresid = ValErr(0.830371, 0.00242492, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0421671, None, 0.000415166, None, -0.0387887, None, 0.000669532, None, -0.0387887, None, 0.000669532, None, -0.0362913, None, 0.0006362, None, -0.0362913, None, 0.0006362, None, 0.830399, None, 0.00773133, None, 0.830399, None, 0.00773133, None)
reports[-1].CovMatrix = ['1.60958e-05','2.27356e-05','-8.54113e-08','3.31111e-09','0','0','0','0','0','2.27356e-05','0.00855228','-1.61191e-07','1.24725e-07','0','0','0','0','0','-8.54113e-08','-1.61191e-07','1.69245e-09','2.80948e-11','0','0','0','0','0','3.31111e-09','1.24725e-07','2.80948e-11','5.88024e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 62593
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0244735, 0.00390711, 0), \
                           ValErr(-0.233344, 0.0923577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.60009e-06, 4.10668e-05, 0), \
                           -79618, 62593, 62593, -nan)
reports[-1].sigmaresid = ValErr(0.863343, 0.00244009, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0284482, None, -0.000660519, None, -0.0247607, None, -0.000382565, None, -0.0247607, None, -0.000382565, None, -0.0197335, None, -0.000436174, None, -0.0197335, None, -0.000436174, None, 0.863387, None, 0.00802155, None, 0.863387, None, 0.00802155, None)
reports[-1].CovMatrix = ['1.52655e-05','-2.63415e-06','-7.5248e-08','3.11888e-09','0','0','0','0','0','-2.63415e-06','0.00852995','6.49989e-08','1.25308e-07','0','0','0','0','0','-7.5248e-08','6.49989e-08','1.68648e-09','3.40384e-11','0','0','0','0','0','3.11888e-09','1.25308e-07','3.40384e-11','5.95404e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 64266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0525738, 0.00381666, 0), \
                           ValErr(0.214134, 0.0910058, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000181155, 4.00012e-05, 0), \
                           -82116.8, 64266, 64266, -nan)
reports[-1].sigmaresid = ValErr(0.868339, 0.00242115, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0382752, None, 0.000759103, None, -0.0447941, None, 0.000888108, None, -0.0447941, None, 0.000888108, None, -0.0416929, None, 0.000923305, None, -0.0416929, None, 0.000923305, None, 0.868512, None, 0.00780301, None, 0.868512, None, 0.00780301, None)
reports[-1].CovMatrix = ['1.45669e-05','-9.4621e-06','-6.72262e-08','-7.03832e-09','0','0','0','0','0','-9.4621e-06','0.00828206','4.04507e-08','5.52004e-08','0','0','0','0','0','-6.72262e-08','4.04507e-08','1.60009e-09','1.51999e-10','0','0','0','0','0','-7.03832e-09','5.52004e-08','1.51999e-10','5.86195e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 154624
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00873602, 0.00112982, 0), \
                           ValErr(-0.0402853, 0.0129246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.91097e-05, 2.58407e-05, 0), \
                           -93422.4, 154624, 154624, -nan)
reports[-1].sigmaresid = ValErr(0.442751, 0.00079617, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00807969, None, 0.00072113, None, -0.00898919, None, 0.000715312, None, -0.00898919, None, 0.000715312, None, -0.00929768, None, 0.000746709, None, -0.00929768, None, 0.000746709, None, 0.442775, None, 0.00816676, None, 0.442775, None, 0.00816676, None)
reports[-1].CovMatrix = ['1.27648e-06','-1.99019e-08','-2.41119e-09','3.13935e-10','0','0','0','0','0','-1.99019e-08','0.000167045','1.42417e-09','3.92085e-09','0','0','0','0','0','-2.41119e-09','1.42417e-09','6.67742e-10','7.21924e-12','0','0','0','0','0','3.13935e-10','3.92085e-09','7.21924e-12','6.33887e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 102171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.025798, 0.00143014, 0), \
                           ValErr(-0.0761173, 0.0143202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.04497e-05, 3.53482e-05, 0), \
                           -59948.1, 102171, 102171, -nan)
reports[-1].sigmaresid = ValErr(0.435093, 0.000962506, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0253422, None, 0.000330316, None, 0.0251387, None, 0.00023757, None, 0.0251387, None, 0.00023757, None, 0.0240267, None, 0.000249453, None, 0.0240267, None, 0.000249453, None, 0.43516, None, 0.00828672, None, 0.43516, None, 0.00828672, None)
reports[-1].CovMatrix = ['2.04531e-06','2.87379e-07','-1.54962e-08','3.80578e-10','0','0','0','0','0','2.87379e-07','0.000205068','-3.63068e-09','5.18864e-09','0','0','0','0','0','-1.54962e-08','-3.63068e-09','1.2495e-09','9.21074e-12','0','0','0','0','0','3.80578e-10','5.18864e-09','9.21074e-12','9.26418e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 159261
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0532205, 0.00111469, 0), \
                           ValErr(0.0119707, 0.0128419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.35224e-05, 2.54334e-05, 0), \
                           -96267, 159261, 159261, -nan)
reports[-1].sigmaresid = ValErr(0.44287, 0.000784706, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0543024, None, 0.000736243, None, 0.0530817, None, 0.000746941, None, 0.0530817, None, 0.000746941, None, 0.0530563, None, 0.000772594, None, 0.0530563, None, 0.000772594, None, 0.442874, None, 0.00806174, None, 0.442874, None, 0.00806174, None)
reports[-1].CovMatrix = ['1.24254e-06','-1.01214e-09','-2.6693e-09','3.02062e-10','0','0','0','0','0','-1.01214e-09','0.000164914','1.83527e-09','3.84401e-09','0','0','0','0','0','-2.6693e-09','1.83527e-09','6.4686e-10','6.93377e-12','0','0','0','0','0','3.02062e-10','3.84401e-09','6.93377e-12','6.15764e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 153296
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0596678, 0.00113621, 0), \
                           ValErr(0.036591, 0.0131079, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.99142e-05, 2.59117e-05, 0), \
                           -92616.6, 153296, 153296, -nan)
reports[-1].sigmaresid = ValErr(0.442741, 0.000799594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0611775, None, -0.000221398, None, 0.0601532, None, -0.000242468, None, 0.0601532, None, -0.000242468, None, 0.061092, None, -0.000274734, None, 0.061092, None, -0.000274734, None, 0.442773, None, 0.00796131, None, 0.442773, None, 0.00796131, None)
reports[-1].CovMatrix = ['1.29098e-06','-3.49309e-07','-2.79543e-09','3.05412e-10','0','0','0','0','0','-3.49309e-07','0.000171817','4.19809e-09','3.93312e-09','0','0','0','0','0','-2.79543e-09','4.19809e-09','6.71417e-10','7.24584e-12','0','0','0','0','0','3.05412e-10','3.93312e-09','7.24584e-12','6.3935e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 96897
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0596297, 0.00143927, 0), \
                           ValErr(0.00762397, 0.0171187, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.8951e-05, 3.32908e-05, 0), \
                           -57536.2, 96897, 96897, -nan)
reports[-1].sigmaresid = ValErr(0.438169, 0.00099534, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0591484, None, -0.000319226, None, 0.0598489, None, -0.000419827, None, 0.0598489, None, -0.000419827, None, 0.0622011, None, -0.000286627, None, 0.0622011, None, -0.000286627, None, 0.43817, None, 0.00859507, None, 0.43817, None, 0.00859507, None)
reports[-1].CovMatrix = ['2.07149e-06','-3.34302e-06','-7.42586e-09','3.92611e-10','0','0','0','0','0','-3.34302e-06','0.00029305','-1.40078e-08','5.43471e-09','0','0','0','0','0','-7.42586e-09','-1.40078e-08','1.10828e-09','1.03251e-11','0','0','0','0','0','3.92611e-10','5.43471e-09','1.03251e-11','9.90702e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 155955
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0346011, 0.00113203, 0), \
                           ValErr(0.00161604, 0.0130938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.36236e-05, 2.58253e-05, 0), \
                           -95288.9, 155955, 155955, -nan)
reports[-1].sigmaresid = ValErr(0.445777, 0.000798184, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0362259, None, 0.000303727, None, 0.0348114, None, 0.000384951, None, 0.0348114, None, 0.000384951, None, 0.0351425, None, 0.000440126, None, 0.0351425, None, 0.000440126, None, 0.445786, None, 0.00806969, None, 0.445786, None, 0.00806969, None)
reports[-1].CovMatrix = ['1.28149e-06','-1.32617e-07','-2.19001e-09','3.16216e-10','0','0','0','0','0','-1.32617e-07','0.000171448','8.55924e-11','3.95234e-09','0','0','0','0','0','-2.19001e-09','8.55924e-11','6.66944e-10','7.29898e-12','0','0','0','0','0','3.16216e-10','3.95234e-09','7.29898e-12','6.37098e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 117021
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00905166, 0.00129393, 0), \
                           ValErr(-0.00251494, 0.013046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.09667e-05, 2.95684e-05, 0), \
                           -70332, 117021, 117021, -nan)
reports[-1].sigmaresid = ValErr(0.44135, 0.000912296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0103505, None, -7.21923e-05, None, 0.00922221, None, -6.94154e-05, None, 0.00922221, None, -6.94154e-05, None, 0.00938688, None, -9.07821e-05, None, 0.00938688, None, -9.07821e-05, None, 0.441355, None, 0.00805779, None, 0.441355, None, 0.00805779, None)
reports[-1].CovMatrix = ['1.67427e-06','6.98055e-08','-2.90767e-09','4.15607e-10','0','0','0','0','0','6.98055e-08','0.000170199','-5.9443e-10','4.51682e-09','0','0','0','0','0','-2.90767e-09','-5.9443e-10','8.74288e-10','9.44079e-12','0','0','0','0','0','4.15607e-10','4.51682e-09','9.44079e-12','8.32283e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 160071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00970324, 0.00110785, 0), \
                           ValErr(0.00466039, 0.0128845, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.70197e-05, 2.52272e-05, 0), \
                           -96156.4, 160071, 160071, -nan)
reports[-1].sigmaresid = ValErr(0.441213, 0.000779788, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00878297, None, -2.7091e-05, None, -0.00997241, None, 4.61326e-06, None, -0.00997241, None, 4.61326e-06, None, -0.0113152, None, -1.51795e-05, None, -0.0113152, None, -1.51795e-05, None, 0.441223, None, 0.00800405, None, 0.441223, None, 0.00800405, None)
reports[-1].CovMatrix = ['1.22733e-06','-2.50319e-07','-2.62149e-09','2.91967e-10','0','0','0','0','0','-2.50319e-07','0.00016601','-1.21545e-09','3.71778e-09','0','0','0','0','0','-2.62149e-09','-1.21545e-09','6.3641e-10','6.74723e-12','0','0','0','0','0','2.91967e-10','3.71778e-09','6.74723e-12','6.0807e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 154948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0206289, 0.0011306, 0), \
                           ValErr(-0.0127041, 0.0132208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.80032e-05, 2.59376e-05, 0), \
                           -93787.5, 154948, 154948, -nan)
reports[-1].sigmaresid = ValErr(0.443235, 0.000796207, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0207211, None, -0.00041601, None, -0.0210251, None, -0.000457051, None, -0.0210251, None, -0.000457051, None, -0.0199347, None, -0.000490723, None, -0.0199347, None, -0.000490723, None, 0.443257, None, 0.00832047, None, 0.443257, None, 0.00832047, None)
reports[-1].CovMatrix = ['1.27827e-06','-3.99563e-07','-2.5249e-09','3.04387e-10','0','0','0','0','0','-3.99563e-07','0.00017479','9.92726e-10','3.90236e-09','0','0','0','0','0','-2.5249e-09','9.92726e-10','6.72759e-10','7.21328e-12','0','0','0','0','0','3.04387e-10','3.90236e-09','7.21328e-12','6.33946e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 162703
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00111848, 0.00114007, 0), \
                           ValErr(-0.0631593, 0.013202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.92993e-05, 2.64809e-05, 0), \
                           -103686, 162703, 162703, -nan)
reports[-1].sigmaresid = ValErr(0.457644, 0.000802259, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000388477, None, 4.16056e-05, None, -0.00135344, None, -2.23214e-05, None, -0.00135344, None, -2.23214e-05, None, -0.000726003, None, -3.92563e-05, None, -0.000726003, None, -3.92563e-05, None, 0.457685, None, 0.00762739, None, 0.457685, None, 0.00762739, None)
reports[-1].CovMatrix = ['1.29977e-06','1.48723e-07','-2.94774e-09','3.26421e-10','0','0','0','0','0','1.48723e-07','0.000174292','1.67335e-09','4.19134e-09','0','0','0','0','0','-2.94774e-09','1.67335e-09','7.01238e-10','7.54571e-12','0','0','0','0','0','3.26421e-10','4.19134e-09','7.54571e-12','6.4362e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 158598
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0419628, 0.00116116, 0), \
                           ValErr(-0.0627154, 0.0133247, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.14832e-05, 2.73371e-05, 0), \
                           -102464, 158598, 158598, -nan)
reports[-1].sigmaresid = ValErr(0.461682, 0.000819745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0410926, None, 6.69179e-05, None, 0.0418692, None, 3.13511e-06, None, 0.0418692, None, 3.13511e-06, None, 0.0416178, None, -3.54636e-05, None, 0.0416178, None, -3.54636e-05, None, 0.46173, None, 0.00772074, None, 0.46173, None, 0.00772074, None)
reports[-1].CovMatrix = ['1.34829e-06','3.03271e-07','-1.67373e-09','3.62039e-10','0','0','0','0','0','3.03271e-07','0.000177548','7.60954e-09','4.45753e-09','0','0','0','0','0','-1.67373e-09','7.60954e-09','7.47317e-10','8.53376e-12','0','0','0','0','0','3.62039e-10','4.45753e-09','8.53376e-12','6.71982e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 162305
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0514498, 0.00114107, 0), \
                           ValErr(0.0360389, 0.0132273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.25266e-05, 2.64041e-05, 0), \
                           -103119, 162305, 162305, -nan)
reports[-1].sigmaresid = ValErr(0.456758, 0.000801687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0527452, None, 0.000745269, None, 0.051906, None, 0.000864326, None, 0.051906, None, 0.000864326, None, 0.0537368, None, 0.000939872, None, 0.0537368, None, 0.000939872, None, 0.456786, None, 0.00761229, None, 0.456786, None, 0.00761229, None)
reports[-1].CovMatrix = ['1.30204e-06','-3.05857e-08','-3.40518e-09','3.17847e-10','0','0','0','0','0','-3.05857e-08','0.000174962','1.53615e-09','4.13561e-09','0','0','0','0','0','-3.40518e-09','1.53615e-09','6.97179e-10','7.44333e-12','0','0','0','0','0','3.17847e-10','4.13561e-09','7.44333e-12','6.42703e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 159243
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0651654, 0.00116061, 0), \
                           ValErr(0.0581496, 0.0134453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.94422e-05, 2.68739e-05, 0), \
                           -101871, 159243, 159243, -nan)
reports[-1].sigmaresid = ValErr(0.458764, 0.000812912, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0647363, None, 0.000934022, None, 0.0652379, None, 0.00105713, None, 0.0652379, None, 0.00105713, None, 0.0662691, None, 0.00110768, None, 0.0662691, None, 0.00110768, None, 0.458791, None, 0.00755936, None, 0.458791, None, 0.00755936, None)
reports[-1].CovMatrix = ['1.34703e-06','1.40273e-07','-4.27259e-09','3.24718e-10','0','0','0','0','0','1.40273e-07','0.000180776','-1.517e-09','4.28414e-09','0','0','0','0','0','-4.27259e-09','-1.517e-09','7.22207e-10','7.45759e-12','0','0','0','0','0','3.24718e-10','4.28414e-09','7.45759e-12','6.60826e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 158323
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0477524, 0.00115954, 0), \
                           ValErr(-0.00214591, 0.0134396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.04473e-05, 2.67978e-05, 0), \
                           -101364, 158323, 158323, -nan)
reports[-1].sigmaresid = ValErr(0.459001, 0.000815692, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0471594, None, 0.00036234, None, 0.047799, None, 0.000333506, None, 0.047799, None, 0.000333506, None, 0.0470142, None, 0.000349317, None, 0.0470142, None, 0.000349317, None, 0.459002, None, 0.0077283, None, 0.459002, None, 0.0077283, None)
reports[-1].CovMatrix = ['1.34454e-06','9.41541e-08','-3.14585e-09','3.36565e-10','0','0','0','0','0','9.41541e-08','0.000180622','5.27653e-10','4.31202e-09','0','0','0','0','0','-3.14585e-09','5.27653e-10','7.18121e-10','7.76762e-12','0','0','0','0','0','3.36565e-10','4.31202e-09','7.76762e-12','6.65353e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 157046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.017949, 0.00116994, 0), \
                           ValErr(0.0618298, 0.0135395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000118027, 2.70603e-05, 0), \
                           -101273, 157046, 157046, -nan)
reports[-1].sigmaresid = ValErr(0.461128, 0.000822799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0179335, None, -2.64524e-06, None, 0.0183471, None, 0.000167319, None, 0.0183471, None, 0.000167319, None, 0.0181956, None, 0.000230493, None, 0.0181956, None, 0.000230493, None, 0.461187, None, 0.00780712, None, 0.461187, None, 0.00780712, None)
reports[-1].CovMatrix = ['1.36876e-06','3.59151e-07','-3.21169e-09','3.49312e-10','0','0','0','0','0','3.59151e-07','0.000183319','-1.34861e-09','4.44687e-09','0','0','0','0','0','-3.21169e-09','-1.34861e-09','7.32259e-10','7.84983e-12','0','0','0','0','0','3.49312e-10','4.44687e-09','7.84983e-12','6.76998e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 161052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00561976, 0.00114851, 0), \
                           ValErr(-0.0168317, 0.0132719, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.54316e-05, 2.64892e-05, 0), \
                           -102671, 161052, 161052, -nan)
reports[-1].sigmaresid = ValErr(0.457748, 0.000806545, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00361897, None, -0.000106913, None, -0.00553299, None, -0.000101547, None, -0.00553299, None, -0.000101547, None, -0.00347308, None, -0.000108782, None, -0.00347308, None, -0.000108782, None, 0.457751, None, 0.00750786, None, 0.457751, None, 0.00750786, None)
reports[-1].CovMatrix = ['1.31908e-06','8.54695e-08','-3.55442e-09','3.23057e-10','0','0','0','0','0','8.54695e-08','0.000176144','8.93325e-10','4.20749e-09','0','0','0','0','0','-3.55442e-09','8.93325e-10','7.01677e-10','7.42302e-12','0','0','0','0','0','3.23057e-10','4.20749e-09','7.42302e-12','6.50514e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 164445
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0234769, 0.00113741, 0), \
                           ValErr(0.0162723, 0.0131586, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00014734, 2.63689e-05, 0), \
                           -105155, 164445, 164445, -nan)
reports[-1].sigmaresid = ValErr(0.458642, 0.00079974, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0237635, None, -0.000119001, None, -0.0241505, None, -9.44648e-05, None, -0.0241505, None, -9.44648e-05, None, -0.024787, None, -0.000126659, None, -0.024787, None, -0.000126659, None, 0.458688, None, 0.00760813, None, 0.458688, None, 0.00760813, None)
reports[-1].CovMatrix = ['1.2937e-06','3.89224e-09','-3.17925e-09','3.19388e-10','0','0','0','0','0','3.89224e-09','0.000173147','-1.11428e-09','4.09314e-09','0','0','0','0','0','-3.17925e-09','-1.11428e-09','6.9532e-10','7.36615e-12','0','0','0','0','0','3.19388e-10','4.09314e-09','7.36615e-12','6.39583e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 141125
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0138452, 0.00122562, 0), \
                           ValErr(0.0043975, 0.0141334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000211477, 2.83466e-05, 0), \
                           -90083.8, 141125, 141125, -nan)
reports[-1].sigmaresid = ValErr(0.458125, 0.000862318, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0155543, None, -8.85948e-05, None, -0.0147469, None, -0.000205888, None, -0.0147469, None, -0.000205888, None, -0.0143865, None, -0.00025834, None, -0.0143865, None, -0.00025834, None, 0.458216, None, 0.00804727, None, 0.458216, None, 0.00804727, None)
reports[-1].CovMatrix = ['1.50215e-06','3.50851e-07','-3.39264e-09','3.82103e-10','0','0','0','0','0','3.50851e-07','0.000199754','1.88438e-09','4.87324e-09','0','0','0','0','0','-3.39264e-09','1.88438e-09','8.03531e-10','8.68735e-12','0','0','0','0','0','3.82103e-10','4.87324e-09','8.68735e-12','7.43592e-07','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 71560
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0452525, 0.00374183, 0), \
                           ValErr(-0.166133, 0.0913337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000149333, 4.05648e-05, 0), \
                           -95529.5, 71560, 71560, -nan)
reports[-1].sigmaresid = ValErr(0.919447, 0.00243039, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.039379, None, -0.000146447, None, 0.0399894, None, -0.000135289, None, 0.0399894, None, -0.000135289, None, 0.0366973, None, -0.000182896, None, 0.0366973, None, -0.000182896, None, 0.919556, None, 0.00830318, None, 0.919556, None, 0.00830318, None)
reports[-1].CovMatrix = ['1.40013e-05','8.57714e-06','-5.98766e-08','3.51072e-09','0','0','0','0','0','8.57714e-06','0.00834184','1.79515e-10','1.28464e-07','0','0','0','0','0','-5.98766e-08','1.79515e-10','1.6455e-09','3.66105e-11','0','0','0','0','0','3.51072e-09','1.28464e-07','3.66105e-11','5.90682e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 43406
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0316177, 0.00524607, 0), \
                           ValErr(0.0373306, 0.126275, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126168, 7.78029e-05, 0), \
                           -64965.6, 43406, 43406, -nan)
reports[-1].sigmaresid = ValErr(1.08086, 0.0036684, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0301048, None, -0.00127452, None, 0.0329183, None, -0.00125157, None, 0.0329183, None, -0.00125157, None, 0.0315374, None, -0.0013089, None, 0.0315374, None, -0.0013089, None, 1.0809, None, 0.00900549, None, 1.0809, None, 0.00900549, None)
reports[-1].CovMatrix = ['2.75213e-05','-2.04109e-05','5.85597e-08','1.28455e-08','0','0','0','0','0','-2.04109e-05','0.0159455','5.04228e-07','2.95098e-07','0','0','0','0','0','5.85597e-08','5.04228e-07','6.0533e-09','2.09565e-10','0','0','0','0','0','1.28455e-08','2.95098e-07','2.09565e-10','1.34572e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 55191
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0312749, 0.00505849, 0), \
                           ValErr(0.14247, 0.100001, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000158179, 5.27412e-05, 0), \
                           -67574.6, 55191, 55191, -nan)
reports[-1].sigmaresid = ValErr(0.823197, 0.00247411, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0411581, None, 9.88653e-05, None, 0.042058, None, 6.85692e-06, None, 0.042058, None, 6.85692e-06, None, 0.0426134, None, -4.56567e-05, None, 0.0426134, None, -4.56567e-05, None, 0.823279, None, 0.0078104, None, 0.823279, None, 0.0078104, None)
reports[-1].CovMatrix = ['2.55883e-05','1.51902e-05','-1.92632e-07','-2.72416e-08','0','0','0','0','0','1.51902e-05','0.0100002','-5.17137e-08','2.36043e-07','0','0','0','0','0','-1.92632e-07','-5.17137e-08','2.78164e-09','1.56646e-11','0','0','0','0','0','-2.72416e-08','2.36043e-07','1.56646e-11','6.1212e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 59701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.058387, 0.00449744, 0), \
                           ValErr(-0.0686648, 0.0985849, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000100227, 4.741e-05, 0), \
                           -75850.3, 59701, 59701, -nan)
reports[-1].sigmaresid = ValErr(0.862056, 0.00248547, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0640618, None, 0.000110325, None, 0.064265, None, 0.00029601, None, 0.064265, None, 0.00029601, None, 0.0685685, None, 0.000307329, None, 0.0685685, None, 0.000307329, None, 0.862091, None, 0.00800199, None, 0.862091, None, 0.00800199, None)
reports[-1].CovMatrix = ['2.0227e-05','-1.39947e-05','-1.32858e-07','-5.38516e-08','0','0','0','0','0','-1.39947e-05','0.00971898','1.26411e-07','-3.80707e-08','0','0','0','0','0','-1.32858e-07','1.26411e-07','2.24771e-09','2.09989e-11','0','0','0','0','0','-5.38516e-08','-3.80707e-08','2.09989e-11','6.17754e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 68820
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0603378, 0.00385748, 0), \
                           ValErr(-0.164278, 0.0919132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000114725, 4.14997e-05, 0), \
                           -90760.4, 68820, 68820, -nan)
reports[-1].sigmaresid = ValErr(0.904721, 0.00243734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0641635, None, 0.000319563, None, 0.0651635, None, 0.000308308, None, 0.0651635, None, 0.000308308, None, 0.0655388, None, 0.000260014, None, 0.0655388, None, 0.000260014, None, 0.90479, None, 0.00815116, None, 0.90479, None, 0.00815116, None)
reports[-1].CovMatrix = ['1.48802e-05','5.04014e-06','-7.18154e-08','2.94987e-09','0','0','0','0','0','5.04014e-06','0.00844805','-4.44858e-08','-4.54121e-08','0','0','0','0','0','-7.18154e-08','-4.44858e-08','1.72223e-09','-1.65965e-10','0','0','0','0','0','2.94987e-09','-4.54121e-08','-1.65965e-10','5.94063e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 69361
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0370398, 0.00381536, 0), \
                           ValErr(-0.431927, 0.0918394, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.72532e-05, 4.09872e-05, 0), \
                           -91774.3, 69361, 69361, -nan)
reports[-1].sigmaresid = ValErr(0.90865, 0.00243964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0391422, None, 0.000718488, None, 0.0383243, None, 0.000958422, None, 0.0383243, None, 0.000958422, None, 0.0410503, None, 0.00104829, None, 0.0410503, None, 0.00104829, None, 0.908798, None, 0.00826714, None, 0.908798, None, 0.00826714, None)
reports[-1].CovMatrix = ['1.4557e-05','-6.41339e-06','-6.6744e-08','3.25569e-09','0','0','0','0','0','-6.41339e-06','0.00843447','6.72824e-08','1.26339e-07','0','0','0','0','0','-6.6744e-08','6.72824e-08','1.67995e-09','3.66528e-11','0','0','0','0','0','3.25569e-09','1.26339e-07','3.66528e-11','5.95184e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 64965
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.065024, 0.00397213, 0), \
                           ValErr(-0.331614, 0.0948153, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000172911, 4.19661e-05, 0), \
                           -85077.5, 64965, 64965, -nan)
reports[-1].sigmaresid = ValErr(0.896419, 0.00248689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0557225, None, 0.000605155, None, 0.0578601, None, 0.000674277, None, 0.0578601, None, 0.000674277, None, 0.0520523, None, 0.00068504, None, 0.0520523, None, 0.00068504, None, 0.896626, None, 0.007959, None, 0.896626, None, 0.007959, None)
reports[-1].CovMatrix = ['1.57778e-05','1.68269e-05','-7.73214e-08','3.59034e-09','0','0','0','0','0','1.68269e-05','0.00898993','-1.2917e-07','1.33664e-07','0','0','0','0','0','-7.73214e-08','-1.2917e-07','1.76116e-09','3.33491e-11','0','0','0','0','0','3.59034e-09','1.33664e-07','3.33491e-11','6.18462e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 71377
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0979599, 0.00376554, 0), \
                           ValErr(0.153002, 0.0900986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.28721e-05, 4.05973e-05, 0), \
                           -93699.8, 71377, 71377, -nan)
reports[-1].sigmaresid = ValErr(0.899252, 0.00237744, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.087106, None, 0.000232567, None, 0.0943203, None, 0.000274857, None, 0.0943203, None, 0.000274857, None, 0.097006, None, 0.000274347, None, 0.097006, None, 0.000274347, None, 0.899302, None, 0.00808241, None, 0.899302, None, 0.00808241, None)
reports[-1].CovMatrix = ['1.41793e-05','-1.30193e-05','-6.87535e-08','1.46987e-08','0','0','0','0','0','-1.30193e-05','0.00811776','1.19854e-07','2.83872e-07','0','0','0','0','0','-6.87535e-08','1.19854e-07','1.64814e-09','-6.71213e-10','0','0','0','0','0','1.46987e-08','2.83872e-07','-6.71213e-10','5.65222e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 59705
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0621474, 0.0041653, 0), \
                           ValErr(0.178765, 0.0968332, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.901e-05, 4.25307e-05, 0), \
                           -75976, 59705, 59705, -nan)
reports[-1].sigmaresid = ValErr(0.863803, 0.00245135, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0654297, None, -0.000330574, None, 0.0646952, None, -0.000347343, None, 0.0646952, None, -0.000347343, None, 0.0652168, None, -0.000431913, None, 0.0652168, None, -0.000431913, None, 0.863834, None, 0.00799971, None, 0.863834, None, 0.00799971, None)
reports[-1].CovMatrix = ['1.73498e-05','1.17794e-05','-9.65392e-08','-1.62096e-07','0','0','0','0','0','1.17794e-05','0.00937667','-1.01308e-07','5.64307e-06','0','0','0','0','0','-9.65392e-08','-1.01308e-07','1.80886e-09','-1.96053e-09','0','0','0','0','0','-1.62096e-07','5.64307e-06','-1.96053e-09','6.00911e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 72172
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0649957, 0.0037385, 0), \
                           ValErr(0.195232, 0.0908182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.77528e-05, 4.09262e-05, 0), \
                           -95705.6, 72172, 72172, -nan)
reports[-1].sigmaresid = ValErr(0.911319, 0.00239867, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0617209, None, -0.000331633, None, 0.0627696, None, -0.000285612, None, 0.0627696, None, -0.000285612, None, 0.0682949, None, -0.000311319, None, 0.0682949, None, -0.000311319, None, 0.911361, None, 0.00809382, None, 0.911361, None, 0.00809382, None)
reports[-1].CovMatrix = ['1.39764e-05','-1.86145e-08','-6.43088e-08','3.21939e-09','0','0','0','0','0','-1.86145e-08','0.00824795','1.01634e-08','1.22827e-07','0','0','0','0','0','-6.43088e-08','1.01634e-08','1.67495e-09','3.53603e-11','0','0','0','0','0','3.21939e-09','1.22827e-07','3.53603e-11','5.75363e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 61014
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0398279, 0.00394439, 0), \
                           ValErr(0.0883052, 0.0780752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.21958e-05, 4.2932e-05, 0), \
                           -79654.6, 61014, 61014, -nan)
reports[-1].sigmaresid = ValErr(0.892774, 0.00244909, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0429369, None, -0.000914716, None, 0.0403732, None, -0.000775086, None, 0.0403732, None, -0.000775086, None, 0.0400953, None, -0.000832491, None, 0.0400953, None, -0.000832491, None, 0.892777, None, 0.00829085, None, 0.892777, None, 0.00829085, None)
reports[-1].CovMatrix = ['1.55582e-05','-4.58232e-05','-7.74407e-08','5.55559e-07','0','0','0','0','0','-4.58232e-05','0.00609574','-6.90852e-08','3.86107e-05','0','0','0','0','0','-7.74407e-08','-6.90852e-08','1.84316e-09','5.75374e-10','0','0','0','0','0','5.55559e-07','3.86107e-05','5.75374e-10','5.99804e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 72764
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0437376, 0.00370196, 0), \
                           ValErr(0.127569, 0.0888851, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.96331e-05, 4.02036e-05, 0), \
                           -96073.6, 72764, 72764, -nan)
reports[-1].sigmaresid = ValErr(0.906115, 0.00235517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0444983, None, 0.000766968, None, 0.0452722, None, 0.000922683, None, 0.0452722, None, 0.000922683, None, 0.0426737, None, 0.00093249, None, 0.0426737, None, 0.00093249, None, 0.90613, None, 0.00821775, None, 0.90613, None, 0.00821775, None)
reports[-1].CovMatrix = ['1.37045e-05','-4.58107e-07','-6.33018e-08','-4.44462e-08','0','0','0','0','0','-4.58107e-07','0.00790056','3.81489e-08','1.24865e-06','0','0','0','0','0','-6.33018e-08','3.81489e-08','1.61633e-09','-6.67745e-10','0','0','0','0','0','-4.44462e-08','1.24865e-06','-6.67745e-10','5.54684e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 59525
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0458429, 0.00411176, 0), \
                           ValErr(-0.12571, 0.0956357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0002221, 4.15515e-05, 0), \
                           -77825.8, 59525, 59525, -nan)
reports[-1].sigmaresid = ValErr(0.894505, 0.00242798, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0290869, None, -0.000413608, None, 0.0356134, None, -0.000263964, None, 0.0356134, None, -0.000263964, None, 0.0375668, None, -0.00032607, None, 0.0375668, None, -0.00032607, None, 0.894724, None, 0.00793244, None, 0.894724, None, 0.00793244, None)
reports[-1].CovMatrix = ['1.69065e-05','-1.00232e-05','-7.77417e-08','3.40877e-07','0','0','0','0','0','-1.00232e-05','0.00914618','5.02797e-08','-1.80567e-05','0','0','0','0','0','-7.77417e-08','5.02797e-08','1.72652e-09','-2.37249e-09','0','0','0','0','0','3.40877e-07','-1.80567e-05','-2.37249e-09','5.89508e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 57179
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0361958, 0.00427403, 0), \
                           ValErr(-0.146964, 0.100397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000151482, 4.35383e-05, 0), \
                           -73792.4, 57179, 57179, -nan)
reports[-1].sigmaresid = ValErr(0.879513, 0.00260015, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0189918, None, 0.000235292, None, 0.0287092, None, 0.000265501, None, 0.0287092, None, 0.000265501, None, 0.0254044, None, 0.000275222, None, 0.0254044, None, 0.000275222, None, 0.879621, None, 0.00783885, None, 0.879621, None, 0.00783885, None)
reports[-1].CovMatrix = ['1.82673e-05','3.21994e-06','-9.47345e-08','1.33607e-09','0','0','0','0','0','3.21994e-06','0.0100795','5.15417e-08','3.1356e-08','0','0','0','0','0','-9.47345e-08','5.15417e-08','1.89558e-09','-2.71797e-11','0','0','0','0','0','1.33607e-09','3.1356e-08','-2.71797e-11','6.76078e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 57443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0244648, 0.0042452, 0), \
                           ValErr(0.15623, 0.101544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.1615e-05, 4.21617e-05, 0), \
                           -75367.8, 57443, 57443, -nan)
reports[-1].sigmaresid = ValErr(0.898622, 0.00265066, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0200396, None, -0.000227554, None, 0.0217204, None, -0.00056214, None, 0.0217204, None, -0.00056214, None, 0.0191144, None, -0.000586773, None, 0.0191144, None, -0.000586773, None, 0.898657, None, 0.00856526, None, 0.898657, None, 0.00856526, None)
reports[-1].CovMatrix = ['1.80218e-05','-1.31987e-05','-8.37377e-08','9.709e-10','0','0','0','0','0','-1.31987e-05','0.0103111','5.91626e-08','-2.75172e-08','0','0','0','0','0','-8.37377e-08','5.91626e-08','1.77761e-09','-4.20211e-11','0','0','0','0','0','9.709e-10','-2.75172e-08','-4.20211e-11','7.02598e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 53715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0209251, 0.00444983, 0), \
                           ValErr(-0.062877, 0.103185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.10224e-05, 4.45072e-05, 0), \
                           -69407, 53715, 53715, -nan)
reports[-1].sigmaresid = ValErr(0.880908, 0.0026862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0156211, None, 0.000504232, None, 0.0200107, None, 0.000532112, None, 0.0200107, None, 0.000532112, None, 0.0230399, None, 0.000546875, None, 0.0230399, None, 0.000546875, None, 0.880912, None, 0.00797297, None, 0.880912, None, 0.00797297, None)
reports[-1].CovMatrix = ['1.9801e-05','4.02778e-05','-1.02251e-07','2.23985e-09','0','0','0','0','0','4.02778e-05','0.0106471','-2.43079e-07','4.81276e-08','0','0','0','0','0','-1.02251e-07','-2.43079e-07','1.98089e-09','-5.58121e-11','0','0','0','0','0','2.23985e-09','4.81276e-08','-5.58121e-11','7.21567e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 62114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0197081, 0.00413977, 0), \
                           ValErr(0.501759, 0.0989032, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.8815e-05, 4.45796e-05, 0), \
                           -80671, 62114, 62114, -nan)
reports[-1].sigmaresid = ValErr(0.886761, 0.00251592, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0260201, None, 0.000615689, None, 0.023812, None, 0.000813209, None, 0.023812, None, 0.000813209, None, 0.0254858, None, 0.000868341, None, 0.0254858, None, 0.000868341, None, 0.886968, None, 0.00819817, None, 0.886968, None, 0.00819817, None)
reports[-1].CovMatrix = ['1.71377e-05','-3.5148e-06','-9.40528e-08','3.24724e-09','0','0','0','0','0','-3.5148e-06','0.00978184','-2.67359e-07','1.27132e-07','0','0','0','0','0','-9.40528e-08','-2.67359e-07','1.98734e-09','3.21585e-11','0','0','0','0','0','3.24724e-09','1.27132e-07','3.21585e-11','6.32987e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 64210
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0224547, 0.00399163, 0), \
                           ValErr(-0.143251, 0.0943924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000115018, 4.1849e-05, 0), \
                           -83556.6, 64210, 64210, -nan)
reports[-1].sigmaresid = ValErr(0.88902, 0.00248082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0263665, None, 0.000163538, None, 0.0276132, None, -0.000244316, None, 0.0276132, None, -0.000244316, None, 0.0280336, None, -0.000347709, None, 0.0280336, None, -0.000347709, None, 0.889088, None, 0.00883483, None, 0.889088, None, 0.00883483, None)
reports[-1].CovMatrix = ['1.59331e-05','-5.1877e-06','-7.96445e-08','3.20134e-09','0','0','0','0','0','-5.1877e-06','0.00890992','1.68159e-08','1.29239e-07','0','0','0','0','0','-7.96445e-08','1.68159e-08','1.75134e-09','3.48621e-11','0','0','0','0','0','3.20134e-09','1.29239e-07','3.48621e-11','6.15449e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 75723
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0265033, 0.00367347, 0), \
                           ValErr(0.199694, 0.0890569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000162595, 3.99551e-05, 0), \
                           -101336, 75723, 75723, -nan)
reports[-1].sigmaresid = ValErr(0.922476, 0.00236352, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0356255, None, 0.000144465, None, 0.0327028, None, 0.000208052, None, 0.0327028, None, 0.000208052, None, 0.0324791, None, 0.000168039, None, 0.0324791, None, 0.000168039, None, 0.922603, None, 0.00780739, None, 0.922603, None, 0.00780739, None)
reports[-1].CovMatrix = ['1.34944e-05','-4.9589e-06','-6.07264e-08','-1.70194e-08','0','0','0','0','0','-4.9589e-06','0.00793114','5.71046e-08','6.8132e-07','0','0','0','0','0','-6.07264e-08','5.71046e-08','1.59641e-09','-5.97706e-10','0','0','0','0','0','-1.70194e-08','6.8132e-07','-5.97706e-10','5.58622e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 58414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0302308, 0.00501796, 0), \
                           ValErr(0.0176026, 0.101896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.81737e-05, 5.19607e-05, 0), \
                           -74482.8, 58414, 58414, -nan)
reports[-1].sigmaresid = ValErr(0.866015, 0.00252365, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0372826, None, 0.000238569, None, 0.0335219, None, 0.000235673, None, 0.0335219, None, 0.000235673, None, 0.0291039, None, 0.000184772, None, 0.0291039, None, 0.000184772, None, 0.86602, None, 0.00737381, None, 0.86602, None, 0.00737381, None)
reports[-1].CovMatrix = ['2.51799e-05','-4.95203e-05','-1.8349e-07','-9.5209e-08','0','0','0','0','0','-4.95203e-05','0.0103827','4.35813e-07','6.86716e-07','0','0','0','0','0','-1.8349e-07','4.35813e-07','2.69991e-09','7.38783e-11','0','0','0','0','0','-9.5209e-08','6.86716e-07','7.38783e-11','6.36882e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 67034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0306608, 0.00418344, 0), \
                           ValErr(-0.103296, 0.0936101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.4918e-05, 4.53384e-05, 0), \
                           -87277.6, 67034, 67034, -nan)
reports[-1].sigmaresid = ValErr(0.889631, 0.00242967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.034869, None, -0.000139466, None, 0.0336981, None, -0.00019126, None, 0.0336981, None, -0.00019126, None, 0.0314943, None, -0.000245155, None, 0.0314943, None, -0.000245155, None, 0.889648, None, 0.0076849, None, 0.889648, None, 0.0076849, None)
reports[-1].CovMatrix = ['1.75012e-05','3.17911e-05','-1.07969e-07','3.44828e-09','0','0','0','0','0','3.17911e-05','0.00876284','-3.32649e-07','1.28913e-07','0','0','0','0','0','-1.07969e-07','-3.32649e-07','2.05557e-09','2.76508e-11','0','0','0','0','0','3.44828e-09','1.28913e-07','2.76508e-11','5.9033e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 66023
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0507143, 0.00409018, 0), \
                           ValErr(0.0778104, 0.0947937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000204295, 4.36913e-05, 0), \
                           -85883.1, 66023, 66023, -nan)
reports[-1].sigmaresid = ValErr(0.888578, 0.0024453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0620236, None, 0.000306457, None, 0.0607466, None, 0.000428565, None, 0.0607466, None, 0.000428565, None, 0.0604927, None, 0.000399942, None, 0.0604927, None, 0.000399942, None, 0.888732, None, 0.00762258, None, 0.888732, None, 0.00762258, None)
reports[-1].CovMatrix = ['1.67296e-05','2.50255e-05','-9.52133e-08','3.43614e-09','0','0','0','0','0','2.50255e-05','0.00898585','-2.23384e-07','1.31069e-07','0','0','0','0','0','-9.52133e-08','-2.23384e-07','1.90893e-09','2.9597e-11','0','0','0','0','0','3.43614e-09','1.31069e-07','2.9597e-11','5.97951e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 77498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.076646, 0.00361307, 0), \
                           ValErr(0.0555819, 0.0553358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.26856e-07, 3.99618e-05, 0), \
                           -104659, 77498, 77498, -nan)
reports[-1].sigmaresid = ValErr(0.933824, 0.0023337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0764553, None, -0.000226143, None, 0.0766216, None, -0.000115697, None, 0.0766216, None, -0.000115697, None, 0.0716984, None, -0.000186915, None, 0.0716984, None, -0.000186915, None, 0.933825, None, 0.00785749, None, 0.933825, None, 0.00785749, None)
reports[-1].CovMatrix = ['1.30543e-05','-2.7243e-05','-5.50502e-08','1.80605e-07','0','0','0','0','0','-2.7243e-05','0.00306205','1.48166e-07','2.97635e-05','0','0','0','0','0','-5.50502e-08','1.48166e-07','1.59695e-09','-9.47865e-10','0','0','0','0','0','1.80605e-07','2.97635e-05','-9.47865e-10','5.44616e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 71894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0466684, 0.00379855, 0), \
                           ValErr(-0.118446, 0.0897741, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.70915e-05, 4.12022e-05, 0), \
                           -94390.2, 71894, 71894, -nan)
reports[-1].sigmaresid = ValErr(0.8994, 0.00236106, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0422219, None, 0.000532086, None, 0.045013, None, 0.000602805, None, 0.045013, None, 0.000602805, None, 0.0459169, None, 0.000581631, None, 0.0459169, None, 0.000581631, None, 0.899413, None, 0.00784918, None, 0.899413, None, 0.00784918, None)
reports[-1].CovMatrix = ['1.4429e-05','-4.52286e-06','-7.38641e-08','-6.32847e-09','0','0','0','0','0','-4.52286e-06','0.00805939','3.01118e-09','-7.30999e-07','0','0','0','0','0','-7.38641e-08','3.01118e-09','1.69762e-09','-7.69451e-10','0','0','0','0','0','-6.32847e-09','-7.30999e-07','-7.69451e-10','5.57459e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 76366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0610358, 0.00363228, 0), \
                           ValErr(-0.173374, 0.0880011, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.65486e-05, 3.99327e-05, 0), \
                           -101883, 76366, 76366, -nan)
reports[-1].sigmaresid = ValErr(0.918699, 0.00235076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0601929, None, 0.000629597, None, 0.0623965, None, 0.000606333, None, 0.0623965, None, 0.000606333, None, 0.063472, None, 0.000577435, None, 0.063472, None, 0.000577435, None, 0.918727, None, 0.00791476, None, 0.918727, None, 0.00791476, None)
reports[-1].CovMatrix = ['1.31935e-05','5.2534e-07','-5.84333e-08','3.14822e-09','0','0','0','0','0','5.2534e-07','0.00774419','1.17044e-08','1.17141e-07','0','0','0','0','0','-5.84333e-08','1.17044e-08','1.59462e-09','3.4668e-11','0','0','0','0','0','3.14822e-09','1.17141e-07','3.4668e-11','5.52607e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 66874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0838472, 0.00413489, 0), \
                           ValErr(0.0271643, 0.0938305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.88464e-05, 4.42716e-05, 0), \
                           -87992.8, 66874, 66874, -nan)
reports[-1].sigmaresid = ValErr(0.902005, 0.00245116, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0812451, None, 0.000668867, None, 0.0818903, None, 0.000839073, None, 0.0818903, None, 0.000839073, None, 0.0813836, None, 0.000829528, None, 0.0813836, None, 0.000829528, None, 0.902008, None, 0.00780842, None, 0.902008, None, 0.00780842, None)
reports[-1].CovMatrix = ['1.70974e-05','-6.96974e-06','-1.01016e-07','-8.84606e-08','0','0','0','0','0','-6.96974e-06','0.00880417','1.10371e-07','1.41766e-06','0','0','0','0','0','-1.01016e-07','1.10371e-07','1.95998e-09','-9.62289e-10','0','0','0','0','0','-8.84606e-08','1.41766e-06','-9.62289e-10','6.0082e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 69551
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0635343, 0.00383113, 0), \
                           ValErr(-0.00624783, 0.063142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.29146e-05, 4.12878e-05, 0), \
                           -92187.6, 69551, 69551, -nan)
reports[-1].sigmaresid = ValErr(0.910766, 0.0023777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0569171, None, 0.000403611, None, 0.0604629, None, 0.00045556, None, 0.0604629, None, 0.00045556, None, 0.0639123, None, 0.000466459, None, 0.0639123, None, 0.000466459, None, 0.910785, None, 0.00767658, None, 0.910785, None, 0.00767658, None)
reports[-1].CovMatrix = ['1.46776e-05','-2.57325e-05','-7.06812e-08','-3.08809e-07','0','0','0','0','0','-2.57325e-05','0.00398691','1.73253e-07','-3.69893e-05','0','0','0','0','0','-7.06812e-08','1.73253e-07','1.70468e-09','1.69633e-09','0','0','0','0','0','-3.08809e-07','-3.69893e-05','1.69633e-09','5.65346e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 67349
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0695105, 0.00406897, 0), \
                           ValErr(-0.298824, 0.094368, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000111699, 4.34356e-05, 0), \
                           -89214.2, 67349, 67349, -nan)
reports[-1].sigmaresid = ValErr(0.910025, 0.00247955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0598742, None, -4.18415e-05, None, 0.064244, None, -3.88187e-05, None, 0.064244, None, -3.88187e-05, None, 0.0726386, None, -4.66914e-05, None, 0.0726386, None, -4.66914e-05, None, 0.910137, None, 0.00787527, None, 0.910137, None, 0.00787527, None)
reports[-1].CovMatrix = ['1.65565e-05','1.28593e-06','-8.96506e-08','3.25516e-09','0','0','0','0','0','1.28593e-06','0.00890533','-1.24545e-09','1.31817e-07','0','0','0','0','0','-8.96506e-08','-1.24545e-09','1.88666e-09','3.46164e-11','0','0','0','0','0','3.25516e-09','1.31817e-07','3.46164e-11','6.14816e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 71443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0397292, 0.00380581, 0), \
                           ValErr(0.0355115, 0.0504535, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00013746, 4.13147e-05, 0), \
                           -95157.3, 71443, 71443, -nan)
reports[-1].sigmaresid = ValErr(0.916668, 0.002422, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0323574, None, -0.00102341, None, 0.0341763, None, -0.00106597, None, 0.0341763, None, -0.00106597, None, 0.0300017, None, -0.001178, None, 0.0300017, None, -0.001178, None, 0.916743, None, 0.00809838, None, 0.916743, None, 0.00809838, None)
reports[-1].CovMatrix = ['1.44842e-05','2.16033e-05','-6.8533e-08','-2.18689e-08','0','0','0','0','0','2.16033e-05','0.00254556','-2.24184e-07','1.77484e-06','0','0','0','0','0','-6.8533e-08','-2.24184e-07','1.70691e-09','4.76418e-11','0','0','0','0','0','-2.18689e-08','1.77484e-06','4.76418e-11','5.86609e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 78165
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0505532, 0.00358789, 0), \
                           ValErr(-0.0954665, 0.0583009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.54061e-05, 3.96208e-05, 0), \
                           -104427, 78165, 78165, -nan)
reports[-1].sigmaresid = ValErr(0.920393, 0.00228881, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0457743, None, -0.00173284, None, 0.0468185, None, -0.00201075, None, 0.0468185, None, -0.00201075, None, 0.0422495, None, -0.00216493, None, 0.0422495, None, -0.00216493, None, 0.920431, None, 0.0082852, None, 0.920431, None, 0.0082852, None)
reports[-1].CovMatrix = ['1.2873e-05','1.97295e-05','-6.17087e-08','2.16815e-07','0','0','0','0','0','1.97295e-05','0.00339899','2.67091e-07','-2.75903e-05','0','0','0','0','0','-6.17087e-08','2.67091e-07','1.5698e-09','9.43097e-10','0','0','0','0','0','2.16815e-07','-2.75903e-05','9.43097e-10','5.23865e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 58784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0370415, 0.00421692, 0), \
                           ValErr(-0.0197822, 0.0568932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.66125e-05, 4.21759e-05, 0), \
                           -75792.7, 58784, 58784, -nan)
reports[-1].sigmaresid = ValErr(0.878447, 0.00256127, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0302185, None, 0.000118923, None, 0.0331158, None, 0.00033986, None, 0.0331158, None, 0.00033986, None, 0.0326038, None, 0.000288796, None, 0.0326038, None, 0.000288796, None, 0.878475, None, 0.00775957, None, 0.878475, None, 0.00775957, None)
reports[-1].CovMatrix = ['1.77824e-05','-1.06078e-05','-9.11842e-08','-2.76195e-09','0','0','0','0','0','-1.06078e-05','0.00323684','2.06436e-07','-2.59997e-06','0','0','0','0','0','-9.11842e-08','2.06436e-07','1.77881e-09','1.53349e-11','0','0','0','0','0','-2.76195e-09','-2.59997e-06','1.53349e-11','6.56009e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 63380
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0356847, 0.00413087, 0), \
                           ValErr(-0.0569353, 0.0968789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.02136e-05, 4.24847e-05, 0), \
                           -83933.5, 63380, 63380, -nan)
reports[-1].sigmaresid = ValErr(0.909693, 0.00254986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0391332, None, 0.000191094, None, 0.0323701, None, -0.000104172, None, 0.0323701, None, -0.000104172, None, 0.0312403, None, -0.000104683, None, 0.0312403, None, -0.000104683, None, 0.909714, None, 0.008177, None, 0.909714, None, 0.008177, None)
reports[-1].CovMatrix = ['1.70641e-05','-1.62341e-06','-8.54416e-08','-2.95545e-09','0','0','0','0','0','-1.62341e-06','0.00938553','-2.34269e-08','-2.81843e-07','0','0','0','0','0','-8.54416e-08','-2.34269e-08','1.80495e-09','-4.93019e-10','0','0','0','0','0','-2.95545e-09','-2.81843e-07','-4.93019e-10','6.5018e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 57019
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.026689, 0.00431972, 0), \
                           ValErr(-0.0095221, 0.0570235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.39438e-05, 4.3033e-05, 0), \
                           -73436.4, 57019, 57019, -nan)
reports[-1].sigmaresid = ValErr(0.877209, 0.00259734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0239908, None, 0.00016544, None, 0.0248927, None, 0.000222772, None, 0.0248927, None, 0.000222772, None, 0.0306144, None, 0.000240564, None, 0.0306144, None, 0.000240564, None, 0.877214, None, 0.00748867, None, 0.877214, None, 0.00748867, None)
reports[-1].CovMatrix = ['1.866e-05','-1.02152e-05','-9.78216e-08','1.95812e-10','0','0','0','0','0','-1.02152e-05','0.00325168','1.04278e-07','2.37112e-06','0','0','0','0','0','-9.78216e-08','1.04278e-07','1.85184e-09','-1.37037e-11','0','0','0','0','0','1.95812e-10','2.37112e-06','-1.37037e-11','6.74619e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 68497
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.038264, 0.00391721, 0), \
                           ValErr(-0.276008, 0.0921582, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.651e-05, 4.17694e-05, 0), \
                           -89591.2, 68497, 68497, -nan)
reports[-1].sigmaresid = ValErr(0.894959, 0.00241798, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0378292, None, 3.09103e-05, None, 0.0396648, None, 0.000134689, None, 0.0396648, None, 0.000134689, None, 0.0397325, None, 7.85477e-05, None, 0.0397325, None, 7.85477e-05, None, 0.895022, None, 0.00784568, None, 0.895022, None, 0.00784568, None)
reports[-1].CovMatrix = ['1.53445e-05','-1.68404e-05','-7.97308e-08','2.86624e-09','0','0','0','0','0','-1.68404e-05','0.00849312','1.9248e-07','1.25523e-07','0','0','0','0','0','-7.97308e-08','1.9248e-07','1.74468e-09','3.62484e-11','0','0','0','0','0','2.86624e-09','1.25523e-07','3.62484e-11','5.84665e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 71933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00896382, 0.00381012, 0), \
                           ValErr(0.0778733, 0.0923578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.65348e-05, 4.13639e-05, 0), \
                           -96409.2, 71933, 71933, -nan)
reports[-1].sigmaresid = ValErr(0.924341, 0.00243699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0133384, None, 0.000454797, None, 0.0119799, None, 0.000368029, None, 0.0119799, None, 0.000368029, None, 0.0078, None, 0.000299151, None, 0.0078, None, 0.000299151, None, 0.924368, None, 0.00770349, None, 0.924368, None, 0.00770349, None)
reports[-1].CovMatrix = ['1.4517e-05','1.56189e-06','-6.7197e-08','3.32812e-09','0','0','0','0','0','1.56189e-06','0.00852997','-6.50945e-08','1.24711e-07','0','0','0','0','0','-6.7197e-08','-6.50945e-08','1.71097e-09','3.54253e-11','0','0','0','0','0','3.32812e-09','1.24711e-07','3.54253e-11','5.9389e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 72274
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0432101, 0.00375613, 0), \
                           ValErr(0.0205102, 0.0496909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000125462, 4.07194e-05, 0), \
                           -96546, 72274, 72274, -nan)
reports[-1].sigmaresid = ValErr(0.92025, 0.00242012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0350469, None, 0.000838021, None, 0.0384574, None, 0.000836542, None, 0.0384574, None, 0.000836542, None, 0.0432773, None, 0.000911776, None, 0.0432773, None, 0.000911776, None, 0.920315, None, 0.00800154, None, 0.920315, None, 0.00800154, None)
reports[-1].CovMatrix = ['1.41085e-05','9.868e-06','-6.29701e-08','5.33448e-09','0','0','0','0','0','9.868e-06','0.00246919','-9.89988e-08','8.13021e-07','0','0','0','0','0','-6.29701e-08','-9.89988e-08','1.65807e-09','-1.16495e-10','0','0','0','0','0','5.33448e-09','8.13021e-07','-1.16495e-10','5.85699e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 96724
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00656348, 0.00167226, 0), \
                           ValErr(-0.0525556, 0.0169456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000116911, 4.37183e-05, 0), \
                           -73945.8, 96724, 96724, -nan)
reports[-1].sigmaresid = ValErr(0.519736, 0.00118168, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00306188, None, 0.000775558, None, -0.00674842, None, 0.000770215, None, -0.00674842, None, 0.000770215, None, -0.00578504, None, 0.000825666, None, -0.00578504, None, 0.000825666, None, 0.519781, None, 0.00809922, None, 0.519781, None, 0.00809922, None)
reports[-1].CovMatrix = ['2.79645e-06','-1.29691e-07','-2.63948e-09','8.09644e-10','0','0','0','0','0','-1.29691e-07','0.000287154','9.7628e-10','8.5153e-09','0','0','0','0','0','-2.63948e-09','9.7628e-10','1.91129e-09','2.13092e-11','0','0','0','0','0','8.09644e-10','8.5153e-09','2.13092e-11','1.39637e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 114806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0309233, 0.00153296, 0), \
                           ValErr(-0.0939183, 0.017459, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.80729e-05, 3.99644e-05, 0), \
                           -87524.9, 114806, 114806, -nan)
reports[-1].sigmaresid = ValErr(0.51863, 0.00108233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0320065, None, -1.73832e-05, None, 0.0308449, None, -2.51281e-05, None, 0.0308449, None, -2.51281e-05, None, 0.031617, None, -8.43231e-05, None, 0.031617, None, -8.43231e-05, None, 0.518699, None, 0.00792462, None, 0.518699, None, 0.00792462, None)
reports[-1].CovMatrix = ['2.34996e-06','1.36713e-07','-3.34656e-09','6.75584e-10','0','0','0','0','0','1.36713e-07','0.000304816','2.77528e-09','8.13525e-09','0','0','0','0','0','-3.34656e-09','2.77528e-09','1.59715e-09','1.75426e-11','0','0','0','0','0','6.75584e-10','8.13525e-09','1.75426e-11','1.17145e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 123756
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0583453, 0.00146687, 0), \
                           ValErr(-0.0766309, 0.0168517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101789, 3.83238e-05, 0), \
                           -93585.6, 123756, 123756, -nan)
reports[-1].sigmaresid = ValErr(0.515444, 0.00103606, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.059176, None, 0.000163534, None, 0.0581818, None, 0.00020144, None, 0.0581818, None, 0.00020144, None, 0.0557356, None, 0.000198409, None, 0.0557356, None, 0.000198409, None, 0.515501, None, 0.00793972, None, 0.515501, None, 0.00793972, None)
reports[-1].CovMatrix = ['2.15171e-06','8.01701e-08','-2.67182e-09','6.26138e-10','0','0','0','0','0','8.01701e-08','0.000283981','4.80752e-09','7.44851e-09','0','0','0','0','0','-2.67182e-09','4.80752e-09','1.46871e-09','1.63821e-11','0','0','0','0','0','6.26138e-10','7.44851e-09','1.63821e-11','1.07342e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 118763
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0626508, 0.00150769, 0), \
                           ValErr(0.0889323, 0.0173215, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.20481e-05, 3.93131e-05, 0), \
                           -90609.9, 118763, 118763, -nan)
reports[-1].sigmaresid = ValErr(0.518927, 0.00106476, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0629359, None, -0.000823174, None, 0.0630033, None, -0.000870306, None, 0.0630033, None, -0.000870306, None, 0.0631662, None, -0.00096463, None, 0.0631662, None, -0.00096463, None, 0.518996, None, 0.00804561, None, 0.518996, None, 0.00804561, None)
reports[-1].CovMatrix = ['2.27313e-06','-6.96638e-07','-2.53356e-09','6.37527e-10','0','0','0','0','0','-6.96638e-07','0.000300033','7.92882e-09','7.74156e-09','0','0','0','0','0','-2.53356e-09','7.92882e-09','1.54552e-09','1.72932e-11','0','0','0','0','0','6.37527e-10','7.74156e-09','1.72932e-11','1.13371e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 116577
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0604473, 0.0015126, 0), \
                           ValErr(-0.0459915, 0.0173639, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.22681e-05, 3.94262e-05, 0), \
                           -88249.4, 116577, 116577, -nan)
reports[-1].sigmaresid = ValErr(0.515853, 0.00106833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0602499, None, -0.000172311, None, 0.0605253, None, -0.000188247, None, 0.0605253, None, -0.000188247, None, 0.0638311, None, -0.000197024, None, 0.0638311, None, -0.000197024, None, 0.515869, None, 0.00816177, None, 0.515869, None, 0.00816177, None)
reports[-1].CovMatrix = ['2.28795e-06','2.4418e-07','-2.81427e-09','6.61496e-10','0','0','0','0','0','2.4418e-07','0.000301504','1.82765e-09','7.9713e-09','0','0','0','0','0','-2.81427e-09','1.82765e-09','1.55442e-09','1.71086e-11','0','0','0','0','0','6.61496e-10','7.9713e-09','1.71086e-11','1.14133e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 104850
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0379502, 0.0016684, 0), \
                           ValErr(0.0150218, 0.0213489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.15985e-06, 4.19102e-05, 0), \
                           -80083.2, 104850, 104850, -nan)
reports[-1].sigmaresid = ValErr(0.519364, 0.00113416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0393347, None, -0.0011234, None, 0.0382685, None, -0.00123505, None, 0.0382685, None, -0.00123505, None, 0.037991, None, -0.00122359, None, 0.037991, None, -0.00122359, None, 0.519365, None, 0.00803818, None, 0.519365, None, 0.00803818, None)
reports[-1].CovMatrix = ['2.78357e-06','-9.77097e-06','-2.22399e-09','5.81654e-10','0','0','0','0','0','-9.77097e-06','0.000455778','2.85713e-08','8.2123e-09','0','0','0','0','0','-2.22399e-09','2.85713e-08','1.75647e-09','2.02918e-11','0','0','0','0','0','5.81654e-10','8.2123e-09','2.02918e-11','1.28631e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 117943
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00483038, 0.00150498, 0), \
                           ValErr(-0.013219, 0.0170835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.88412e-05, 3.93101e-05, 0), \
                           -89478.7, 117943, 117943, -nan)
reports[-1].sigmaresid = ValErr(0.516708, 0.00106388, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00526271, None, -0.000828094, None, 0.00487369, None, -0.000841156, None, 0.00487369, None, -0.000841156, None, 0.00721879, None, -0.000933918, None, 0.00721879, None, -0.000933918, None, 0.516711, None, 0.00824294, None, 0.516711, None, 0.00824294, None)
reports[-1].CovMatrix = ['2.26495e-06','2.56005e-07','-1.26514e-09','6.72336e-10','0','0','0','0','0','2.56005e-07','0.000291848','-3.61066e-09','7.76586e-09','0','0','0','0','0','-1.26514e-09','-3.61066e-09','1.54528e-09','1.7272e-11','0','0','0','0','0','6.72336e-10','7.76586e-09','1.7272e-11','1.13185e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 108158
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00900197, 0.00162265, 0), \
                           ValErr(0.0587104, 0.0207886, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00014658, 4.08093e-05, 0), \
                           -81262.7, 108158, 108158, -nan)
reports[-1].sigmaresid = ValErr(0.512935, 0.00110285, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00669374, None, -0.00105877, None, -0.00801528, None, -0.00107035, None, -0.00801528, None, -0.00107035, None, -0.0080324, None, -0.00112942, None, -0.0080324, None, -0.00112942, None, 0.512986, None, 0.00797967, None, 0.512986, None, 0.00797967, None)
reports[-1].CovMatrix = ['2.63299e-06','-9.18907e-06','-3.49549e-09','5.33107e-10','0','0','0','0','0','-9.18907e-06','0.000432167','2.83226e-08','7.66973e-09','0','0','0','0','0','-3.49549e-09','2.83226e-08','1.6654e-09','1.86872e-11','0','0','0','0','0','5.33107e-10','7.66973e-09','1.86872e-11','1.21629e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 123270
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0240579, 0.00147232, 0), \
                           ValErr(-0.00465816, 0.0169371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.37063e-05, 3.85151e-05, 0), \
                           -93510.2, 123270, 123270, -nan)
reports[-1].sigmaresid = ValErr(0.516666, 0.00104056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0231064, None, -1.22589e-05, None, -0.0241483, None, -3.54099e-05, None, -0.0241483, None, -3.54099e-05, None, -0.0246959, None, -2.17392e-05, None, -0.0246959, None, -2.17392e-05, None, 0.516674, None, 0.00803944, None, 0.516674, None, 0.00803944, None)
reports[-1].CovMatrix = ['2.16773e-06','-4.59961e-08','-1.80605e-09','6.28968e-10','0','0','0','0','0','-4.59961e-08','0.000286864','8.29978e-10','7.4876e-09','0','0','0','0','0','-1.80605e-09','8.29978e-10','1.48342e-09','1.65444e-11','0','0','0','0','0','6.28968e-10','7.4876e-09','1.65444e-11','1.08276e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 126879
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00264707, 0.0014894, 0), \
                           ValErr(-0.0960622, 0.0171525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000121218, 3.89749e-05, 0), \
                           -99595.5, 126879, 126879, -nan)
reports[-1].sigmaresid = ValErr(0.53048, 0.00105308, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00410495, None, -0.000318259, None, 0.00268865, None, -0.000257421, None, 0.00268865, None, -0.000257421, None, 0.00256911, None, -0.000297904, None, 0.00256911, None, -0.000297904, None, 0.530565, None, 0.00759577, None, 0.530565, None, 0.00759577, None)
reports[-1].CovMatrix = ['2.21832e-06','2.50118e-07','-5.04787e-10','6.78878e-10','0','0','0','0','0','2.50118e-07','0.000294208','4.1256e-09','7.93174e-09','0','0','0','0','0','-5.04787e-10','4.1256e-09','1.51904e-09','1.76903e-11','0','0','0','0','0','6.78878e-10','7.93174e-09','1.76903e-11','1.10897e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 125956
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0537121, 0.00151062, 0), \
                           ValErr(-0.0607976, 0.0171798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00024241, 4.00855e-05, 0), \
                           -100108, 125956, 125956, -nan)
reports[-1].sigmaresid = ValErr(0.535717, 0.00106736, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0531756, None, -0.000461164, None, 0.0541116, None, -0.000493611, None, 0.0541116, None, -0.000493611, None, 0.0517074, None, -0.000571008, None, 0.0517074, None, -0.000571008, None, 0.535819, None, 0.00777485, None, 0.535819, None, 0.00777485, None)
reports[-1].CovMatrix = ['2.28197e-06','6.52787e-07','1.82909e-09','7.5132e-10','0','0','0','0','0','6.52787e-07','0.000295145','1.54099e-08','8.47398e-09','0','0','0','0','0','1.82909e-09','1.54099e-08','1.60684e-09','1.97678e-11','0','0','0','0','0','7.5132e-10','8.47398e-09','1.97678e-11','1.13926e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 129116
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0571239, 0.00148415, 0), \
                           ValErr(0.0923554, 0.017135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.28285e-05, 3.8871e-05, 0), \
                           -101941, 129116, 129116, -nan)
reports[-1].sigmaresid = ValErr(0.532908, 0.00104869, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.056875, None, -0.000124657, None, 0.0572349, None, -0.000138749, None, 0.0572349, None, -0.000138749, None, 0.0577417, None, -0.000188787, None, 0.0577417, None, -0.000188787, None, 0.532972, None, 0.00764112, None, 0.532972, None, 0.00764112, None)
reports[-1].CovMatrix = ['2.2027e-06','-1.23889e-07','-2.18095e-09','6.57804e-10','0','0','0','0','0','-1.23889e-07','0.000293607','3.49099e-09','7.71906e-09','0','0','0','0','0','-2.18095e-09','3.49099e-09','1.51095e-09','1.6928e-11','0','0','0','0','0','6.57804e-10','7.71906e-09','1.6928e-11','1.09975e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 127653
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0772498, 0.00149149, 0), \
                           ValErr(0.0508773, 0.0171991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.12375e-05, 3.89196e-05, 0), \
                           -100628, 127653, 127653, -nan)
reports[-1].sigmaresid = ValErr(0.532248, 0.00105338, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.077023, None, -0.000439646, None, 0.0770518, None, -0.000481927, None, 0.0770518, None, -0.000481927, None, 0.0780144, None, -0.000528715, None, 0.0780144, None, -0.000528715, None, 0.532278, None, 0.00751097, None, 0.532278, None, 0.00751097, None)
reports[-1].CovMatrix = ['2.22455e-06','1.59071e-07','-2.82204e-09','6.52526e-10','0','0','0','0','0','1.59071e-07','0.00029581','2.00517e-09','7.92394e-09','0','0','0','0','0','-2.82204e-09','2.00517e-09','1.51474e-09','1.69606e-11','0','0','0','0','0','6.52526e-10','7.92394e-09','1.69606e-11','1.1096e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 126112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0493117, 0.00150125, 0), \
                           ValErr(0.000728188, 0.0173113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.15574e-06, 3.92209e-05, 0), \
                           -99558.2, 126112, 126112, -nan)
reports[-1].sigmaresid = ValErr(0.532861, 0.00106102, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0465006, None, -0.000382582, None, 0.0493052, None, -0.000458097, None, 0.0493052, None, -0.000458097, None, 0.0499468, None, -0.000479606, None, 0.0499468, None, -0.000479606, None, 0.532861, None, 0.0078223, None, 0.532861, None, 0.0078223, None)
reports[-1].CovMatrix = ['2.25375e-06','2.41855e-07','-1.77818e-09','6.8603e-10','0','0','0','0','0','2.41855e-07','0.000299681','-7.18426e-10','8.04996e-09','0','0','0','0','0','-1.77818e-09','-7.18426e-10','1.53828e-09','1.7372e-11','0','0','0','0','0','6.8603e-10','8.04996e-09','1.7372e-11','1.12575e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 125520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0181186, 0.00151366, 0), \
                           ValErr(0.0789363, 0.0174782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000121134, 3.94598e-05, 0), \
                           -99804.9, 125520, 125520, -nan)
reports[-1].sigmaresid = ValErr(0.5359, 0.00106958, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0175011, None, -0.000209458, None, 0.0180767, None, -0.000166232, None, 0.0180767, None, -0.000166232, None, 0.0176346, None, -0.000194282, None, 0.0176346, None, -0.000194282, None, 0.535964, None, 0.00744167, None, 0.535964, None, 0.00744167, None)
reports[-1].CovMatrix = ['2.29117e-06','6.58465e-07','-1.65145e-09','7.03616e-10','0','0','0','0','0','6.58465e-07','0.000305487','1.11012e-09','8.34669e-09','0','0','0','0','0','-1.65145e-09','1.11012e-09','1.55707e-09','1.79013e-11','0','0','0','0','0','7.03616e-10','8.34669e-09','1.79013e-11','1.144e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 128248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167847, 0.0014863, 0), \
                           ValErr(-0.0718649, 0.017143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.79554e-05, 3.87916e-05, 0), \
                           -101006, 128248, 128248, -nan)
reports[-1].sigmaresid = ValErr(0.531871, 0.00105019, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219045, None, 1.9328e-05, None, -0.00172962, None, 5.89263e-05, None, -0.00172962, None, 5.89263e-05, None, -0.00206252, None, 5.07455e-05, None, -0.00206252, None, 5.07455e-05, None, 0.531912, None, 0.00760458, None, 0.531912, None, 0.00760458, None)
reports[-1].CovMatrix = ['2.20909e-06','1.33818e-07','-2.20952e-09','6.54502e-10','0','0','0','0','0','1.33818e-07','0.000293883','3.82946e-09','7.87101e-09','0','0','0','0','0','-2.20952e-09','3.82946e-09','1.50479e-09','1.70758e-11','0','0','0','0','0','6.54502e-10','7.87101e-09','1.70758e-11','1.10289e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 131451
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0242621, 0.0014699, 0), \
                           ValErr(-0.0247659, 0.0169455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000196716, 3.84751e-05, 0), \
                           -103745, 131451, 131451, -nan)
reports[-1].sigmaresid = ValErr(0.532749, 0.00103903, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0232491, None, -0.000264813, None, -0.0244527, None, -0.000223673, None, -0.0244527, None, -0.000223673, None, -0.0261555, None, -0.000233862, None, -0.0261555, None, -0.000233862, None, 0.532805, None, 0.00749152, None, 0.532805, None, 0.00749152, None)
reports[-1].CovMatrix = ['2.16062e-06','4.71093e-08','-1.47064e-09','6.42435e-10','0','0','0','0','0','4.71093e-08','0.000287151','-1.30421e-09','7.62476e-09','0','0','0','0','0','-1.47064e-09','-1.30421e-09','1.48033e-09','1.69694e-11','0','0','0','0','0','6.42435e-10','7.62476e-09','1.69694e-11','1.07958e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 132118
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125105, 0.00146706, 0), \
                           ValErr(-0.0211628, 0.0169174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00021284, 3.85702e-05, 0), \
                           -104302, 132118, 132118, -nan)
reports[-1].sigmaresid = ValErr(0.532873, 0.00103664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0115786, None, 0.000303222, None, -0.0127738, None, 0.00046072, None, -0.0127738, None, 0.00046072, None, -0.0164495, None, 0.000502345, None, -0.0164495, None, 0.000502345, None, 0.532936, None, 0.00774193, None, 0.532936, None, 0.00774193, None)
reports[-1].CovMatrix = ['2.15227e-06','3.10601e-07','-2.00027e-09','6.44732e-10','0','0','0','0','0','3.10601e-07','0.000286198','-4.26444e-10','7.66557e-09','0','0','0','0','0','-2.00027e-09','-4.26444e-10','1.48766e-09','1.68574e-11','0','0','0','0','0','6.44732e-10','7.66557e-09','1.68574e-11','1.07463e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 45447
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.046625, 0.00493463, 0), \
                           ValErr(0.0360195, 0.0545772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000200962, 5.46391e-05, 0), \
                           -63244.7, 45447, 45447, -nan)
reports[-1].sigmaresid = ValErr(0.973045, 0.00322974, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0399762, None, -0.000349536, None, 0.0397486, None, -0.000302717, None, 0.0397486, None, -0.000302717, None, 0.042569, None, -0.000267345, None, 0.042569, None, -0.000267345, None, 0.973191, None, 0.00828563, None, 0.973191, None, 0.00828563, None)
reports[-1].CovMatrix = ['2.43505e-05','2.34403e-05','-1.01845e-07','2.34947e-08','0','0','0','0','0','2.34403e-05','0.00297867','-4.13711e-07','3.12507e-06','0','0','0','0','0','-1.01845e-07','-4.13711e-07','2.98543e-09','3.26531e-11','0','0','0','0','0','2.34947e-08','3.12507e-06','3.26531e-11','1.04312e-05','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 68416
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0338948, 0.00401023, 0), \
                           ValErr(0.0474665, 0.096779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.52893e-05, 4.46697e-05, 0), \
                           -93428.5, 68416, 68416, -nan)
reports[-1].sigmaresid = ValErr(0.948055, 0.00256122, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0287537, None, 0.000323218, None, 0.0317964, None, 0.000409407, None, 0.0317964, None, 0.000409407, None, 0.0296335, None, 0.000346525, None, 0.0296335, None, 0.000346525, None, 0.948067, None, 0.00809757, None, 0.948067, None, 0.00809757, None)
reports[-1].CovMatrix = ['1.6082e-05','-9.27259e-06','-7.6591e-08','1.62255e-08','0','0','0','0','0','-9.27259e-06','0.00936617','1.55146e-07','4.76403e-08','0','0','0','0','0','-7.6591e-08','1.55146e-07','1.99538e-09','-2.786e-10','0','0','0','0','0','1.62255e-08','4.76403e-08','-2.786e-10','6.55987e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 59905
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0444429, 0.00478781, 0), \
                           ValErr(0.148992, 0.105129, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000106211, 5.60831e-05, 0), \
                           -80229.9, 59905, 59905, -nan)
reports[-1].sigmaresid = ValErr(0.923437, 0.00266785, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0533049, None, -0.00083718, None, 0.0499868, None, -0.000778549, None, 0.0499868, None, -0.000778549, None, 0.050615, None, -0.000864975, None, 0.050615, None, -0.000864975, None, 0.923483, None, 0.00777391, None, 0.923483, None, 0.00777391, None)
reports[-1].CovMatrix = ['2.29231e-05','2.54697e-05','-1.65304e-07','3.8765e-09','0','0','0','0','0','2.54697e-05','0.011052','-4.36017e-07','1.54325e-07','0','0','0','0','0','-1.65304e-07','-4.36017e-07','3.14531e-09','3.50946e-11','0','0','0','0','0','3.8765e-09','1.54325e-07','3.50946e-11','7.11741e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 64308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0723812, 0.00445157, 0), \
                           ValErr(-0.207367, 0.101266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.67911e-05, 5.00015e-05, 0), \
                           -87030.4, 64308, 64308, -nan)
reports[-1].sigmaresid = ValErr(0.936506, 0.00260962, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0685251, None, -0.00185493, None, 0.0689635, None, -0.00167327, None, 0.0689635, None, -0.00167327, None, 0.0666764, None, -0.00181405, None, 0.0666764, None, -0.00181405, None, 0.936546, None, 0.00778571, None, 0.936546, None, 0.00778571, None)
reports[-1].CovMatrix = ['1.98165e-05','-1.06573e-05','-1.2505e-07','-3.05434e-09','0','0','0','0','0','-1.06573e-05','0.0102549','1.07731e-07','-2.06984e-07','0','0','0','0','0','-1.2505e-07','1.07731e-07','2.50015e-09','-3.19913e-10','0','0','0','0','0','-3.05434e-09','-2.06984e-07','-3.19913e-10','6.81013e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 69058
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0900264, 0.00399952, 0), \
                           ValErr(0.0359638, 0.0650785, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.96372e-06, 4.43922e-05, 0), \
                           -95399.3, 69058, 69058, -nan)
reports[-1].sigmaresid = ValErr(0.963195, 0.00253056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0920605, None, -0.000402067, None, 0.0901766, None, -0.000235933, None, 0.0901766, None, -0.000235933, None, 0.0919739, None, -0.000314096, None, 0.0919739, None, -0.000314096, None, 0.963194, None, 0.00814211, None, 0.963194, None, 0.00814211, None)
reports[-1].CovMatrix = ['1.59961e-05','-3.80142e-05','-7.19366e-08','3.05372e-07','0','0','0','0','0','-3.80142e-05','0.00423521','4.87888e-07','4.1314e-05','0','0','0','0','0','-7.19366e-08','4.87888e-07','1.97067e-09','-3.95758e-09','0','0','0','0','0','3.05372e-07','4.1314e-05','-3.95758e-09','6.40376e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 68564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0333581, 0.00403152, 0), \
                           ValErr(0.132026, 0.0972017, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000258658, 4.51187e-05, 0), \
                           -94851.1, 68564, 68564, -nan)
reports[-1].sigmaresid = ValErr(0.965082, 0.00259219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0456037, None, -0.00196328, None, 0.0427455, None, -0.00179325, None, 0.0427455, None, -0.00179325, None, 0.045715, None, -0.00191744, None, 0.045715, None, -0.00191744, None, 0.965323, None, 0.00806853, None, 0.965323, None, 0.00806853, None)
reports[-1].CovMatrix = ['1.62532e-05','-3.761e-06','-7.37171e-08','8.94365e-09','0','0','0','0','0','-3.761e-06','0.00944817','5.56459e-08','9.64136e-07','0','0','0','0','0','-7.37171e-08','5.56459e-08','2.0357e-09','-3.355e-10','0','0','0','0','0','8.94365e-09','9.64136e-07','-3.355e-10','6.71945e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 66440
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0675097, 0.00412706, 0), \
                           ValErr(-0.069282, 0.0987136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.67339e-05, 4.57115e-05, 0), \
                           -90983.6, 66440, 66440, -nan)
reports[-1].sigmaresid = ValErr(0.951679, 0.00261072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0638595, None, -0.000570266, None, 0.0648805, None, -0.000401561, None, 0.0648805, None, -0.000401561, None, 0.0643021, None, -0.000454794, None, 0.0643021, None, -0.000454794, None, 0.951698, None, 0.00808627, None, 0.951698, None, 0.00808627, None)
reports[-1].CovMatrix = ['1.70326e-05','1.32093e-05','-8.42168e-08','4.00389e-09','0','0','0','0','0','1.32093e-05','0.00974437','-1.29165e-07','1.47844e-07','0','0','0','0','0','-8.42168e-08','-1.29165e-07','2.08954e-09','4.01929e-11','0','0','0','0','0','4.00389e-09','1.47844e-07','4.01929e-11','6.81587e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 71939
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0926661, 0.00390741, 0), \
                           ValErr(0.134552, 0.0950599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.16923e-05, 4.39044e-05, 0), \
                           -99380.8, 71939, 71939, -nan)
reports[-1].sigmaresid = ValErr(0.963214, 0.00253937, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0901986, None, -0.000208603, None, 0.0909262, None, -0.000167443, None, 0.0909262, None, -0.000167443, None, 0.0892984, None, -0.000241156, None, 0.0892984, None, -0.000241156, None, 0.963237, None, 0.00819633, None, 0.963237, None, 0.00819633, None)
reports[-1].CovMatrix = ['1.52679e-05','-8.05036e-06','-6.75698e-08','3.63158e-09','0','0','0','0','0','-8.05036e-06','0.00903639','9.39164e-08','1.38717e-07','0','0','0','0','0','-6.75698e-08','9.39164e-08','1.9276e-09','4.35711e-11','0','0','0','0','0','3.63158e-09','1.38717e-07','4.35711e-11','6.4484e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 61873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0686259, 0.00430415, 0), \
                           ValErr(0.0503218, 0.0544858, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.95362e-05, 4.76631e-05, 0), \
                           -82558.6, 61873, 61873, -nan)
reports[-1].sigmaresid = ValErr(0.918865, 0.00261152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0625928, None, -0.000417314, None, 0.0672817, None, -0.000292584, None, 0.0672817, None, -0.000292584, None, 0.0709582, None, -0.000369903, None, 0.0709582, None, -0.000369903, None, 0.91887, None, 0.00804158, None, 0.91887, None, 0.00804158, None)
reports[-1].CovMatrix = ['1.85257e-05','3.37489e-06','-1.05486e-07','3.28775e-09','0','0','0','0','0','3.37489e-06','0.0029687','1.57155e-08','-3.95015e-07','0','0','0','0','0','-1.05486e-07','1.57155e-08','2.27177e-09','-4.57204e-11','0','0','0','0','0','3.28775e-09','-3.95015e-07','-4.57204e-11','6.82003e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 72066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0843344, 0.00387717, 0), \
                           ValErr(0.106927, 0.0949521, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000182404, 4.36603e-05, 0), \
                           -99548.3, 72066, 72066, -nan)
reports[-1].sigmaresid = ValErr(0.963108, 0.00253685, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0766118, None, 0.00189272, None, 0.0782225, None, 0.00178122, None, 0.0782225, None, 0.00178122, None, 0.081241, None, 0.00186024, None, 0.081241, None, 0.00186024, None, 0.963234, None, 0.00801991, None, 0.963234, None, 0.00801991, None)
reports[-1].CovMatrix = ['1.50325e-05','-5.20348e-06','-6.41773e-08','3.70725e-09','0','0','0','0','0','-5.20348e-06','0.00901589','8.65509e-08','1.39241e-07','0','0','0','0','0','-6.41773e-08','8.65509e-08','1.90623e-09','4.3925e-11','0','0','0','0','0','3.70725e-09','1.39241e-07','4.3925e-11','6.43561e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 72035
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0411592, 0.00375478, 0), \
                           ValErr(-0.0733866, 0.0922905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.90619e-06, 4.38021e-05, 0), \
                           -99531.3, 72035, 72035, -nan)
reports[-1].sigmaresid = ValErr(0.963455, 0.00250875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0392691, None, -0.000992987, None, 0.0411294, None, -0.000871513, None, 0.0411294, None, -0.000871513, None, 0.0407388, None, -0.000891712, None, 0.0407388, None, -0.000891712, None, 0.963457, None, 0.00791537, None, 0.963457, None, 0.00791537, None)
reports[-1].CovMatrix = ['1.40984e-05','2.46994e-05','-6.96476e-08','3.90473e-07','0','0','0','0','0','2.46994e-05','0.00851753','5.69188e-08','-7.58602e-06','0','0','0','0','0','-6.96476e-08','5.69188e-08','1.91863e-09','1.01834e-09','0','0','0','0','0','3.90473e-07','-7.58602e-06','1.01834e-09','6.29384e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 61329
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0233366, 0.00439018, 0), \
                           ValErr(0.172005, 0.101791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132741, 4.70462e-05, 0), \
                           -83364.5, 61329, 61329, -nan)
reports[-1].sigmaresid = ValErr(0.942106, 0.0026902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0138319, None, 0.000365749, None, 0.0173176, None, 0.000442986, None, 0.0173176, None, 0.000442986, None, 0.0166884, None, 0.000424542, None, 0.0166884, None, 0.000424542, None, 0.94219, None, 0.00769536, None, 0.94219, None, 0.00769536, None)
reports[-1].CovMatrix = ['1.92737e-05','-1.41563e-05','-1.02823e-07','-1.51506e-09','0','0','0','0','0','-1.41563e-05','0.0103615','1.08236e-07','-3.33977e-08','0','0','0','0','0','-1.02823e-07','1.08236e-07','2.21334e-09','-1.29355e-10','0','0','0','0','0','-1.51506e-09','-3.33977e-08','-1.29355e-10','7.23718e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 55443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.026313, 0.00463492, 0), \
                           ValErr(0.0359524, 0.0976366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00015726, 4.93219e-05, 0), \
                           -74783.8, 55443, 55443, -nan)
reports[-1].sigmaresid = ValErr(0.932308, 0.0025893, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00984576, None, -0.00205659, None, 0.0186865, None, -0.00188711, None, 0.0186865, None, -0.00188711, None, 0.0138985, None, -0.00196339, None, 0.0138985, None, -0.00196339, None, 0.932388, None, 0.00835768, None, 0.932388, None, 0.00835768, None)
reports[-1].CovMatrix = ['2.14824e-05','7.58755e-06','-1.20184e-07','-4.91855e-08','0','0','0','0','0','7.58755e-06','0.00953291','2.70871e-07','3.92997e-05','0','0','0','0','0','-1.20184e-07','2.70871e-07','2.43265e-09','-7.67991e-09','0','0','0','0','0','-4.91855e-08','3.92997e-05','-7.67991e-09','6.70448e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 59047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0090658, 0.00453991, 0), \
                           ValErr(0.138525, 0.105575, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127917, 4.76302e-05, 0), \
                           -80124.1, 59047, 59047, -nan)
reports[-1].sigmaresid = ValErr(0.939898, 0.00273506, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00128869, None, -0.000615515, None, 0.00279016, None, -0.000585475, None, 0.00279016, None, -0.000585475, None, 0.00295155, None, -0.000667694, None, 0.00295155, None, -0.000667694, None, 0.93997, None, 0.00780528, None, 0.93997, None, 0.00780528, None)
reports[-1].CovMatrix = ['2.06108e-05','-1.55558e-05','-1.13157e-07','3.71141e-09','0','0','0','0','0','-1.55558e-05','0.0111462','1.53746e-07','1.64092e-07','0','0','0','0','0','-1.13157e-07','1.53746e-07','2.26864e-09','4.37225e-11','0','0','0','0','0','3.71141e-09','1.64092e-07','4.37225e-11','7.48057e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 57278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0167828, 0.00464017, 0), \
                           ValErr(0.188776, 0.105941, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00016458, 4.94813e-05, 0), \
                           -77401.7, 57278, 57278, -nan)
reports[-1].sigmaresid = ValErr(0.93463, 0.00276141, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00583408, None, -0.00193735, None, 0.00821672, None, -0.0017337, None, 0.00821672, None, -0.0017337, None, 0.00627028, None, -0.00188599, None, 0.00627028, None, -0.00188599, None, 0.93474, None, 0.00797726, None, 0.93474, None, 0.00797726, None)
reports[-1].CovMatrix = ['2.15311e-05','3.14714e-05','-1.23767e-07','4.4452e-09','0','0','0','0','0','3.14714e-05','0.0112234','-2.99124e-07','1.67988e-07','0','0','0','0','0','-1.23767e-07','-2.99124e-07','2.4484e-09','3.80533e-11','0','0','0','0','0','4.4452e-09','1.67988e-07','3.80533e-11','7.62539e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 63745
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0292828, 0.00425379, 0), \
                           ValErr(0.346095, 0.103216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.77157e-07, 4.75282e-05, 0), \
                           -86653.9, 63745, 63745, -nan)
reports[-1].sigmaresid = ValErr(0.942186, 0.00263876, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.033932, None, -0.00222668, None, 0.0299252, None, -0.00202973, None, 0.0299252, None, -0.00202973, None, 0.0297905, None, -0.00221132, None, 0.0297905, None, -0.00221132, None, 0.942266, None, 0.0079599, None, 0.942266, None, 0.0079599, None)
reports[-1].CovMatrix = ['1.80947e-05','-1.73986e-05','-9.66422e-08','3.5893e-09','0','0','0','0','0','-1.73986e-05','0.0106536','-3.87665e-08','1.46043e-07','0','0','0','0','0','-9.66422e-08','-3.87665e-08','2.25893e-09','4.28593e-11','0','0','0','0','0','3.5893e-09','1.46043e-07','4.28593e-11','6.96307e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 66879
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171746, 0.00413519, 0), \
                           ValErr(-0.0918111, 0.0973669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143195, 4.56664e-05, 0), \
                           -91042.5, 66879, 66879, -nan)
reports[-1].sigmaresid = ValErr(0.943992, 0.00258112, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0220314, None, -0.0014433, None, 0.0232256, None, -0.00133485, None, 0.0232256, None, -0.00133485, None, 0.0266884, None, -0.00146402, None, 0.0266884, None, -0.00146402, None, 0.944069, None, 0.00823372, None, 0.944069, None, 0.00823372, None)
reports[-1].CovMatrix = ['1.70998e-05','-6.54671e-06','-8.8717e-08','3.58395e-09','0','0','0','0','0','-6.54671e-06','0.00948031','7.23267e-08','1.44761e-07','0','0','0','0','0','-8.8717e-08','7.23267e-08','2.08542e-09','4.2356e-11','0','0','0','0','0','3.58395e-09','1.44761e-07','4.2356e-11','6.66217e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 70926
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0509158, 0.00394109, 0), \
                           ValErr(0.0251298, 0.0569688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.60117e-05, 4.50272e-05, 0), \
                           -99186.9, 70926, 70926, -nan)
reports[-1].sigmaresid = ValErr(0.979726, 0.00259413, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0504686, None, -0.00286612, None, 0.0514928, None, -0.002694, None, 0.0514928, None, -0.002694, None, 0.0526567, None, -0.00288357, None, 0.0526567, None, -0.00288357, None, 0.979727, None, 0.00787507, None, 0.979727, None, 0.00787507, None)
reports[-1].CovMatrix = ['1.55322e-05','-6.29591e-05','-6.82076e-08','5.41668e-08','0','0','0','0','0','-6.29591e-05','0.00324545','8.55949e-08','1.84729e-06','0','0','0','0','0','-6.82076e-08','8.55949e-08','2.02745e-09','-8.14508e-10','0','0','0','0','0','5.41668e-08','1.84729e-06','-8.14508e-10','6.72949e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 65809
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0349968, 0.00481302, 0), \
                           ValErr(0.407794, 0.1028, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.38482e-05, 5.41447e-05, 0), \
                           -89775.2, 65809, 65809, -nan)
reports[-1].sigmaresid = ValErr(0.946714, 0.00260953, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.036955, None, -0.00137005, None, 0.0364241, None, -0.0013287, None, 0.0364241, None, -0.0013287, None, 0.0344709, None, -0.00141892, None, 0.0344709, None, -0.00141892, None, 0.946826, None, 0.00732721, None, 0.946826, None, 0.00732721, None)
reports[-1].CovMatrix = ['2.31652e-05','-3.99836e-05','-1.67059e-07','2.79449e-09','0','0','0','0','0','-3.99836e-05','0.0105679','4.10759e-07','1.50834e-07','0','0','0','0','0','-1.67059e-07','4.10759e-07','2.93164e-09','4.37292e-11','0','0','0','0','0','2.79449e-09','1.50834e-07','4.37292e-11','6.80965e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 68592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.041914, 0.00418021, 0), \
                           ValErr(-0.304, 0.0993402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.77108e-05, 4.83382e-05, 0), \
                           -95698.6, 68592, 68592, -nan)
reports[-1].sigmaresid = ValErr(0.97653, 0.00263654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0443635, None, -0.00391476, None, 0.0427881, None, -0.00365591, None, 0.0427881, None, -0.00365591, None, 0.0457066, None, -0.00387411, None, 0.0457066, None, -0.00387411, None, 0.976595, None, 0.00778212, None, 0.976595, None, 0.00778212, None)
reports[-1].CovMatrix = ['1.74741e-05','1.24746e-05','-9.13057e-08','4.08018e-09','0','0','0','0','0','1.24746e-05','0.00986847','-1.67541e-07','1.51379e-07','0','0','0','0','0','-9.13057e-08','-1.67541e-07','2.33658e-09','4.29544e-11','0','0','0','0','0','4.08018e-09','1.51379e-07','4.29544e-11','6.95136e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 47503
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0670746, 0.00549676, 0), \
                           ValErr(0.0129637, 0.128584, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000198525, 5.74927e-05, 0), \
                           -65342.7, 47503, 47503, -nan)
reports[-1].sigmaresid = ValErr(0.95754, 0.00310657, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.077168, None, -0.0021427, None, 0.0753984, None, -0.0019278, None, 0.0753984, None, -0.0019278, None, 0.0720763, None, -0.00199842, None, 0.0720763, None, -0.00199842, None, 0.957662, None, 0.00753105, None, 0.957662, None, 0.00753105, None)
reports[-1].CovMatrix = ['3.02144e-05','0.000285515','-1.55824e-07','1.10017e-08','0','0','0','0','0','0.000285515','0.0165338','-9.47557e-07','3.32517e-07','0','0','0','0','0','-1.55824e-07','-9.47557e-07','3.30541e-09','4.0527e-11','0','0','0','0','0','1.10017e-08','3.32517e-07','4.0527e-11','9.65079e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 76213
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0787485, 0.00381252, 0), \
                           ValErr(-0.0483981, 0.0478386, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.9042e-05, 4.30473e-05, 0), \
                           -107371, 76213, 76213, -nan)
reports[-1].sigmaresid = ValErr(0.989938, 0.00251975, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0784177, None, -0.000774397, None, 0.0802527, None, -0.000659049, None, 0.0802527, None, -0.000659049, None, 0.0756512, None, -0.000774062, None, 0.0756512, None, -0.000774062, None, 0.989952, None, 0.00788765, None, 0.989952, None, 0.00788765, None)
reports[-1].CovMatrix = ['1.45353e-05','2.69739e-06','-5.61738e-08','8.95607e-08','0','0','0','0','0','2.69739e-06','0.00228854','-2.27776e-08','1.07462e-05','0','0','0','0','0','-5.61738e-08','-2.27776e-08','1.85307e-09','-1.07302e-09','0','0','0','0','0','8.95607e-08','1.07462e-05','-1.07302e-09','6.34914e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 72680
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0424603, 0.0039244, 0), \
                           ValErr(0.0634372, 0.0952147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.03164e-05, 4.46043e-05, 0), \
                           -100384, 72680, 72680, -nan)
reports[-1].sigmaresid = ValErr(0.962949, 0.00252569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0402732, None, -0.000422984, None, 0.0439747, None, -0.000307538, None, 0.0439747, None, -0.000307538, None, 0.0416611, None, -0.000424709, None, 0.0416611, None, -0.000424709, None, 0.962957, None, 0.00785541, None, 0.962957, None, 0.00785541, None)
reports[-1].CovMatrix = ['1.5401e-05','-1.12974e-05','-7.2438e-08','3.4885e-09','0','0','0','0','0','-1.12974e-05','0.00906585','1.20552e-07','1.37769e-07','0','0','0','0','0','-7.2438e-08','1.20552e-07','1.98954e-09','4.34374e-11','0','0','0','0','0','3.4885e-09','1.37769e-07','4.34374e-11','6.37913e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 69395
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0676137, 0.00399116, 0), \
                           ValErr(0.0338562, 0.0975811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000179512, 4.59114e-05, 0), \
                           -97266.7, 69395, 69395, -nan)
reports[-1].sigmaresid = ValErr(0.982849, 0.0026382, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.076374, None, 2.50563e-05, None, 0.072959, None, 0.000111065, None, 0.072959, None, 0.000111065, None, 0.0717715, None, 8.91812e-05, None, 0.0717715, None, 8.91812e-05, None, 0.982958, None, 0.00779663, None, 0.982958, None, 0.00779663, None)
reports[-1].CovMatrix = ['1.59294e-05','2.69286e-05','-6.39541e-08','4.66509e-09','0','0','0','0','0','2.69286e-05','0.00952207','-4.42354e-08','1.5863e-07','0','0','0','0','0','-6.39541e-08','-4.42354e-08','2.10786e-09','4.78272e-11','0','0','0','0','0','4.66509e-09','1.5863e-07','4.78272e-11','6.96011e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 70124
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0765415, 0.00418712, 0), \
                           ValErr(-0.148561, 0.0970988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000160792, 4.72201e-05, 0), \
                           -97023.6, 70124, 70124, -nan)
reports[-1].sigmaresid = ValErr(0.965285, 0.00254133, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0672148, None, -0.00161961, None, 0.0694741, None, -0.00153283, None, 0.0694741, None, -0.00153283, None, 0.0680676, None, -0.00165658, None, 0.0680676, None, -0.00165658, None, 0.965374, None, 0.00750015, None, 0.965374, None, 0.00750015, None)
reports[-1].CovMatrix = ['1.7532e-05','-2.57129e-06','-9.73402e-08','1.17878e-07','0','0','0','0','0','-2.57129e-06','0.00942818','2.22654e-08','-2.9041e-06','0','0','0','0','0','-9.73402e-08','2.22654e-08','2.22974e-09','-1.58972e-09','0','0','0','0','0','1.17878e-07','-2.9041e-06','-1.58972e-09','6.45839e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 70776
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0652898, 0.00402708, 0), \
                           ValErr(0.0235716, 0.0508729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000105583, 4.50355e-05, 0), \
                           -98185.4, 70776, 70776, -nan)
reports[-1].sigmaresid = ValErr(0.968825, 0.00255875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0733384, None, 0.00109106, None, 0.0692879, None, 0.00107914, None, 0.0692879, None, 0.00107914, None, 0.0760971, None, 0.00108649, None, 0.0760971, None, 0.00108649, None, 0.968866, None, 0.00764788, None, 0.968866, None, 0.00764788, None)
reports[-1].CovMatrix = ['1.62174e-05','2.348e-05','-7.73339e-08','5.67065e-08','0','0','0','0','0','2.348e-05','0.00258805','-3.15823e-07','3.5585e-06','0','0','0','0','0','-7.73339e-08','-3.15823e-07','2.0282e-09','-6.36771e-10','0','0','0','0','0','5.67065e-08','3.5585e-06','-6.36771e-10','6.54719e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 69300
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0616099, 0.00419332, 0), \
                           ValErr(-0.0271162, 0.0508186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.09961e-05, 4.77282e-05, 0), \
                           -96234, 69300, 69300, -nan)
reports[-1].sigmaresid = ValErr(0.970172, 0.00259013, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0597278, None, 7.06126e-05, None, 0.0594768, None, 0.00017832, None, 0.0594768, None, 0.00017832, None, 0.0570078, None, 0.000136368, None, 0.0570078, None, 0.000136368, None, 0.970182, None, 0.00767708, None, 0.970182, None, 0.00767708, None)
reports[-1].CovMatrix = ['1.75839e-05','2.11174e-06','-9.54671e-08','5.25834e-08','0','0','0','0','0','2.11174e-06','0.00258254','1.53405e-08','9.0882e-06','0','0','0','0','0','-9.54671e-08','1.53405e-08','2.27798e-09','-7.99722e-10','0','0','0','0','0','5.25834e-08','9.0882e-06','-7.99722e-10','6.70876e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 72322
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0325248, 0.00397462, 0), \
                           ValErr(-0.140467, 0.096418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.90509e-05, 4.47954e-05, 0), \
                           -100743, 72322, 72322, -nan)
reports[-1].sigmaresid = ValErr(0.974382, 0.00255383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0331216, None, -0.000103423, None, 0.0304474, None, -2.23874e-05, None, 0.0304474, None, -2.23874e-05, None, 0.0368679, None, -2.06987e-05, None, 0.0368679, None, -2.06987e-05, None, 0.974407, None, 0.00778982, None, 0.974407, None, 0.00778982, None)
reports[-1].CovMatrix = ['1.57976e-05','1.04397e-05','-7.32714e-08','-1.13602e-08','0','0','0','0','0','1.04397e-05','0.00929643','-1.57777e-07','-7.36389e-07','0','0','0','0','0','-7.32714e-08','-1.57777e-07','2.00662e-09','-6.72797e-11','0','0','0','0','0','-1.13602e-08','-7.36389e-07','-6.72797e-11','6.52207e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 79345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0459389, 0.00373546, 0), \
                           ValErr(-0.127123, 0.0490912, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.48466e-05, 4.19824e-05, 0), \
                           -111433, 79345, 79345, -nan)
reports[-1].sigmaresid = ValErr(0.985581, 0.00247436, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0455557, None, -0.00152485, None, 0.0427985, None, -0.00142733, None, 0.0427985, None, -0.00142733, None, 0.0436665, None, -0.0015445, None, 0.0436665, None, -0.0015445, None, 0.985624, None, 0.00772083, None, 0.985624, None, 0.00772083, None)
reports[-1].CovMatrix = ['1.39536e-05','-3.7798e-05','-5.47962e-08','2.16546e-08','0','0','0','0','0','-3.7798e-05','0.00240995','4.6491e-07','9.64535e-08','0','0','0','0','0','-5.47962e-08','4.6491e-07','1.76253e-09','-3.68441e-10','0','0','0','0','0','2.16546e-08','9.64535e-08','-3.68441e-10','6.12246e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 56875
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0313185, 0.00475371, 0), \
                           ValErr(0.211394, 0.106471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.70652e-05, 5.15912e-05, 0), \
                           -76158, 56875, 56875, -nan)
reports[-1].sigmaresid = ValErr(0.923211, 0.00273732, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0338126, None, 0.00140213, None, 0.0296365, None, 0.00143976, None, 0.0296365, None, 0.00143976, None, 0.0280945, None, 0.00144111, None, 0.0280945, None, 0.00144111, None, 0.923248, None, 0.00742615, None, 0.923248, None, 0.00742615, None)
reports[-1].CovMatrix = ['2.25977e-05','-2.2472e-05','-1.42125e-07','3.51952e-09','0','0','0','0','0','-2.2472e-05','0.0113361','1.20039e-07','1.5796e-07','0','0','0','0','0','-1.42125e-07','1.20039e-07','2.66165e-09','4.34469e-11','0','0','0','0','0','3.51952e-09','1.5796e-07','4.34469e-11','7.49292e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 66233
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0164447, 0.0043183, 0), \
                           ValErr(-0.0961447, 0.100398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.21693e-05, 4.73989e-05, 0), \
                           -91417.1, 66233, 66233, -nan)
reports[-1].sigmaresid = ValErr(0.962036, 0.00264326, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0250776, None, 0.00145747, None, 0.0188111, None, 0.00135037, None, 0.0188111, None, 0.00135037, None, 0.0173122, None, 0.00139667, None, 0.0173122, None, 0.00139667, None, 0.962051, None, 0.00741626, None, 0.962051, None, 0.00741626, None)
reports[-1].CovMatrix = ['1.86477e-05','8.49925e-08','-1.02473e-07','3.76852e-09','0','0','0','0','0','8.49925e-08','0.0100798','-3.27658e-08','1.50905e-07','0','0','0','0','0','-1.02473e-07','-3.27658e-08','2.24665e-09','4.10004e-11','0','0','0','0','0','3.76852e-09','1.50905e-07','4.10004e-11','6.98683e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 59182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0187438, 0.0046647, 0), \
                           ValErr(-0.398669, 0.105275, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126242, 4.96112e-05, 0), \
                           -79684.1, 59182, 59182, -nan)
reports[-1].sigmaresid = ValErr(0.930054, 0.00270333, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0105661, None, -0.00294538, None, 0.0118008, None, -0.00270164, None, 0.0118008, None, -0.00270164, None, 0.0100587, None, -0.00283557, None, 0.0100587, None, -0.00283557, None, 0.930214, None, 0.00748606, None, 0.930214, None, 0.00748606, None)
reports[-1].CovMatrix = ['2.17594e-05','-1.01756e-05','-1.32584e-07','3.56097e-09','0','0','0','0','0','-1.01756e-05','0.0110827','1.1425e-07','1.61801e-07','0','0','0','0','0','-1.32584e-07','1.1425e-07','2.46127e-09','4.14462e-11','0','0','0','0','0','3.56097e-09','1.61801e-07','4.14462e-11','7.308e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 70119
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0566421, 0.00415497, 0), \
                           ValErr(0.123538, 0.0977528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000175951, 4.7491e-05, 0), \
                           -96599.7, 70119, 70119, -nan)
reports[-1].sigmaresid = ValErr(0.959557, 0.00255584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0456782, None, 0.00143023, None, 0.0492051, None, 0.00142153, None, 0.0492051, None, 0.00142153, None, 0.0538975, None, 0.00143896, None, 0.0538975, None, 0.00143896, None, 0.959662, None, 0.00756376, None, 0.959662, None, 0.00756376, None)
reports[-1].CovMatrix = ['1.72638e-05','-1.23391e-05','-9.64546e-08','3.08805e-08','0','0','0','0','0','-1.23391e-05','0.00955561','1.7201e-07','5.75395e-07','0','0','0','0','0','-9.64546e-08','1.7201e-07','2.25539e-09','-6.5882e-10','0','0','0','0','0','3.08805e-08','5.75395e-07','-6.5882e-10','6.53234e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 66298
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0287842, 0.0042087, 0), \
                           ValErr(-0.284561, 0.111649, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.35699e-05, 4.66021e-05, 0), \
                           -92864.2, 66298, 66298, -nan)
reports[-1].sigmaresid = ValErr(0.981937, 0.00269661, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0262414, None, 0.000859286, None, 0.0244588, None, 0.000829318, None, 0.0244588, None, 0.000829318, None, 0.0285629, None, 0.000826593, None, 0.0285629, None, 0.000826593, None, 0.982002, None, 0.00770093, None, 0.982002, None, 0.00770093, None)
reports[-1].CovMatrix = ['1.77131e-05','-7.66287e-05','-7.669e-08','3.36011e-09','0','0','0','0','0','-7.66287e-05','0.0124655','2.19513e-08','1.46182e-07','0','0','0','0','0','-7.669e-08','2.19513e-08','2.17175e-09','4.80628e-11','0','0','0','0','0','3.36011e-09','1.46182e-07','4.80628e-11','7.27173e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 72559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0378832, 0.00394471, 0), \
                           ValErr(0.144431, 0.096877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000110838, 4.38895e-05, 0), \
                           -101522, 72559, 72559, -nan)
reports[-1].sigmaresid = ValErr(0.980426, 0.00257345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0303816, None, -0.00189852, None, 0.0340329, None, -0.00168615, None, 0.0340329, None, -0.00168615, None, 0.0382094, None, -0.00180426, None, 0.0382094, None, -0.00180426, None, 0.980483, None, 0.00767576, None, 0.980483, None, 0.00767576, None)
reports[-1].CovMatrix = ['1.55607e-05','1.90551e-06','-6.66002e-08','2.14945e-08','0','0','0','0','0','1.90551e-06','0.00938515','-7.74456e-09','4.86832e-08','0','0','0','0','0','-6.66002e-08','-7.74456e-09','1.92629e-09','-2.87642e-10','0','0','0','0','0','2.14945e-08','4.86832e-08','-2.87642e-10','6.62266e-06','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]

