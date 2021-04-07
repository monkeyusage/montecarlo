
function random_walk(steps::Int64)::Array{Float64, 1}
    SQRT_STEPS = sqrt(steps)
    walk = ones(steps)
    for idx in 2:steps
        if rand() < .5
            y = -1
        else
            y = 1
        end
        walk[idx] = walk[idx-1] + (y / SQRT_STEPS)
    end
    walk
end

random_walk(100)

multiple = 1
for i in 1:8
    global multiple
    t = @elapsed random_walk(multiple)
    println("jl_random_walk\t$t")
    multiple *= 10
end